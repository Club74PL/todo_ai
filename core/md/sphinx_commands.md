# Sphinx Commands Reference

Below is a table summarizing commonly used Sphinx commands with their descriptions:

| Command                                                                                          | Description                                                                                                   |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `docker compose exec project_template poetry run make html`                                      | Builds the HTML documentation using the `make` command in the Sphinx project.                                |
| `docker compose exec project_template poetry run sphinx-apidoc -o source ../project_template`    | Generates Sphinx API documentation for the `project_template` module and outputs it to the `source` folder. |
| `docker compose exec project_template poetry run sphinx-apidoc -f -o source ../project_template` | Forces regeneration of Sphinx API documentation and outputs it to the `source` folder.                      |
| `docker compose exec project_template poetry run sphinx-build -M html ./source ./build -v`       | Builds the Sphinx documentation to HTML format, specifying source and build directories with verbosity.      |
| `docker compose exec project_template poetry run make clean`                                     | Cleans up build artifacts generated during the documentation build process.                                  |
