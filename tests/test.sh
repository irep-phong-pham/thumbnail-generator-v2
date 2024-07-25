TEST_DIR=/app/test_reports
cd /app
pipenv run pytest --cov=. --cov-report html:$TEST_DIR/coverage --junit-xml=$TEST_DIR/junit.xml