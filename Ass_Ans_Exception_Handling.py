
#Exception_Handling

#Q1

try:
    a=int(input("Enter number 1 - "))
    b=int(input("Enter number 2 - "))
    print(a/b)
except Exception as e:
    print(e)
    
    
#Q2----------------------------------------------------------------------------

while(True):
    try:
        name=input("Name - ")
        surname=input("Surname - ")
        age=int(input("Age - "))
        height=float(input("Height - "))
        weight=float(input("Weight - "))
    except Exception as e:
        print(e)
    else:
        print("Thank you for your info")
        break
    

#Q3----------------------------------------------------------------------------

def printListEle(l,i):
    print(l[i])

l=[1,2,3,5,4,6,9,8]

try:
    printListEle(l,10)    
except:
    print("This index is out of the LIST")
    

#Q4----------------------------------------------------------------------------

d={1:[1,2,3,4],2:[2,4,6,8]}
print(d)

def addEleToDict(d,k,l):
    try:
        if k in d:
            print("This element already exists in the dict")
        else:
            d.update({k:l})
    except Exception as e:
        print(e)
    else:
        print("Done")
    finally:
        print("Finally block executed")
   
addEleToDict(d, 2, [3,6,9,12])   
print(d)      
#Q5----------------------------------------------------------------------------

class InvalidAgeException(Exception):
    def __init__(self,msg="Under age"):
        self.msg=msg
    def __str__(self):
        return "f{Self.msg}"
    
age=int(input("Age - "))

if age<18:
    raise InvalidAgeException()
else:
    print("Welcome")
    
    
#Q6----------------------------------------------------------------------------

l=[1,2,3,4,5,6,7,8,9]
print(l.index(7))

def searchList(l,e,i):
    if i>(len(l)):
        raise IndexError("Index out of bound")
    else:
        print("Element at index - ",l[i])

    if e not in l:
        raise Exception("Element not present")
    else:
        print("Element ",e," is present ")
  
searchList(l, 6,8)
    

    