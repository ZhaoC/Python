#exmaples of python functions

def func1():
    print "I am a function"

func1()
print func1()
print func1

#a function returns value
def cube(x):
    print str(x)+ " with cube:"
    return x*x*x

print cube(3)

# a function with loop
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print power(2)
print power(2, 3)


# a function with vaiable number of arguments 
def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print multi_add(1,2,3)
