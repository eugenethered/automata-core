import unittest

from metainfo.MetaInfo import MetaInfo

from core.arguments.command_line_arguments import option_arg_parser


class CommandLineArgumentsTestCase(unittest.TestCase):

    def setUp(self):
        self.meta_info = MetaInfo('persuader-technology-automata-core', '../../../')

    def test_arg_parser_should_obtain_description_from_setup_cfg(self):
        command_line_arg_parser = option_arg_parser(self.meta_info)
        description = command_line_arg_parser.description
        self.assertEqual(description, 'Automata Core')

    def test_arg_parser_should_obtain_version_from_setup_cfg(self):
        command_line_arg_parser = option_arg_parser(self.meta_info)
        args = command_line_arg_parser.parse_args()
        self.assertRegex(args.version, r'^\d+\.\d+\.\d+$')

    def test_arg_parser_should_process_options(self):
        command_line_arg_parser = option_arg_parser(self.meta_info)
        args = command_line_arg_parser.parse_args(['--options', 'location=earth'])
        self.assertTrue('location' in args.options)
        self.assertEqual(args.options['location'], 'earth')

    def test_arg_parser_should_process_options_and_have_version_included(self):
        command_line_arg_parser = option_arg_parser(self.meta_info)
        args = command_line_arg_parser.parse_args(['--options', 'location=earth'])
        self.assertTrue('version' in args.options)
        self.assertRegex(args.options['version'], r'^\d+\.\d+\.\d+$')


if __name__ == '__main__':
    unittest.main()
