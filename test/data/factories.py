#
# Copyright 2014 the original author or authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from cabalgata.silla.configuration import Definition


class FactoryA(object):
    definitions = [Definition('f', 'int', False, )]

    def __init__(self, directory, configuration=None):
        self.directory = directory
        self.installed = {}
        self.configuration = configuration or {}

    @staticmethod
    def versions():
        return ['1.2.3', '1.2.4']

    def install(self, name, version, configuration=None):
        self.installed[name] = version
        return A(version)

    def uninstall(self, name):
        self.installed.pop(name)

    def load(self, name):
        return A(self.installed[name])


class A(object):
    definitions = [Definition('f', 'int', False, )]

    def __init__(self, version):
        self.version = version
        self.running = False
        self.configuration = {}

    def configure(self, configuration):
        pass

    def start(self):
        self.running = True

    def stop(self, timeout=None):
        self.running = False

    def kill(self):
        self.running = False
