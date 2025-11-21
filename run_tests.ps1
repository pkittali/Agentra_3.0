#!/bin/bash
pytest --platform web --clean-alluredir --alluredir=reports/allure-results
allure serve reports/allure-results