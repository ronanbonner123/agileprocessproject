# This will be our main file for integrating strings of code for our project
# This workflow will install Python dependencies & lint with a variety of Python version 3.11
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python


name: Agile Processes CI


on:
  [push]
  


jobs:
  build:


    runs-on: macos-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.11"]


    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
