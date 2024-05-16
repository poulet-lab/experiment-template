# Data

## Description

This folder is for structuring the data in a way that enables relative imports and exports within the codebase. <br>
With the exception of figures, no data should be synchronized to GitHub.

## Folder Structure

### Raw

Reserved for raw data files. <br>
If raw data is stored in a cloud storage or drive, consider using [symbolic links](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/) or cache mechanisms to access it from this folder.

The structure of the subfolders should be as follows

```shell
./{subject_name}/{session_id}/{files}.{extension}
```

### Processed

Houses all processed data exported from any `src/processing/*` script. <br>
Ensure that processed data is synchronized with cloud storage for backup purposes.

The structure of the subfolders should be as follows

```shell
./{subject_name}/{session_id}/{files}.{extension}
```

### Analyzed

Houses all analyzed data exported from any `src/analysis/*` script. <br>
Ensure that analyzed data is synchronized with cloud storage for backup purposes.

### Figures

Intended for exported figures and graphs from the `src/analysis/*` scripts. <br>
These files can be stored on GitHub or any cloud storage platform.

### Other

For any other data that doesn't fit into the categories mentioned above. <br>
Syncing to GitHub is at the discretion of the individual.
