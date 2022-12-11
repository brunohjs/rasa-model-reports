<div align="center">
<br />
<br />
<img
    height="180"
    alt="logo"
    src="https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/images/logo.png"
/>
<h4>Simple open source Rasa command-line add-on that generates training model health reports for your projects.</h4>
</div>
<hr />


<!-- Badges -->
![Python version](https://img.shields.io/static/v1?label=python&message=v3.10&color=3776AB)
![Code coverage](https://img.shields.io/static/v1?label=coverage&message=100%&color=brightgreen)
![Apache 2.0 License](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=yellowgreen)
![Contributors](https://img.shields.io/github/contributors/brunohjs/rasa-model-report)
<!--  -->


## 🔍 About
[Rasa](https://rasa.com/) is the most popular open source framework for building chat and voice-based AI assistants. The **rasa-model-report** is a unofficial Rasa add-on to facilitate the work of developers and curators of Rasa chatbots. Rasa provides a lot of valuable data that can be "faceted" and extract different information about the training model. This information makes it possible to discover problems in the training model. The **rasa-model-report** does just that, it extracts this information to be displayed more clearly in a report. You can see [this](https://github.com/brunohjs/rasa-model-report/blob/main/docs/markdown/sample_model_report.md) example.

<img
    height="22"
    alt="logo"
    src="https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/images/open_source_logo.png"
/>
***rasa-model-report** is a open source project.*

## 📜 Changelog
Changelog can be found [here](https://github.com/brunohjs/rasa-model-report/blob/main/CHANGELOG.md). You can also follow the [releases](https://github.com/brunohjs/rasa-model-report/releases) on Github and find planned enhancements for project in the [Project Board](https://github.com/users/brunohjs/projects/2).


## 📦 Installation

This module is distributed via [Pypi](https://pypi.org/) and is required to use **Python v3.10** or higher. To install the package, use the command:
```
pip install rasa-model-report
```


## 🚀 Execution
Before anything, is necessary to have the reports generated by the `rasa test` command. To run the program, use the command:
```
rasa-model-report
```
This command must be used in the root of your Rasa project. Otherwise, you can use `--path` parameter to pass the project path.

### Step-by-step
This is the step-by-step guide for using **rasa-model-report** in your project.
1. Go to the root folder of your Rasa project.
2. Train model on your Rasa project using `rasa train` command.
3. Run Rasa end-to-end tests using `rasa test` command.
   - This command will generate some data in json, markdown and image files in `result/` directory.
   - This data **is needed** for **rasa-model-report** to generate the report.
4. (Optional) If you want to know model NLU rating for each sentence in your project, run your project's Rasa API through the command `rasa run --enable-api`.
   - When you run **rasa-model-report**, automatically it will request NLU rating for each sentence. The result will be in the *NLU* section of the report.
   - If you don't want to use this option, just pass the parameter `--disable-nlu` or don't run Rasa API (if you don't run Rasa API, **rasa-model-report** will try to connect, after two tries it will skip this step).
5. Run **rasa-model-report** in root project.
   - If you haven't install it, see [how to install](https://github.com/brunohjs/rasa-model-report#-installation).
6. The result will be in the `model_report.md` file generated in the project root folder.

Below, I created this video to show how to use the **rasa-model-report**. I used the Rasa sample project (from `rasa-init` command). In this [link](https://github.com/brunohjs/rasa-model-report/blob/main/docs/markdown/sample_model_report.md) is the generated report.

https://user-images.githubusercontent.com/26513013/206880601-3145c3d6-e05f-4221-ba16-6a6da06a1edb.mp4


## 🦾 Rasa Version Support
Not every version of Rasa is supported. Check the table below:
|Rasa version|Supported|
|:-:|:-:|
|3.X|✅|
|2.X|✅|
|1.X|❌|
|0.X|❌|


## ⚙️ Options
There are parameters that can be used. Available options are below:

```
  --path TEXT         Rasa project path. (default: ./)
  --output-path TEXT  Report output path. (default: ./)
  --project TEXT      Rasa project name. It's only displayed in the report.
                      (default: My project)
  --version TEXT      Rasa project version. It's only displayed in the report
                      for project versioning. (default: not-identified)
  --rasa-api TEXT     Rasa API URL. Is needed to create NLU section of report.
                      (default: http://localhost:5005)
  --disable-nlu       Disable processing NLU sentences. NLU section will not
                      be generated in the report. Required Rasa API. (default:
                      false)
  -h, --help          Show this help message.
```


### Usage examples
Some usage examples with parameters:
- Without parameters is usually used at the root of the Rasa project.
    ```
    rasa-model-report
    ```
- When you aren't at the root of the project, use `--path` parameter.
    ```
    rasa-model-report --path /path/to/rasa/project
    ```
- Aren't at the root of the project and without NLU report.
    ```
    rasa-model-report --path /path/to/rasa/project --disable-nlu
    ```
- Aren't at the root of the project and change the report output directory.
    ```
    rasa-model-report --path /path/to/rasa/project --output-path path/to/place/report
    ```

## 💻 Development
For development, it's suggested to create an environment using the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation). To create new environment, use the command:
```
mkvirtualenv rasa-model-report --python 3.10
```
After that, your new environment will already be activated. If not, to activate just use the command:
```
workon rasa-model-report
```

### Installation
To install the development environment, use make command:
```
make install-dev
```
or use `pip install`:
```
pip install . -r requirements.txt -r requirements.dev.txt
```

### Test
Before test any changes you've made, you need to install the package again to update package files. Use the command:
```
pip install .
```
After that, you can test using `rasa-model-report` command with or without parameters.

To run unit tests, use `make test` or `pytest` command.


## 🐞 Bugs
Please file an issue for bugs, missing documentation, or unexpected behavior.

[See open issues](https://github.com/brunohjs/rasa-model-report/issues?q=is%3Aopen+is%3Aissue+label%3Abug)


## 💬 Discussions
Please file an issue to suggest new features. Vote on feature requests. This helps maintainers prioritize what to work on.

[See new ideas discussion](https://github.com/brunohjs/rasa-model-report/discussions/categories/ideas)


## ❓ Questions
For questions related to using the add-on, please ask the community on Q&A.

[See Q&A](https://github.com/brunohjs/rasa-model-report/discussions/categories/q-a)
