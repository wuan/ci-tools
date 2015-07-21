import os
import tempfile
from unittest import TestCase
from assertpy import assert_that
from citools.persistence import Persistence


class PersistenceTest(TestCase):
    def test_with_block(self):
        output = tempfile.mkdtemp(prefix='persistence_test')
        persistence_file_name = os.path.join(output, 'name')
        with Persistence(persistence_file_name) as persistence:
            report = persistence.report

        assert_that(report).is_none()

        report_object = "foo"

        with Persistence(persistence_file_name) as persistence:
            persistence.report = report_object

        with Persistence(persistence_file_name) as persistence:
            report = persistence.report

        assert_that(report).is_equal_to(report_object)

        os.unlink(persistence_file_name)
        os.rmdir(output)

    def test_with_block_with_non_existent_path(self):
        self.assertRaises(Exception, lambda: Persistence('/non/existent/path'))
