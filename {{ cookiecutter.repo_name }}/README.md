{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── bin                <- Shell scripts and compiled binaries.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data, eg. trial processing.
│   ├── final          <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data, preferably symlinked to datastore.
|                         e.g. `ln -s path_to_data path_to_raw`
|
├── docs               <- A default Sphinx project; see sphinx-doc.org for details.
|
├── external
│   ├── input          <- Input to external programs, eg. CYANA/FLYA.
│   └── output         <- Output from external programs eg. CYANA/FLYA
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│   |                     the creator's initials, and a short `-` delimited description, e.g.
│   |                     `1.0-jqp-initial-data-exploration`.
│   └── templates      <- Templates for common analyses.  
|
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── validation     <- Validation of analysis workup.
│   ├── deposition     <- A default location for accumulation of deposition info.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
|
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download, generate, and process data.
│   │   └── process.py
│   │
│   ├── analysis       <- Utility Scripts for bespoke analysis
│   │   └── analysis.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
