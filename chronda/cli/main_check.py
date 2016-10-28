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
from chronda.cli.common import add_package
from chronda.package.check import check_package

help = 'Check the given directory can be build into a chronda package'
descr = ''

example = """
Examples:

    chronda check .

"""


def configure_parser(sub_parsers):
    p = sub_parsers.add_parser('check',
                               description=descr,
                               help=help,
                               epilog=example)
    add_package(p)
    p.set_defaults(func=execute)


def execute(args, parser):
    check_package(args)
    print 'check for {} successful'.format(args.package_root)
    print
    print '# Now use'
    print '# $ chronda build {}'.format(args.package_root)
    print '# to build the chronda/conda package'
    print
# ============= EOF =============================================
