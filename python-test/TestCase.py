class TestCase:
    def __init__(self, name) -> None:
        self.name = name
    
    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()