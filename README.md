# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for: processing, analyzing, and depositing NMR data._


#### [Project homepage](http://angusRobertson.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter -c v1 https://github.com/angusRobertson/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

### New version of Cookiecutter Data Science
------------
Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.


### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── bin                <- Shell scripts and compiled binaries.
├── data
│   ├── external       <- Data in/out of third party sources, eg. FLYA/CYANA 
│   ├── db             <- Analysis data stored in database format eg. .csv / SQL.
│   ├── interim        <- Intermediate data, eg. trial processing.
│   ├── final          <- The final, canonical data sets for modeling.j
│   └── raw            <- The original, immutable data, preferably symlinked to datastore.
|                         e.g. `ln -s path_to_data path_to_raw`
|
├── docs               <- A default Sphinx project; see sphinx-doc.org for details.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│   |                     the creator's initials, and a short `-` delimited description, e.g.
│   |                     `1.0-jqp-initial-data-exploration`.
│   ├── figures        <- Location for final figure generation notebooks.  
│   └── templates      <- Templates for common analyses.  
|
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── templates      <- Templates for reporting analysis  
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


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
