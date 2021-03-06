import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import requests

from python_program.employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    @patch('python_program.employee.requests.get')
    def test_monthly_schedule(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'
        schedule = self.emp_1.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/Schafer/May')
        self.assertEqual(schedule, 'Success')

    def test_monthly_schedule_false(self):
        with patch('python_program.employee.requests.get') as mocked_get:
            mocked_get.return_value.text = 'Bad Response!'
            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

    def test_monthly_schedule_mock(self):
        datetime = MagicMock(year=2017, month=3, date=23)
        self.emp_2.put_company_date(datetime)
        year = self.emp_2.get_company_date()
        self.assertEqual(year, 2017)


if __name__ == '__main__':
    unittest.main()