#Question1


def cToF(t):
    return t*float(9/5) + 32
#print (cToF(25))

def fToC(t):
    return (t-32)* float(5/9)
#print (fToC(100))

#Question 2(a)

def shortStrings(L,n):
    def Long(x):
        a= len(x)<n
        return a
    return list(filter(Long,L))
#print (shortStrings(['a','b','abcde','abcdef'],5))

#Question2(b)

def doubleStrings(L):
    def doubled(l):
        return 2*l
    return list(map(doubled,L))
#print (doubleStrings(['a','b','cc']))

#Question 3 

def pigLatin(s):
    s=list(s)
    x= list(s[0])
    s2= list(s[1:])
    final= s2 + x + ['a'] + ['y']
    return final
#print(pigLatin('hello'))

#Question 4
def stringBalance(s):
    strList=list(s)
    SumofOrd= sum(map(ord,strList))
    middlePoint= (ord("m") + ord("n"))/2
    final= SumofOrd -(len(strList)*middlePoint)
    return final
#print(stringBalance('vvvvv'))

