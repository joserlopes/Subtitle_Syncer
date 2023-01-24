class MyTime: 
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self): 
        return f"Hours: {self.hours}\nMinutes: {self.minutes}\nSeconds {self.seconds}\n"

    def __sub__(self, other):
        hours = self.hours - other.hours
        minutes = self.minutes - other.minutes
        seconds = self.seconds - other.seconds
        if (self.hours - other.hours < 0):
            hours -= 1
        if (self.minutes - other.minutes < 0):
            rest = other.minutes - self.minutes
            minutes = 60 - rest
            hours -= 1
        if (self.seconds - other.seconds < 0):
            rest = other.seconds - self.seconds
            seconds = 60 - rest
            minutes -= 1
        return MyTime(hours, minutes, seconds)        

    def __gt__(self, other):
        if self.hours > other.hours: 
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:            
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return True
        return False

    def __ge__(self, other):
        if self.hours >= other.hours: 
            return True
        elif self.hours == other.hours and self.minutes >= other.minutes:            
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds >= other.seconds:
            return True
        return False

    def __lt__(self, other):
        if (self.hours < other.hours):
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        return False
        
        

        