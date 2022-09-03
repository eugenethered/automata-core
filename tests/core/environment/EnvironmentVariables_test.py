import os
import unittest

from core.environment.EnvironmentVariables import EnvironmentVariables


class EnvironmentVariablesTestCase(unittest.TestCase):

    def test_should_obtain_basic_environment_variables(self):
        environment_variables = EnvironmentVariables()
        self.assertTrue('PATH' in environment_variables.options)

    def test_should_obtain_specific_environment_variables(self):
        os.environ['CUSTOM_VAR'] = 'Cat In the Hat'
        environment_variables = EnvironmentVariables()
        self.assertEqual(environment_variables.options['CUSTOM_VAR'], 'Cat In the Hat')


if __name__ == '__main__':
    unittest.main()
