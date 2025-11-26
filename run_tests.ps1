#!/bin/bash
pytest --platform desktop tests/test_launch_app.py --alluredir=reports/allure-results --clean-alluredir
allure serve reports/allure-results