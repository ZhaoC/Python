# Python variable example

#declare a variable and initialize it

f = 0;
print f

f = "abc";
print f

#use function str()
print "string type" + str(200)

#define global varible
def someFunction():
    global f
    f = "def"
    print f

someFunction()
print f

#delete var f
del f
print f