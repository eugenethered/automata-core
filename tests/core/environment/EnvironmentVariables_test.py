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

    def test_should_obtain_url_from_environment_variables(self):
        os.environ['URL'] = 'http://automata'
        environment_variables = EnvironmentVariables()
        self.assertEqual(environment_variables.url(), 'http://automata')

    def test_should_not_obtain_url_from_environment_variables_when_not_set(self):
        environment_variables = EnvironmentVariables()
        self.assertIsNone(environment_variables.url())


if __name__ == '__main__':
    unittest.main()
