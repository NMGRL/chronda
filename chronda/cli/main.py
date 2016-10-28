# ===============================================================================
# Copyright 2016 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================
import importlib
import sys
from argparse import SUPPRESS

from chronda import __version__


def generate_parser():
    from ..cli import chronda_argparse
    p = chronda_argparse.ArgumentParser(
        description='chronda is a tool for managing and deploying pychron'
                    ' environments and packages.')
    p.add_argument('-V', '--version',
                   action='version',
                   version='chronda {}'.format(__version__),
                   help="Show the conda version number and exit.")
    p.add_argument("--debug",
                   action="store_true",
                   help=SUPPRESS)
    p.add_argument("--json",
                   action="store_true",
                   help=SUPPRESS)
    sub_parsers = p.add_subparsers(metavar='command',
                                   dest='cmd')
    # http://bugs.python.org/issue9253
    # http://stackoverflow.com/a/18283730/1599393
    sub_parsers.required = True

    return p, sub_parsers


def _main():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    p, sub_parsers = generate_parser()

    # main_modules = ["info", "help", "list", "search", "create", "install", "update",
    #                 "remove", "config", "clean", "package"]
    modules = ('create', 'check','build','upload', 'help')
    for suffix in modules:
        module = 'chronda.cli.main_{}'.format(suffix)
        imported = importlib.import_module(module)
        imported.configure_parser(sub_parsers)

    args = p.parse_args()

    exit_code = args.func(args, p)
    if isinstance(exit_code, int):
        return exit_code

def main():
    from ..exceptions import exception_handler
    return exception_handler(_main)


if __name__ == '__main__':
    main()
# ============= EOF =============================================
