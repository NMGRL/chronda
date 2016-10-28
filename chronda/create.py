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
import shutil
import ruamel_yaml

from chronda import __version__
from chronda.base.context import context
from chronda.cli.user_input import get_user_confirmation
from chronda.exceptions import ChrondaEnvironmentExistsError, ChrondaInvalidPackageURI, ChrondaInvalidPackage
from chronda.package.anaconda import get_package_from_anaconda
from chronda.template.renderer import render_template


def _create_env(p):
    context.active_env = p
    os.mkdir(p)
    print 'Created New Environment at {}'.format(p)


def create_env(args):
    p = os.path.join(context.env_root, args.name)
    if not os.path.isdir(p):
        _create_env(p)
        return True
    else:
        if args.overwrite_env:
            if args.yes:
                yes = args.yes
            else:
                yes = get_user_confirmation('Overwrite the existing environment\n\t{}\n Proceed (y/n)?'.format(
                    args.name))

            if yes:
                shutil.rmtree(p)
                _create_env(p)
                return True
        else:
            raise ChrondaEnvironmentExistsError(p)


def get_package_root(package_uri):
    if package_uri.startswith('file:'):
        root = package_uri[5:]
    elif package_uri.startswith('anaconda:'):
        root = get_package_from_anaconda(package_uri)
    else:
        raise ChrondaInvalidPackageURI(package_uri)
    return root


def add_package(args):
    p = os.path.join(context.active_env, '.info.yml')
    if os.path.isfile(p):
        with open(p, 'r') as rfile:
            obj = ruamel_yaml.load(rfile)
            packages = obj['packages']
    else:
        obj = {}
        packages = []

    if args.package in packages:
        print 'package {} update to date'.format(args.package)
        return
    else:
        packages.append(args.package)
        obj['chronda_version'] = __version__
        obj['packages']= packages
        with open(p, 'w') as wfile:
            ruamel_yaml.dump(obj, wfile)
        return True


def transfer_payload(args):
    package_uri = args.package
    root = get_package_root(package_uri)
    src = os.path.join(root, 'payload')
    if not os.path.isdir(src):
        raise ChrondaInvalidPackage(package_uri)

    dst = context.active_env

    def func(sp, dp):
        print 'Copy {} >> {}'.format(os.path.relpath(sp, src),
                                     os.path.relpath(dp, dst))
        shutil.copyfile(sp, dp)

    walk_tree(args, src, dst, func)


def render_templates(args):
    package_uri = args.package
    root = get_package_root(package_uri)
    src = os.path.join(root, 'templates')
    dst = context.active_env

    walk_tree(args, src, dst, render_template)


def walk_tree(args, src, dst, func):
    for root, dirs, files in os.walk(src):
        if root == src:
            droot = dst
        else:
            droot = os.path.join(dst, os.path.relpath(root, src))

        if not os.path.isdir(droot):
            os.makedirs(droot)

        for f in files:
            if f in ('.DS_Store',):
                continue

            dp = os.path.join(droot, f)
            if args.overwrite or not os.path.isfile(dp):
                sp = os.path.join(root, f)
                func(sp, dp)

# ============= EOF =============================================
