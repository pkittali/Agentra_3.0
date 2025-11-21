#!/bin/bash
<<<<<<< HEAD
pytest --platform web --clean-alluredir --alluredir=reports/allure-results
=======
pytest --platform web --alluredir=reports/allure-results --clean-alluredir
>>>>>>> 824352e915fb2814294b748fa689958889012cf3
allure serve reports/allure-results