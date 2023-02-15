#Riddhi Mahesh Dange
#Q1.
class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
    
    def __str__(self):
        if self.month > 9:
            month = str(self.month)
        else:
            month = "0"+str(self.month)
        if self.day > 9:
            day = str(self.day)
        else:
            day = "0"+str(self.day)
        d= month + "/" + day + "/" + str(self.year)
        return d
#d = Date(11, 4, 2021)
#print(d)

#Q2.
    def __eq__(self, other):
        return (self.day == other.day and self.month == other.month and self.year ==
        other.year)
#d1 = Date(1, 1, 2000)
#d2 = Date(1, 1, 2000)
#d3 = Date(1, 1, 2001)  
#print(d1 == d2)
#print(d1 == d3)

#Q3.
    def isLeapYear(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
#d1 = Date(1,1,1900)
#d2 = Date(1,1,2020)
#d3 = Date(1,1,2000)
#print(d1.isLeapYear())
#print(d2.isLeapYear())
#print(d3.isLeapYear()) 

#Q4.
    def isBefore(self, d2):
        if self.year == d2.year:
            if self.month == d2.month:
                if self.day == d2.day:
                    return False
                elif self.day < d2.day:
                    return True
                elif self.day > d2.day:
                    return False
            elif self.month > d2.month:
                return False
            elif self.month < d2.month:
                return True
        elif self.year > d2.year:
            return False
        elif self.year < d2.year:
            return True
        
        return False
#d1 = Date(1,1,2000)
#d2 = Date(1,1,2001)
#print(d1.isBefore(d2))
#print(d2.isBefore(d1))
#print(d1.isBefore(d1)) 

#Q5.
    def daysApart(self, other):
        monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
        x = self.year * 365 + self.day
        for item in range(0, self.month - 1):
            x += monthdays[item]
        x += Date.isLeapYear(self)

        y = other.year * 365 + other.day

        for item in range(0, other.month - 1):
            y += monthdays[item]
        
        y += Date.isLeapYear(other)
        
        return abs(y - x)       
#d1 = Date(1, 1, 2021)
#d2 = Date(1, 10, 2021)
#print(d1.daysApart(d2))
#print(d2.daysApart(d1))  
        
