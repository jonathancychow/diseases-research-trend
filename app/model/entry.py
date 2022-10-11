class Entry:
    def __init__(self) -> None:
        self.year = []
        self.entry = []
    
    def _sort(self) -> None:
        self.year, self.entry = zip(*sorted(zip(self.year, self.entry)))