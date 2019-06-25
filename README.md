A repo for Stepik test automation course.
https://stepik.org/course/575/

- `<conftest.py>` -- config file for the tests

# How to execute the tests:
- `<pytest -v --tb=line test_items.py>` - execute tests with default parameters.

- `<pytest -v --tb=line --language="ru" test_items.py>` - execute tests with a custom language parameter

- `<pytest -v --tb=line --browser=firefox --language="fr" test_items.py>` - execute the test in a specific browser with a custom language parameter. The defult browser is Chrome. You can select `<chrome>` or `<firefox>`.