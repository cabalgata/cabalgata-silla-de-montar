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
""" Disk utilities
"""
import contextlib
import os
import shutil
import tempfile
import errno


@contextlib.contextmanager
def temp_directory(*args, **kwargs):
    """
    Context manager returns a path created by mkdtemp and cleans it up afterwards.
    """

    path = tempfile.mkdtemp(*args, **kwargs)
    try:
        yield path
    finally:
        shutil.rmtree(path)


def make_directories(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
