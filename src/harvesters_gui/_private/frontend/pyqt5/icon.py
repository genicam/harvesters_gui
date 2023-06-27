#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports

# Related third party imports
from PyQt5.QtGui import QIcon

# Local application/library specific imports
from harvesters_gui._helper import get_package_root
import os


class Icon(QIcon):
    dynamic_path = os.path.join('_private', 'frontend', 'image', 'icon')

    def __init__(self, file_name):
        #
        super().__init__(
            os.path.join(get_package_root(), self.dynamic_path, file_name)
        )
