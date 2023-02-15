#Riddhi Mahesh Dange
#Q1. Spiral Function
def spiral(L):
    currRow, currCol, currDir = 0, 0, 0
    cols = len(L) - 1
    rows = len(L[0]) - 1
    res = []
    
    while currCol <= cols and currRow <= rows:
        if currDir == 0:
            for iterator in range(currRow, rows + 1):
                res.append(L[currCol][iterator])
            currCol += 1
        elif currDir == 90:
            for iterator in range(currCol, cols + 1):
                res.append(L[iterator][rows])
            rows -= 1
        elif currDir == 180:
            for iterator in range(rows, currRow - 1, -1):
                res.append(L[cols][iterator])
            cols -= 1
        else:
            for iterator in range(cols, currCol - 1, -1):
                res.append(L[iterator][currRow])
            currRow += 1
        
        currDir += 90
        currDir %= 360

    return res
#print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
#print(spiral([[1,2],[3,4]]))

#Q2. Dictionary Inverter
def inverter(D):
    res = {}

    for k, v in D.items():
        if v in res:
            res[v].append(k)
        else:
            res[v]=[k]

    return res
# print(inverter({1:'a', 2:'b', 3:'c', 4:'c', 5:'b'}))
# print(inverter({1:'a', 2:'b', 3:'c'}))

#Q3. Matrix Multiplication
def matrixMultiply(A, B):
    nCol1, nRow1 = len(A[0]), len(A)
    nCol2, nRow2 = len(B[0]), len(B)

    res = []
    
    if nCol1 != nRow2:
        raise ArithmeticError
        errorString = "Dimensions of matrices are incompatible"
        return errorString
    
    for iterator in range(nRow1):
        currRow = []
        for iterator2 in range(nCol2):
            currRow.append(None)
        res.append(currRow)
        
    for iterator in range(nRow1):
        for iterator2 in range(nCol2):
            for iterator3 in range(nRow2):
                if not res[iterator][iterator2]:
                    res[iterator][iterator2] = 0
                res[iterator][iterator2] += A[iterator][iterator3] * B[iterator3][iterator2]
                
    return res
    
# print(matrixMultiply([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]]))
# print(matrixMultiply([[1,2],[4,5],[7,8]],[[1,2],[3,4],[5,6]]))

#Q4. Two Sum
def twoSum(L, t):
    cache = {}
    iterator = 0
    res = []
    
    while iterator < len(L):
        diffNum = t - L[iterator]
        
        if diffNum in cache:
          res.append((L[iterator], diffNum))
        
        cache[L[iterator]] = iterator
        
        iterator += 1
        
    return res    
    
# print(twoSum([1,2,2,3,4,5], 4)) 
# print(twoSum([1,2,3,4,5], 4))