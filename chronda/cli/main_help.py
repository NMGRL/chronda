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

descr = "Displays a list of available chronda commands and their help strings."

example = """
Examples:

    chronda help install
"""


def configure_parser(sub_parsers):
    p = sub_parsers.add_parser('help',
                               description=descr,
                               help=descr,
                               epilog=example)
    p.add_argument('command',
                   metavar='COMMAND',
                   action="store",
                   nargs='?',
                   help="""Print help information for COMMAND (same as: chronda COMMAND
        --help).""")
    p.set_defaults(func=execute)


def execute(args, parser):
    if not args.command:
        parser.print_help()
        return

    import sys
    import subprocess

    subprocess.call([sys.executable, sys.argv[0], args.command, '-h'])

# ============= EOF =============================================
