# tests/unit_test_runner.py
# Combining Test Suites - unittest

#  ----------------- Unit test framework
import unittest

#  ----------------  Individual test suites
from Problem_1.tests import test_problem_1 as test1
import Problem_2.tests.test_problem_2 as test2
import Problem_3.tests.test_problem_3 as test3
import Problem_4.tests.test_problem_4 as test4
import Problem_5.tests.test_problem_5 as test5
import Problem_6.tests.test_problem_6 as test6
import Problem_7.tests.test_problem_7 as test7
import Problem_8.tests.test_problem_8 as test8
import Problem_9.tests.test_problem_9 as test9
import Problem_10.tests.test_problem_10 as test10
import Problem_11.tests.test_problem_11 as test11
import Problem_12.tests.test_problem_12 as test12
import Problem_13.tests.test_problem_13 as test13
import Problem_14.tests.test_problem_14 as test14
import Problem_15.tests.test_problem_15 as test15
import Problem_16.tests.test_problem_16 as test16
import Problem_17.tests.test_problem_17 as test17
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



