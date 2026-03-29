


class BufferedFlush:
    def __init__(self, limit):
        self.items = []
        self.limit = limit
        self.flush = None
        self.args  = {}

    def add(self, item):
        self.items.append(item)
        if len(self.items) >= self.limit:
            self.flush(self.items, self.args)
            self.items = []
    
    def end(self): 
        self.flush(self.items, self.args)
        self.items = []
