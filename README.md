# Project Template

## Description

This template serves as a guide for maintaining a standardized folder structure within a project.

## Folder Structure

The project is organized into thee main folders:

1. **data**:<br>
   This folder is for structuring the data in a way that enables relative imports and exports within the codebase.
2. **src**:<br>
   This folder contains all code, scripts, or notebooks related to the project.
3. **external**:<br>
   Use this folder to link any external repositories or code for backtracing.<br>

Each folder contains a README file providing detailed explanations of their respective purposes.

```shell
├── logbook.csv
├── data
│   ├── analyzed
│   ├── figures
│   ├── other
│   ├── processed
│   │   └── subject_1
│   │       └── session_1
│   └── raw
│       └── subject_1
│           └── session_1
├── external
└── src
    ├── analysis
    ├── data
    ├── experiment
    └── processing

```

## Logbook

A logbook.csv file is present in the root path which should be used from all researchers in every session<βρ>
The logbook has 5 mandatory columns. More can be added depending on the needs.

### Column description

1. **timestamp**:<br>
   UTC Day and time of the start of the session in the following format "YYYY-mm-DD HH:MM:ss +-TTTT".<br>
   +-TTTT is the timezone difference from UTC time.<br>
   e.g "2024-05-20 14:50:32 +0200"
2. **subject_id**:<br>
   The subject id of the session.<br>
   e.g "eg-3429"
3. **method**:<br>
   The method used in the session.<br>
   e.g. surgery, imaging, intrinsic etc.
4. **notes**:<br>
   All notes regarding the session.<br>
   Best would be to use JSON formatting.<br>
   For example, you can use the following as a starting template, but no strict rules are applied here.

   ```json
   {
     "subject": {
       "weight": 34.5,
       "dob": "2024-05-01"
     },
     "drugs": {
       "dosage": "1mg"
     },
     "watering": {
       "restriction": "1w"
     },
     "other_notes": ["highly stressed during surgery", "needed extra ketamine"]
   }
   ```

## Gitignore

The template is language-agnostic but includes specific exceptions for Python and MATLAB in .gitignore file. <br>
It's crucial to update this file as necessary to exclude unnecessary files from being synced to GitHub.

For instance, common data files are excluded by default.
If there's a need to sync PNG format figures with GitHub, remove the `*.png` exclusion from .gitignore.
However, exercise caution to ensure that only required files are synced and unnecessary ones are omitted.

## Usage

Push `use as template` button at the top right of [this page](https://github.com/poulet-lab/project-template/tree/main) to create a new repository based on this template.
Clone the repository and start developing there :)

## Suggest changes

Either open an issue or create a pull request with the change describing the current limitations and the solution.
