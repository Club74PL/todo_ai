### Useful `pytest` Commands for Testing

| **Command**                              | **Description**                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------|
| `pytest <fn_name.py>`                    | Runs all tests in the specified file.                                          |
| `pytest -vv`                             | Runs tests with detailed output.                                               |
| `pytest --tb=long`                       | Displays the full traceback for errors.                                        |
| `pytest <fn_name.py>::test_specific`     | Runs a specific test in the file.                                              |
| `pytest -k "test_name"`                  | Runs only tests with "test_name" in their names.                               |
| `pytest -k "not test_name"`              | Runs all tests except those with "test_name" in their names.                   |
| `pytest -m slow`                         | Runs only tests marked with `@pytest.mark.slow`.                               |
| `pytest -m "not slow"`                   | Excludes tests marked with `@pytest.mark.slow`.                                |
| `pytest --cov=<module_name>`             | Checks the test coverage for the specified module.                             |
| `pytest --cov=<module_name> --cov-report=html` | Generates an HTML report for code coverage.                                   |
| `pytest --durations=3`                   | Displays the three slowest tests.                                              |
| `pytest -x`                              | Stops the test session after the first failure.                                |
| `pytest --junitxml=results.xml`          | Saves the test results in an XML file.                                         |
| `ptw`                                    | Watches for file changes and reruns tests automatically (requires `pytest-watch`). |
| `pytest --maxfail=2`                     | Stops the session after the second failure.                                    |
| `pytest --lf`                            | Runs only the tests that failed during the last session.                       |
| `pytest --ff`                            | Runs all tests but prioritizes the ones that failed last time.                 |
| `pytest -p no:warnings`                  | Disables warnings during test runs.                                            |
| `pytest --disable-warnings`              | Suppresses warnings output.                                                   |
| `pytest --tb=short`                      | Displays a shorter version of the traceback.                                   |
| `pytest --tb=none`                       | Hides all traceback information.                                               |
| `pytest -q`                              | Reduces the verbosity of the test output.                                      |
| `pytest --last-failed`                   | Runs only the tests that failed last time.                                     |
| `pytest -rA`                             | Shows a detailed report of all test statuses (passed, failed, skipped, etc.).  |
| `pytest -f`                              | Runs tests continuously, rerunning them after file changes.                    |
