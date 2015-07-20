# coding=utf-8

"""

   Copyright 2015 Andreas Würl

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""


class TestReport(object):
    def __init__(self, name, suites_by_module, build_number, is_incremental):
        self.name = name

        self.passed = 0
        self.failures = 0
        self.skipped = 0
        self.errors = 0
        self.duration = 0.0

        for suites in suites_by_module.values():
            self.passed = reduce(lambda value, current_suite: current_suite.passed + value, suites, self.passed)
            self.skipped = reduce(lambda value, current_suite: current_suite.skipped + value, suites, self.skipped)
            self.failures = reduce(lambda value, current_suite: current_suite.failures + value, suites, self.failures)
            self.errors = reduce(lambda value, current_suite: current_suite.errors + value, suites, self.errors)
            self.duration = reduce(lambda value, current_suite: current_suite.duration + value, suites, self.duration)

        self.suites_by_module = suites_by_module
        self.build_number = build_number
        self.is_incremental = is_incremental

    @property
    def total(self):
        return self.passed + self.skipped + self.failures + self.errors

    @property
    def is_successful(self):
        return self.errors == 0 and self.failures == 0 and self.passed > 0

    def __repr__(self):
        return "TestReport(total=" + str(self.total) + ", skipped=" + str(self.skipped) + ", failures=" \
               + str(self.failures) + ", errors=" + str(self.errors) + ", #suites=" + str(
            len(self.suites_by_module)) + ")"


class Failure(object):
    def __init__(self, message, type):
        self.message = message
        self.type = type
