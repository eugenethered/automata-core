import time
import unittest
from datetime import datetime

from automata.core.instant.RunInstantHolder import RunInstantHolder


class RunInstantHolderTestCase(unittest.TestCase):

    def test_initializes_run_instant_as_default(self):
        RunInstantHolder.initialize()
        result = RunInstantHolder.run_instant
        self.assertRegex(result.isoformat(), r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+00:00$')

    def test_initialized_with_timestamp(self):
        instant = datetime.fromisoformat('2021-12-09T16:52:48.919605+00:00')
        RunInstantHolder.initialize(instant)
        result = RunInstantHolder.run_instant
        self.assertEqual('2021-12-09T16:52:48.919605+00:00', result.isoformat())

    def test_instant_conversion_as_number_represented_time(self):
        instant = datetime.fromisoformat('2021-12-09T16:52:48.919605+00:00')
        RunInstantHolder.initialize(instant)
        result = RunInstantHolder.numeric_run_instance()
        self.assertEqual(1639068768.919605, result)

    def test_multiple_initialization_should_different(self):
        RunInstantHolder.initialize()
        result = RunInstantHolder.numeric_run_instance()
        self.assertGreater(result, 0)
        time.sleep(1)
        RunInstantHolder.initialize()
        next_result = RunInstantHolder.numeric_run_instance()
        self.assertGreater(next_result, 0)
        self.assertGreater(next_result, result, 'Make sure RunInstantHolder.initialize() is called again')


if __name__ == '__main__':
    unittest.main()
