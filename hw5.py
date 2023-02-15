#Riddhi Mahesh Dange
import math
#Q1
def twoMaxes(L):
    rows, cols = len(L), len(L[0])
    maxRows = []
    maxCols = []      
    for row in range(rows):
        maxRows.append(max(L[row]))
    for col in range(cols):
        currColMax = float("-inf")
        for row in range(rows):
            currColMax = max(currColMax, L[row][col])
        maxCols.append(currColMax)
    return [maxRows, maxCols]

#Q2
def dictionaryCollector(L):
    resDict = {"int": 0, "string": ""}
    for item in L:
        if type(item) == int:
            resDict["int"] += item
        elif type(item) == str:
            resDict["string"] += item
    return resDict

#Q3
def selectionSort(L):
    for item in range(len(L)):
        min = item
        for i in range(item + 1, len(L)):
            if L[i] < L[min]:
                min = i
        L[item], L[min] = L[min], L[item]

#Q4
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return 'Radius: ' + str(self.radius)
    def area(self):
        return round(math.pi * (pow(self.radius, 2)), 2)
        
class Sphere(Circle):
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return 'Radius: ' + str(self.radius)
    def area(self):
        return round(4 * math.pi * (pow(self.radius, 2)), 2)
    def volume(self):
        return round((4/3) * math.pi * (pow(self.radius, 3)), 2)

#Q5
def preciseDivision(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return float(math.inf)
    except:
        return None

