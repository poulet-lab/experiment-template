# External

## Description

Use this folder to link any external repository or code for backtracing.</br>
In a case of a repository, git submodule is preferable.

## Git Submodule Guide

You can link another repository using git submodule by running the following command in the your repository's root path.

```shell
git submodule add {external_repo_url}
```

This will create a `.gitmodules` file in the root path

You can reference a specific branch by specifying the branch in this file.

```shell
[submodule {external_repo}]
    path = /externals/{external_repo}
    url = https://github.com/jzaccone/SubmoduleTestRepo.git
    branch = master
```

To clone all submodules use:

```shell
git clone --recurse-submodules {repo_url}
```

To fetch or pull all submodules use:

```shell
git pull --recurse-submodules
git fetch --recurse-submodules
```
