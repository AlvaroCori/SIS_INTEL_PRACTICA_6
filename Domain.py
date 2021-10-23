class Domain:
    def __init__(self, day, hour, theme):
        self.day = day
        self.hour = hour
        self.theme = theme
        self.consist_values = 0
    
    def __lt__(self, other):
        return self.consist_values < other.consist_values
    
    def get_format(self):
        return str(self.day)+"-"+str(self.hour)+"-"+self.theme
