from TestCase import TestCase
from this import d


class WasRun(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def testMethod(self) -> None:
        self.wasRun = 1
        self.log = self.log + 'testMethod '

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = 'setUp '
