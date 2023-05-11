# Q.1) create one variablr containing following type of data

#string
str="shekhar zade"
print(str)

#list
l=[2,4,23,252,"shekhar",45.23,5+6j]
print(l)

#float
a=45.23
print(a)

#tuple
t=(42,"shekhar",2.3)
print(t)


# Q.2) given are following variables containing data

var1=''
print(type(var1))  #this is string data type

var2='[DS,ML,Python]'
print(type(var2))  #this is string data type

var3=['DS','ML','Python']
print(type(var3))  #this is list data type

var4=1
print(type(var4))  #this is int data type

# Q.3) explain the use of the following operators using an example

# / This operator is used for division
# % This operator is used to find remainder
''' // this operator is used for find int value only
in division it omits float value'''
''' ** this operator is used for find exponent (raise to the power)
eg. 5**6 = 5*5*5*5*5*5'''


'''Q.4) Create a list of length 10 of your choice containing multiple
types od data. using for loop print the element and its data type.'''

l=[12,45,236,12.54,4.6,"shekhar","zade",56,5+6j,"rahul"]

for i in l:
    print(i)
    print(type(i))


'''Q.5) using a while loop, verify if the number A is purely divisible
by number B and if so then how many times it can be divisible.'''

A=120
B=5
i=0
while A%B==0:
    print(A,"is divisible by",B)
    A=A//B
    i=i+1
    print("This number is",A,"times divisible")


'''Q.6) Create a list containing 25 int type data using for loop
and if-else condition print if the element is divisible by 3 or not'''

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

for i in l:
    if i%3==0:
        print(i,"is divible by 3")
    else:
        print(i,"is not divisible by 3")

'''Q.7) What do you understand about mutable and
immutable data types? Give examples for both showing this property.'''

'''Answer : we can change in mutable data type on its perticular index
but in immutable data type we can not change.'''

# Example string is immutable
str= "shekhar"
print(str[1])
print(str[2])
#but
#str[1]="d" #string object does not support item assignment


# list is mutable
l=[1,"shekhar",45]
print(l[1])

l[1]="Rahul"
print(l)  #we can assign item on a perticular index in list



