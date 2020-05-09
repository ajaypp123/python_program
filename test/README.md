### mock
- mock replace eternal interface
- it create dummy object which having same interface to other
- it not check return value or function behavior but it to check whether interface is called or not.

### stub
- Stub are used to generate predefined output.
stub used to return success, fail, exception to check program behavior in return value 

### fake
- fake is utility to create fake data like instead of connecting to external server we can connect to localhost server. Here localhost server is fake.
- db connection can be implemented with memory db and fake it.

### unittest
- unittest is to check functionality not to avoid bugs
- unittest package is used to test data
- setUp() tearDown() are object function execute before every test
- setUpClass() tearDownClass() are class function execute first and last time only
- test not run in order so set it isolated

### pytest
- [Ref](https://www.tutorialspoint.com/pytest/index.htm)
- pytest library find all file start with test_*.py and execute them in dir
- add pytest.main() function to execute all test case at perticular dir

### Method
```
    .assertEqual(a, b)          a == b
    .assertTrue(x)	            bool(x) is True
    .assertFalse(x)	            bool(x) is False
    .assertIs(a, b)	            a is b
    .assertIsNone(x)	        x is None
    .assertIn(a, b)	            a in b
    .assertIsInstance(a, b)     isinstance(a, b)
```

### mocking
- mock uses monkey patching attribute to copy data.
    - patch
        - "from unittest.mock import patch" is used to mock some call depend on other lib like db
        - "with patch('package.file.obj.method') as mock_method" will mock perticular method
        - "mock_method.return_value" can be used for mocking return value
        - Example:
        ```
        @patch('python_program.employee.requests.get')
        def test_monthly_schedule(self, mocked_get):
                        or
        def test_monthly_schedule(self):
        with patch('python_program.employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
        ```
        - Uses
            - It is used to manipulate internal call of function. The call not in parameter and return value.
            - In above example request is used in middle of function

    - MagicMock
        - `unittest.mock` provides a class called `Mock` which you will use to imitate real objects in your codebase.
        - With mock create fake object and with help of monkey patching add property to object to work like real object.
        - [Ref](https://realpython.com/python-mock-library/)
        - side_effect used when handing exception under mock class
        - assert call method
            ```
                from unittest.mock import MagicMock
                json = MagicMock()
                json.loads('{"key": "value"}')
                json.loads.assert_called()                              # Make sure loads called
                json.loads.assert_called_once()                         # Make sure loads called only once
                json.loads.assert_called_with('{"key": "value"}')       # Make sure loads called with value
                json.loads.assert_called_once_with('{"key": "value"}')  # Make sure loads called with value only once
            ```
        - Uses
            - It is used as parameter or return value of function
            - To mock object in call

### parameter
- `V` : more verbosity in test.
- `k` : matching string. Matching substring for test.
    ```
        $ pytest -k <substring> -v
        $ pytest -k "calculator" -v
    ```
- `m` : matching markname with decorator `@pytest.mark.<markername>`
    ```    
        $ pytest -m <markername> -v
        $ python3 test_cal.py
    ```
- `--maxfail = <num>` : Test exist after max fail reach.
- `n 3` : mean run 3 test in parallel. For this need to install `pip install pytest-xdist`
- `--junitxml="result.xml"` : Put output in xml file.

### decorator
- `@pytest.mark.<markername>`
    - It used for test function to catagories as label
    - $ pytest -m <markername> -v
    - above cmd can be used to call specific test cases.
- `@pytest.fixture`
    - Fixtures are functions, which will run before each test function to which it is applied.
    - Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data.
    - Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
    - Add all fixture to conftest.py to access across multiple test cases.
        ```
        import pytest

        @pytest.fixture
        def input_value():
        input = 39
        return input

        def test_divisible_by_3(input_value):
        assert input_value % 3 == 0

        def test_divisible_by_6(input_value):
        assert input_value % 6 == 0
        ```
- `@pytest.mark.parametrize`
    - It used to provide parameter to function.
    - we can provide multiple parameter to test performance.
    ```
        import pytest

        @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
        def test_multiplication_11(num, output):
            assert 11*num == output
   ```
- `@pytest.mark.xfail`
    - In these situations, we have the option to xfail the test or skip the tests.
    - Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests.
- `@pytest.mark.skip`
    - Skipping a test means that the test will not be executed.

### packages
```
    $ pip install pytest
    $ pip install pytest-xdist
    $ pip install mock
```