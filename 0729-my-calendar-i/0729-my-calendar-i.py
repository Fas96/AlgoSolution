class MyCalendar:

    def __init__(self):
        self.bookings = []  

    def book(self, start: int, end: int) -> bool: 
        for existingStart, existingEnd in self.bookings: 
            if start < existingEnd and end > existingStart:
                return False
         
        self.bookings.append((start, end))
        return True
 