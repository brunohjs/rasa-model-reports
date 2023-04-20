from pathlib import Path

from setuptools import find_packages
from setuptools import setup

import rasa_model_report


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="rasa-model-report",
    version=rasa_model_report.__version__,
    author="Bruno Justo",
    author_email="brunohjs@gmail.com",
    license="Apache 2.0",
    description="Simple open-source Rasa command-line add-on that "
                "generates training model health reports for your projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    url="https://github.com/brunohjs/rasa-model-report",
    packages=find_packages(),
    package_data={
        "": ["assets/css/*.css"]
    },
    package_dir={
        "": "."
    },
    install_requires=[
        "Click",
        "requests>=2.28.1",
        "pyyaml>=6.0"
    ],
    entry_points="""
        [console_scripts]
        rasa-model-report=rasa_model_report.main:main
    """,
)
