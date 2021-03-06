#
# Copyright 2014-15 the original author or authors
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
""" Factories
"""
import pkg_resources

ENTRY_POINT = 'cabalgata.factories'


def load_factory(name, directory, configuration=None):
    """ Load a factory and have it initialize in a particular directory
    :param name: the name of the plugin to load
    :param directory: the directory where the factory will reside
    :return:
    """
    for entry_point in pkg_resources.iter_entry_points(ENTRY_POINT):
        if entry_point.name == name:
            factory_class = entry_point.load(require=False)
            return factory_class(directory, configuration)

    raise KeyError
