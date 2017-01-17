# python loops

def main():
    x = 0
    #define a while loop
    while (x<5):
        print x
        x = x + 1

    for x in range(2, 10):
        #if x == 3: break
        if (x %2 == 0):  continue
        print x

    # loop a collection
    days = ["Monday", "Thuesdy", "Wendsday"]
    for d in days:
        print d

    # using enumerate function to get index in collection
    months = ["Jan", "Feb", "Mar", "Apr"]
    for i, d in enumerate(months):
        print i+1, d

if __name__ == "__main__":
     main()