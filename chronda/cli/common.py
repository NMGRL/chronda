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
from chronda.base.context import context
from chronda.constants import NULL


def add_parser_yes(p):
    p.add_argument(
        "-y", "--yes",
        action="store_true",
        default=NULL,
        help="Do not ask for confirmation.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Only display what would have been done.",
    )

def add_parser_install(p):
    add_parser_prefix(p)
    p.add_argument('-p', '--package',
                   metavar='package_spec',
                   action='store',
                   # nargs='*',
                   help='Package to install into the chronda environment.')

    p.add_argument('-o', '--overwrite',
                   action='store_true',
                   help='Overwrite existing files')


def add_parser_prefix(p):
    # npgroup = p.add_mutually_exclusive_group()
    p.add_argument('name',
                   action='store',
                   help='Name of environment (in {}).'.format(context.env_root),
                   metavar='ENVIRONMENT',
                   # choices=Environments(),
                   )
    # p.add_argument(
    #     '-p', "--prefix",
    #     action="store",
    #     help="Full path to environment prefix (default: %s)." % context.default_prefix,
    #     metavar='PATH',
    # )

# ============= EOF =============================================
