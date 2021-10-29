**Installation of circleci, hadolint**
Installation of hadolint used in checking Docker file might be a problem for Linux users.Trying the sources from github hadolint might fail returing exit code 1 error . Solved this using [https://tcoil.info/how-to-install-hadolint-on-linux/](https://tcoil.info/how-to-install-hadolint-on-linux/) 

For circleci installation,for linux users adding either apt or sudo,helps to prevent permission.Official documentation [circleci-installation](https://circleci.com/docs/2.0/local-cli/)

Make commands are followed by a command in makefile example running run-circleci-local should have circleci-local in the Makefile. Failure to results to missing separator error.
