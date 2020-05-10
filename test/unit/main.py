#!/usr/bin/env python3

"""

mock
    - mock replace eternal interface
    - it create dummy object which having same interface to other
    - it not check return value or function behavior but it to check
    whether interface is called or not.

stub
    - Stub are used to generate predefined output.
    - stub used to return success, fail, exception to check program behavior
    in return value 

fake
    - fake is utility to create fake data like insted of connecting to external server
    we can connect to localhost server. Here localhost server is fake.
    - db connection can be implemented with memory db and fake it.

unittest
    - unittest is to check functionality not to avoid bugs.
    - unittest package is used to test data
    - setUp() tearDown() are object function execute before every test
    - setUpClass() tearDownClass() are class function execute first and last time only
    - test not run in order so set it isolated

pytest
    - Ref: https://www.tutorialspoint.com/pytest/index.htm
    - pytest library find all file start with test_*.py and execute them in dir
    - add pytest.main() function to execute all test case at perticular dir

Method
    .assertEqual(a, b)	            a == b
    .assertTrue(x)	                bool(x) is True
    .assertFalse(x)	                bool(x) is False
    .assertIs(a, b)	                a is b
    .assertIsNone(x)	            x is None
    .assertIn(a, b)	                a in b
    .assertIsInstance(a, b)         isinstance(a, b)

mocking
    - mock uses monkey patching attribute to copy data.
    patch
        - "from unittest.mock import patch" is used to mock some call depend on other lib like db
        - "with patch('package.file.obj.method') as mock_method" will mock perticular method
        - "mock_method.return_value" can be used for mocking return value
        - Example:
                with patch('python_program.employee.requests.get') as mocked_get:
                    mocked_get.return_value.ok = True
                    mocked_get.return_value.text = 'Success'

parameter
    V: more verbosity in test.
    k: matching string. Matching substring for test.
            $ pytest -k <substring> -v
            $ pytest -k "calculator" -v
    m: matching markname with decorator "@pytest.mark.<markername>"
            $ pytest -m <markername> -v


$ python3 test_cal.py
"""

import os
import sys
import pathlib
import pytest

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(pathlib.Path(__file__)), '..', '..', '..'))
    pytest.main(['-v', os.path.join(os.path.dirname(pathlib.Path(__file__)), '.')])