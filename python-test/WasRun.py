from TestCase import TestCase
from this import d


class WasRun(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = 'setUp '

    def testMethod(self) -> None:
        self.log = self.log + 'testMethod '

    def tearDown(self):
        self.log = self.log + 'tearDown '
