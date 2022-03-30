import argparse
import getpass


class PasswordPromptAction(argparse.Action):
    def __init__(self, option_strings, dest=None, nargs=0, default=None, required=False, type=None, metavar=None, help=None):
        super(PasswordPromptAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            default=default,
            required=required,
            metavar=metavar,
            type=type,
            help=help)

    def __call__(self, parser, args, values, option_string=None):
        password = getpass.getpass()
        setattr(args, self.dest, password)
