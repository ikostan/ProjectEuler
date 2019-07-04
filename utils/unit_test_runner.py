# tests/unit_test_runner.py
# Combining Test Suites - unittest

#  ----------------- Unit test framework
import unittest

#  ----------------  Individual test suites
from Problems_1_to_100.Problem_1.tests import test_problem_1 as test1
import Problems_1_to_100.Problem_2.tests.test_problem_2 as test2
import Problems_1_to_100.Problem_3.tests.test_problem_3 as test3
import Problems_1_to_100.Problem_4.tests.test_problem_4 as test4
import Problems_1_to_100.Problem_6.tests.test_problem_6 as test6
import Problems_1_to_100.Problem_8.tests.test_problem_8 as test8
import Problems_1_to_100.Problem_10.tests.test_problem_10 as test10
import Problems_1_to_100.Problem_11.tests.test_problem_11 as test11
import Problems_1_to_100.Problem_12.tests.test_problem_12 as test12
from Problems_1_to_100 import Problem_14 as test14, Problem_5 as test5, Problem_13 as test13, Problem_16 as test16, \
    Problem_9 as test9, Problem_7 as test7
import Problems_1_to_100.Problem_15.tests.test_problem_15 as test15
import Problems_1_to_100.Problem_17.tests.test_problem_17 as test17
#import Problem_18.test_problem_8 as test18
#import Problem_67.test_problem_9 as test67



# -----------------  Load all the test cases
suiteList = list()
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test1.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test2.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test3.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test4.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test5.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test6.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test7.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test8.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test9.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test10.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test11.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test12.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test13.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test14.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test15.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test16.MyTestCase))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test17.MyTestCase))
#suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test18.MyTestCase))
#suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test67.MyTestCase))


# ----------------   Join them together ane run them
comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=2).run(comboSuite)

'''
# Testing utils
- pytest --cov-report term-missing --cov=utils utils/tests/ # check test coverage with pytest-cov
# Problem 1
#- python -m pytest Problem_1/tests/ # run unit tests with pytest
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_1 Problems_1_to_100/Problem_1/tests/ # check test coverage with pytest-cov
# Problem 2
#- python -m pytest Problem_2/tests/ # run unit tests with pytest
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_2 Problems_1_to_100/Problem_2/tests/ # check test coverage with pytest-cov
# Problem 3
#- python -m pytest Problem_3/tests/ # run unit tests with pytest
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_3 Problems_1_to_100/Problem_3/tests/ # check test coverage with pytest-cov
# Problem 4
#- python -m pytest Problem_4/tests/ # run unit tests with pytest
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_4 Problems_1_to_100/Problem_4/tests/ # check test coverage with pytest-cov
# Problem 5
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_5 Problems_1_to_100/Problem_5/tests/ # check test coverage with pytest-cov
# Problem 6
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_6 Problems_1_to_100/Problem_6/tests/ # check test coverage with pytest-cov
# Problem 7
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_7 Problems_1_to_100/Problem_7/tests/ # check test coverage with pytest-cov
# Problem 8
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_8 Problems_1_to_100/Problem_8/tests/ # check test coverage with pytest-cov
# Problem 9
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_9 Problems_1_to_100/Problem_9/tests/ # check test coverage with pytest-cov
# Problem 10
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_10 Problems_1_to_100/Problem_10/tests/ # check test coverage with pytest-cov
# Problem 11
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_11 Problems_1_to_100/Problem_11/tests/ # check test coverage with pytest-cov
# Problem 12
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_12 Problems_1_to_100/Problem_12/tests/ # check test coverage with pytest-cov
# Problem 13
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_13 Problems_1_to_100/Problem_13/tests/ # check test coverage with pytest-cov
# Problem 14
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_14 Problems_1_to_100/Problem_14/tests/ # check test coverage with pytest-cov
# Problem 15
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_15 Problems_1_to_100/Problem_15/tests/ # check test coverage with pytest-cov
# Problem 16
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_16 Problems_1_to_100/Problem_16/tests/ # check test coverage with pytest-cov
# Problem 17
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_17 Problems_1_to_100/Problem_17/tests/ # check test coverage with pytest-cov
# Problem 18
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_18 Problems_1_to_100/Problem_18/tests/ # check test coverage with pytest-cov
# Problem 19
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_19 Problems_1_to_100/Problem_19/tests/ # check test coverage with pytest-cov
# Problem 20
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_20 Problems_1_to_100/Problem_20/tests/ # check test coverage with pytest-cov
# Problem 21
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_21 Problems_1_to_100/Problem_21/tests/ # check test coverage with pytest-cov
# Problem 22
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_22 Problems_1_to_100/Problem_22/tests/ # check test coverage with pytest-cov
# Problem 23
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_23 Problems_1_to_100/Problem_23/tests/ # check test coverage with pytest-cov
# Problem 24
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_24 Problems_1_to_100/Problem_24/tests/ # check test coverage with pytest-cov
# Problem 25
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_25 Problems_1_to_100/Problem_25/tests/ # check test coverage with pytest-cov
# Problem 26
#- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_26 Problems_1_to_100/Problem_26/tests/ # check test coverage with pytest-cov
# Problem 28
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_28 Problems_1_to_100/Problem_28/tests/ # check test coverage with pytest-cov
# Problem 29
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_29 Problems_1_to_100/Problem_29/tests/ # check test coverage with pytest-cov
# Problem 30
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_30 Problems_1_to_100/Problem_30/tests/ # check test coverage with pytest-cov
# Problem 32
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_32 Problems_1_to_100/Problem_32/tests/ # check test coverage with pytest-cov
# Problem 34
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_34 Problems_1_to_100/Problem_34/tests/ # check test coverage with pytest-cov
# Problem 35
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_35 Problems_1_to_100/Problem_35/tests/ # check test coverage with pytest-cov
# Problem 36
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_36 Problems_1_to_100/Problem_36/tests/ # check test coverage with pytest-cov
# Problem 37
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_37 Problems_1_to_100/Problem_37/tests/ # check test coverage with pytest-cov
# Problem 41
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_41 Problems_1_to_100/Problem_41/tests/ # check test coverage with pytest-cov
# Problem 48
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_48 Problems_1_to_100/Problem_48/tests/ # check test coverage with pytest-cov
# Problem 67
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_67 Problems_1_to_100/Problem_67/tests/ # check test coverage with pytest-cov
# Problem 99
- pytest --cov-report term-missing --cov=Problems_1_to_100/Problem_99 Problems_1_to_100/Problem_99/tests/ # check test coverage with pytest-cov
'''
