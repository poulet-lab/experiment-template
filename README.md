# Project Template

## Description

This template serves as a guide for maintaining a standardized folder structure within a project.

## Folder Structure

The project is organized into thee main folders: `data`, `src` and `external`. <br>
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

A logbook.csv file is present in the root path which should be used from all researchers in every session

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
