import io
import contextlib
from unittest import TestCase

class BaseTestCase(TestCase):
    def assertStdout(self, expected_output, func):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            func()
            output = buf.getvalue().strip()
            self.assertEqual(output, expected_output)
            