
#FUNCTION_2_ASS

#Q1

def overlapping(l1,l2):
    for i in l1:
       if i in l2:
           return True
           break
    else:
        return False
   
l1=[1,2,3,4,5,6]
l2=[6,7,8,9,10,11]

print(overlapping(l1, l2))


#Q2----------------------------------------------------------------------------

def longestWord(l):
    max=0
    for i in range(0,len(l)):
        if (len(l[i])>max):
            max=len(l[i])
    return max

l=["hi","Hello","God","World!"]

print(longestWord(l))


#Q3----------------------------------------------------------------------------

def longestWord(l,n):
    lst=[]
    for i in range(0,len(l)):
        if (len(l[i])>n):
            lst.append(l[i])
    return lst

l=["hi","Hello","God","World!"]

print(longestWord(l,2))


#Q4----------------------------------------------------------------------------

def spellingCorrection(s):
    s=s.replace('  ',' ')
    str=""
    for i in s:
        if (i=='.'):
            i=' '
            str+=i
        else:
            str=str+i
            
    return str

s="Where.are  you looking.at!"

print(spellingCorrection(s))

