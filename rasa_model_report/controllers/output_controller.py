import logging
import os.path

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.controllers.csv_controller import CsvController
from rasa_model_report.controllers.e2e_coverage_controller import E2ECoverageController
from rasa_model_report.controllers.json_controller import JsonController
from rasa_model_report.controllers.nlu_controller import NluController
from rasa_model_report.helpers import constants
from rasa_model_report.helpers import utils


class OutputController(Controller):
    """
    Controller responsible for PDF files.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        rasa_version: str,
        project_version: str,
        **kwargs
    ) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param rasa_version: Rasa version.
        :param project_version: Project version.
        """
        super().__init__(rasa_path, output_path, project_name, project_version, **kwargs)

        self.result: str = ""
        self.format: str = kwargs.get("output_format", constants.OUTPUT_FORMAT)
        self.title: str = "Model health report"
        self.output_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.html")
        self.readme_path: str = "README.md"
        self.rasa_version: str = rasa_version
        self.model_link: str = kwargs.get("model_link")
        self.no_images: bool = kwargs.get("no_images", constants.NO_IMAGES)
        self.precision: int = kwargs.get("precision", constants.GRADE_PRECISION)
        self.json: JsonController = JsonController(rasa_path, output_path, project_name, project_version)
        self.csv: CsvController = CsvController(rasa_path, output_path, project_name, project_version)
        self.nlu: NluController = NluController(
            rasa_path,
            output_path,
            project_name,
            project_version,
            url=kwargs.get("rasa_api_url", constants.RASA_API_URL),
            disable_nlu=kwargs.get("disable_nlu", constants.DISABLE_NLU)
        )
        self.e2e_coverage: E2ECoverageController = E2ECoverageController(
            rasa_path,
            output_path,
            kwargs.get("actions_path"),
            project_name,
            project_version
        )

        self.json.update_overview({
            "nlu": self.nlu.general_grade,
            "e2e_coverage": self.e2e_coverage.total_rate
        })
        logging.info(f"Model output format: {self.format}")
        if self.no_images:
            logging.info("--no-images activated. Images will not be displayed in the report.")

    def add_text(self, text: str) -> None:
        """
        Concatenates a text to the result text.

        :param text: Text that concatenates.
        """
        raise NotImplementedError("")

    def add_image(self, image_filename: str, title: str) -> None:
        """
        Concatenates image (markdown format) into the result text.

        :param image_filename: Image file name.
        :param title: Image title.
        """
        raise NotImplementedError("")

    def add_title(self, title, description=None, heading_level=2, tag=None):
        """
        Concatenates a title and description to the result text.

        :param title: Title text.
        :param description: Description text (default: None).
        :param int heading_level: Heading level (default: 2).
        :param tag: Tag for an anchor link (default: None).
        """
        raise NotImplementedError("")

    def add_credits(self) -> str:
        """
        Build the report credits block.

        :return str: Text block in markdown format.
        """
        self.result += f"<h6>Generated by rasa-model-report v{self.version}, collaborative open-source project for " \
            "Rasa projects. Github repository at this " \
            "<a href='https://github.com/brunohjs/rasa-model-report'>link</a>.</h6>"

    def save_report(self) -> None:
        """
        Save the report data to file.
        """
        if os.path.isfile(self.output_report_path):
            text = f"{self.output_report_path} file successfully changed."
        else:
            text = f"{self.output_report_path} file successfully created."
        file = open(self.output_report_path, "w", encoding="utf-8")
        file.write(self.result)
        file.close()
        logging.info(text)

    def save_overview(self) -> None:
        """
        Save the overview report to JSON file.
        """
        self.json.save_overview()

    def generate_report(self) -> None:
        """
        Function that generates the report.
        """
        if os.path.isdir(self.results_path):
            # Overview
            self.add_title(self.title, heading_level=1)
            self.add_text(self.build_summary())
            self.add_text(self.build_overview())

            # Config
            if os.path.isfile(self.config_report_path):
                self.add_title(
                    "Configs",
                    "Settings that were used in the training pipeline and policies.",
                    tag="configs"
                )
                self.add_text(self.build_config_report())

            # Intents
            self.add_title(
                "Intents",
                "Section that discusses metrics on model intents.",
                tag="intents"
            )
            self.add_text(self.build_intent_table())
            self.add_text(self.build_intent_errors_table())
            self.add_image(self.images["INTENT_HISTOGRAM"], "Histogram")
            self.add_image(self.images["INTENT_MATRIX"], "Confusion Matrix")

            # Entities
            self.add_title(
                "Entities",
                "Section that discusses metrics about the model entities.",
                tag="entities"
            )
            self.add_text(self.build_entity_table())
            self.add_text(self.build_entity_errors_table())
            self.add_image(self.images['ENTITY_HISTOGRAM'], "Histogram")
            self.add_image(self.images['ENTITY_MATRIX'], "Confusion Matrix")

            # NLU
            if self.nlu.is_connected():
                self.add_title(
                    "NLU",
                    "Section that discusses metrics about NLU and its example phrases.",
                    tag="nlu"
                )
                self.add_text(self.build_nlu_table())
                self.add_text(self.build_nlu_errors_table())

            # Core
            self.add_title(
                "Core",
                "Section that discusses metrics about bot responses and actions.",
                tag="core"
            )
            self.add_text(self.build_core_table())
            self.add_image(self.images['STORY_MATRIX'], "Confusion Matrix")

            # E2E Coverage
            self.add_title(
                "E2E Coverage",
                "Section that shows data from intents, entities and responses that aren't covered by end-to-end tests",
                tag="e2e"
            )
            self.add_text(self.build_e2e_coverage_list())

            # Credits
            self.add_credits()

            # Save report and overview files
            self.save_report()
            self.save_overview()

            logging.info("Script successfully completed.")
        else:
            logging.error(f"{self.images['results_path']} directory doesn't exist.")
            logging.error(
                "To inform the directory where the Rasa project files are located, use the --path parameter."
            )
            logging.error("Script finished with errors.")
