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
from chronda.cli.common import add_parser_install, add_parser_yes
from chronda.constants import NULL
from chronda.create import create_env, transfer_payload, render_templates
from ..utils import on_win

help = "Create a new pychron environment from a list of specified packages. "
descr = (help +
         "To use the created environment, use 'source activate "
         "envname' look in that directory first.  This command requires either "
         "the -n NAME or -p PREFIX option.")

example = """
Examples:

    conda create -n myenv sqlite

"""


def configure_parser(sub_parsers):
    p = sub_parsers.add_parser('create',
                               description=descr,
                               help=help,
                               epilog=example)
    if on_win:
        p.add_argument("--shortcuts",
                       action="store_true",
                       help="Install start menu shortcuts",
                       dest="shortcuts",
                       default=NULL)
        p.add_argument("--no-shortcuts",
                       action="store_false",
                       help="Don't install start menu shortcuts",
                       dest="shortcuts",
                       default=NULL)
    add_parser_install(p)
    add_parser_yes(p)

    # add_parser_json(p)
    p.add_argument('-O', '--overwrite_env',
                   action='store_true',
                   help='Overwrite existing environment')

    p.add_argument("--clone",
                   action="store",
                   help='Path to (or name of) existing local environment.',
                   metavar='ENV')
    p.add_argument("--no-default-packages",
                   action="store_true",
                   help='Ignore create_default_packages in the .condarc file.')
    p.set_defaults(func=execute)


def execute(args, parser):
    if create_env(args):
        if args.package:
            transfer_payload(args)
            render_templates(args)

    # install(args, parser, 'create')
    # delete_trash()

# ============= EOF =============================================
