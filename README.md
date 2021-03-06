[![CircleCI](https://circleci.com/gh/ikostan/ProjectEuler.svg?style=svg)](https://circleci.com/gh/ikostan/ProjectEuler)
[![Build Status](https://travis-ci.org/ikostan/ProjectEuler.svg?branch=master)](https://travis-ci.org/ikostan/ProjectEuler)
[![codecov](https://codecov.io/gh/ikostan/ProjectEuler/branch/master/graph/badge.svg)](https://codecov.io/gh/ikostan/ProjectEuler)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/38a887c081ce407088010e417b580998)](https://www.codacy.com/manual/ikostan/ProjectEuler?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ikostan/ProjectEuler&amp;utm_campaign=Badge_Grade)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![HitCount](http://hits.dwyl.com/ikostan/ProjectEuler.svg)](http://hits.dwyl.com/ikostan/ProjectEuler)

# Python 3 solutions for Project Euler

![](https://github.com/ikostan/ProjectEuler/blob/master/ProjectEuler.png)

### What is Project Euler?

Project Euler ([projecteuler.net](http://projecteuler.net)) is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems.

### List of Completed Puzzles (Python 3):

| No. | GitHub Link | Difficulty Rating |                                                                                    
|-----|-------------|-------------------|
|1 - 100  |[Solution](https://github.com/ikostan/ProjectEuler/tree/master/Problems_1_to_100)| 5% - 10% |
|101 - 200|[N/A]()| 0% |
|201 - 300|[N/A]()| 0% |
|301 - 400|[N/A]()| 0% |
|401 - 500|[N/A]()| 0% |
|501 - 600|[N/A]()| 0% |

### Code Coverage Overview

website: [Codecov](https://codecov.io/)

```bash
   # 1) install codecov
   pip install codecov

   # 2) next call "codecov" at end of CI build
   # public repo using Travis, CircleCI or AppVeyor
   env:
    - CODECOV_TOKEN=<token>#IF ONLY YOU HAVE A PRIVATE REPOSITORY

   after_success:
    - codecov
```

### Travis CI: Building a Python Project

**.travis.yml** - Specify python versions using the python key. As we update the Python build images, aliases like 3.6 will point to different exact versions or patch levels.

```bash
language: python
python:
  - "2.6"
  - "2.7"
  - "3.3"
  - "3.4"
  - "3.5"
  - "3.5-dev"  # 3.5 development branch
  - "3.6"
  - "3.6-dev"  # 3.6 development branch
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script:
  - pytest
```

<img align="right" width="" height="" src="https://projecteuler.net/profile/iKostan.png">
