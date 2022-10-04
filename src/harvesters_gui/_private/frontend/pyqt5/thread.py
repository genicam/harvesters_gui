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
from PyQt5.QtCore import QMutexLocker, QThread

# Local application/library specific imports
from harvesters.core import ThreadBase


class _PyQtThreadBase(ThreadBase):
    def __init__(self, parent=None, mutex=None, worker=None, update_cycle_us=1):
        #
        super().__init__(mutex=mutex)
        self._thread = None

    def acquire(self):
        return self._thread.acquire()

    def release(self):
        self._thread.release()

    @property
    def worker(self):
        return self._thread.worker

    @worker.setter
    def worker(self, obj):
        self._thread.worker = obj

    @property
    def mutex(self):
        return self._mutex

    @property
    def id_(self):
        return self._thread.id_

    def is_running(self) -> bool:
        return self._is_running

    def join(self):
        pass

    def _internal_stop(self):
        self._thread.stop()
        self._thread.wait()
        self._is_running = False

    def _internal_start(self) -> None:
        self._is_running = True
        self._thread.start()


class _PyQtThread(_PyQtThreadBase):
    def __init__(self, parent=None, mutex=None, worker=None, update_cycle_us=1):
        #
        super().__init__(mutex=mutex)

        #
        self._thread = _ThreadImpl(
            parent=parent, base=self, worker=worker,
            update_cycle_us=update_cycle_us
        )


class _PyQtModuleEventMonitorThread(_PyQtThreadBase):
    def __init__(self, parent=None, mutex=None, worker=None, update_cycle_us=1):
        #
        super().__init__(mutex=mutex)

        #
        self._thread = _ModuleEventMonitorThreadImpl(
            parent=parent, base=self, worker=worker,
            update_cycle_us=update_cycle_us
        )


class _ThreadImplBase(QThread):
    def __init__(self, parent=None, base=None, worker=None,
                 update_cycle_us=1):
        #
        super().__init__(parent)

        #
        self._worker = worker
        self._base = base
        self._update_cycle_us = update_cycle_us

    def stop(self):
        with QMutexLocker(self._base.mutex):
            self._base._is_running = False

    def run(self):
        raise NotImplementedError

    def acquire(self):
        return QMutexLocker(self._base.mutex)

    def release(self):
        pass

    @property
    def worker(self):
        return self._worker

    @worker.setter
    def worker(self, obj):
        self._worker = obj

    @property
    def id_(self):
        return int(self.currentThreadId())


class _ThreadImpl(_ThreadImplBase):
    def __init__(self, parent=None, base=None, worker=None,
                 update_cycle_us=1):
        #
        super().__init__(parent=parent, base=base, worker=worker, update_cycle_us=update_cycle_us)

    def run(self):
        while self._base.is_running():
            if self._worker:
                self._worker()
                # Force the current thread to sleep for some microseconds:
                self.usleep(self._update_cycle_us)


class _ModuleEventMonitorThreadImpl(_ThreadImplBase):
    def __init__(self, parent=None, base=None, worker=None,
                 update_cycle_us=1):
        super().__init__(parent=parent, base=base, worker=worker, update_cycle_us=update_cycle_us)

    def run(self):
        while self._base.is_running():
            if self._worker:
                self._worker()
                self.msleep(10)


