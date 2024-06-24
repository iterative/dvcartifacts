## Getting artifacts from GitHub monorepo projects without cloning the entire monorepo

`dvcartifacts` is a Python CLI tool which relies on gitpython and ssh to authenticate with the remote repo

It uses sparse checkout without downloading anything outside of the project directory to speed things up.

It relies on `boto3` or `google-cloud-storage` to access the bucket (depending on the cloud storage used as a remote).

```cli
usage: dvcartifacts [-h] [-r REV] repourl projectdir artifact_name

Download an artifact from the remote bucket

positional arguments:
  repourl            url of the GitHub repository associated with the artifact
  projectdir         project subdirectory in the monorepo where the artifact was created
  artifact_name      Name of the artifact to find

options:
  -h, --help         show this help message and exit
  -r REV, --rev REV  GTO tag of the artifact (optional)
```

TODO: Handle the situation where the remote is in a subdirectory in the bucket
