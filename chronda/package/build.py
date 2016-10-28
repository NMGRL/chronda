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
import os

import ruamel_yaml

from chronda.cli.user_input import get_user_input
from chronda.utils import on_win


def build_package(args):
    create_meta(args)
    if on_win:
        create_bat(args)
    else:
        create_sh(args)


def create_bat(args):
    p = os.path.join(args.package_root, 'bld.bat')
    with open(p, 'w') as wfile:
        pass


def create_sh(args):
    p = os.path.join(args.package_root, 'build.sh')
    with open(p, 'w') as wfile:
        pass


def create_meta(args):
    """
    package:
      name: pyinstrument
      version: "0.13.1"

    source:
      git_rev: v0.13.1
      git_url: https://github.com/joerick/pyinstrument.git

    requirements:
      build:
        - python
        - setuptools
      run:
        - python

    test:
      imports:
        - pyinstrument

    about:
      home: https://github.com/joerick/pyinstrument
      license: BSD
      license_file: LICENSE

    :param root:
    :return:
    """
    meta = {'package': get_package(args),
            'about': get_about(),
            'source': {'path': '../src'}}
    p=os.path.join(args.package_root, 'meta.yaml')
    with open(p, 'w') as wfile:
        ruamel_yaml.dump(meta, wfile, default_flow_style=False)


def get_about():
    home = 'https://github.com/NMGRL/chronda'
    return {'home': home,
            'license': 'Apache 2.0'}


def get_package(args):
    pname = os.path.basename(args.package_root)
    name = get_user_input('Package name', default=pname)
    version = get_user_input('Version', default='0.0.1')
    pkg = {'name': name,
           'version': version}

    return pkg

# ============= EOF =============================================
