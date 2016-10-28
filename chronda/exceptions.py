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
text_type = unicode


class ChrondaError(Exception):
    def __init__(self, message, **kwargs):
        self.message = message
        self._kwargs = kwargs
        super(ChrondaError, self).__init__(message)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return text_type(self.message.format(**self._kwargs))


class ChrondaExitZero(ChrondaError):
    pass


class ChrondaEnvironmentExistsError(ChrondaError):
    def __init__(self, path, **kw):
        super(ChrondaEnvironmentExistsError, self).__init__(path, **kw)
        self.message = 'Pychron Environment {} already exists'.format(path)


class ChrondaInvalidPackageURI(ChrondaError):
    def __init__(self, uri, **kw):
        super(ChrondaInvalidPackageURI, self).__init__(uri, **kw)
        self.message = 'Invalid URI= {}. URI must start with file: or anaconda:'.format(uri)


class ChrondaInvalidPackage(ChrondaError):
    def __init__(self, uri, **kw):
        super(ChrondaInvalidPackage, self).__init__(uri, **kw)
        self.message = 'Could not locate {}'.format(uri)


class ChrondaBadPackageError(ChrondaError):
    pass


def exception_handler(func, *args, **kw):
    try:
        return_value = func(*args, **kw)
        if isinstance(return_value, int):
            return return_value
    except ChrondaExitZero:
        return 0
    except ChrondaError, e:
        print '\n---------------------{}----------------------------'.format(repr(e))
        print e
        print '----------------------------------------------------------'
        return 1

# ============= EOF =============================================
