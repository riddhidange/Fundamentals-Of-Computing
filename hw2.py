#Q1.
def length(x):
    '''
    Function to find length of an iterable such as string or a list which returns an integer value.
    Precondition1: Input should be string or a list.
    '''
    count = 0
    for item in x:
        count += 1

    return count

def dot(L, K):
    '''
    Function to return dot product of two lists using recursion. This function returns the dot product of two vectors/lists as the sum of products of element in same position of the vectors/lists as a numeric value.
    Precondition 1: Input should be either a list or a vector of numeric values.
    '''
    if L == [] or K == []:
        return 0
    
    if length(K) != length(L):
        return float("-inf")
    
    return L[0] * K[0] + dot(L[1:], K[1:])

#Q2.
def explode(S):
    '''
    Function to return a list of all the characters in the string. This function takes a string as an input and returns a list of characters of the string.
    Precondition 1: The input must be string of characters.
    '''
    if not S:
        return []

    return [S[0]] + explode(S[1:])
        
#Q3.
def length(x):
    '''
    Function to find length of an iterable such as string or a list which returns an integer value.
    Precondition1: Input should be string or a list.
    '''
    count = 0
    for item in x:
        count += 1

    return count

def runningAverage(L):
    '''
    Function to find running average which takes list of numeric values as an input and returns new list of numeric values where at each index n is the running average upto n in original list.
    Precondition1: Input should be a list of numeric values.
    '''
    runAvg = []
    runSum = 0
    for i in range(length(L)):
        runSum += L[i]
        runAvg += [runSum / (i+1)]
    return runAvg

#Q4.
# def double (n):
#     return 2 * n
    
# def isEven(n):
#     return  n % 2==0
    
def customMap(f,L):
    '''
    Function to replicate a behaviour of map. This function takes a function f and a list L as inputs and returns the output list according to the function.
    Precondition 1: parameter f is a function
    Precondition 2: parameter L is a list
    '''
    MappedList = []
    for i in L:
        MappedList += [f(i)]
        
    return MappedList

def customFilter(f,L):
    '''
    Function to replicate a behaviour of map. This function takes a function f and a list L as inputs and returns the output list according to the function.
    Precondition 1: parameter f is a function
    Precondition 2: parameter L is a list
    '''
    FilteredList=[]
    for i in L:
        if f(i):
            FilteredList += [i]
            
    return FilteredList
