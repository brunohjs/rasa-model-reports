from typing import Dict

from rasa_model_report import __version__
from rasa_model_report.helpers import utils


class Controller:
    """
    Controller base class.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        project_version: str,
        **kwargs: dict
    ) -> None:
        """
        __init__ method.

        :param rasa_path: Project Rasa path.
        :param output_path: Output directory.
        :param project_name: Project name.
        :param project_version: Project version.
        """
        self.project_name: str = project_name
        self.project_version: str = project_version
        self.rasa_path: str = utils.remove_duplicate_slashs(rasa_path)
        self.actions_path = utils.remove_duplicate_slashs(kwargs.get("actions_path") or f"{self.rasa_path}/actions/")
        self.output_path: str = utils.remove_duplicate_slashs(output_path)
        self.nlu_path: str = utils.remove_duplicate_slashs(f"{self.rasa_path}/data")
        self.results_path: str = utils.remove_duplicate_slashs(f"{self.rasa_path}/results")
        self.images: Dict[str, str] = {
            "INTENT_HISTOGRAM": "intent_histogram.png",
            "INTENT_MATRIX": "intent_confusion_matrix.png",
            "ENTITY_HISTOGRAM": "DIETClassifier_histogram.png",
            "ENTITY_MATRIX": "DIETClassifier_confusion_matrix.png",
            "STORY_MATRIX": "story_confusion_matrix.png"
        }
        self.config_report_path: str = utils.remove_duplicate_slashs(f"{self.rasa_path}/config.yml")
        self.version: str = __version__
