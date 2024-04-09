set /p token="Enter token here: "
twine upload -u __token__ -p %token% --skip-existing dist/*
pause