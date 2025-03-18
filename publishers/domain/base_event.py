class Event:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.__class__.__name__}(data={self.data})"
