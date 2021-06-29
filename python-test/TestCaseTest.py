from WasRun import WasRun
from TestCase import TestCase


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
    
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

    def setUp(self):
        pass

TestCaseTest("testSetUp").run()