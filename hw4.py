class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours=hours
        self.minutes=minutes
        assert self.hours >=0 and self.hours<=23
        assert self.minutes>= 0 and self.minutes<=59
#Q1.
    def __str__(self):
        if self.hours<10 and self.minutes<10:
            return '0'+str(self.hours)+':'+'0'+str(self.minutes)
        if self.hours<10:
            return '0'+str(self.hours)+':'+str(self.minutes)
        if self.minutes<10:
            return str(self.hours)+ ':'+'0'+str(self.minutes)
        return str(self.hours)+':'+str(self.minutes)
#Q2.
    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes
#Q3.
    def isAfterNoon(self):
        if self.hours >= 12 and self.hours < 17:
            return True
        else:
            return False
#Q4.
    def isBefore(self, t2):
        if self.hours < t2.hours or self.minutes < t2.minutes:
            return True
        else:
            return False
#Q5.
    def tick(self):
        if self.minutes == 59:
            self.minutes = 0
            if self.hours == 23:
                self.hours = 0
            else:
                self.hours += 1
        else:
            self.minutes += 1
#Q6.
    def shortTimeApart(self, other):
        t = Time()
        if self.minutes == 59:
            t.hours = other.hours
            t.minutes = 1 + other.minutes
        elif other.minutes == 59:
            t.hours = self.hours
            t.minutes = 1 + self.minutes
        else:
            t.minutes = abs(self.minutes - other.minutes)

        return t
#Q7.
    def longTimeApart(self, other):
        t = Time()
        if self.minutes == 59:
            t.hours = self.hours
            t.minutes = self.minutes - other.minutes
        elif other.minutes == 59:
            t.hours = other.hours
            t.minutes = abs(self.minutes - other.minutes)
        else:
            t.minutes = abs(self.minutes - other.minutes)

        return t

#t= Time(10,59)
#print(t)
#t1= Time(11,21)
#t2=Time(11,21)
#t3=Time(11,22)
#print(t1==t2)
#print(t1==t3)
#t2=Time(13,22)
#print(t2.isAfterNoon())
#print(t1.isBefore(t1))
#str(t)
#t.tick()
#print(str(t))
#t1=Time(23,59)
#t2=Time(0,1)
#print(t1.shortTimeApart(t2))