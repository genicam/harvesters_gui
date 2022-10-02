#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2021 EMVA
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


import sys
from PyQt5.QtWidgets import QApplication
from harvesters_gui.frontend.pyqt5 import Harvester


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with Harvester() as h:
        h.show()
        sys.exit(app.exec_())
