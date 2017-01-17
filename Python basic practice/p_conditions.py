# examples of python conditions

def main():
    x, y =10, 10

    if(x<y):
        st = "x is less than y"
    else:
        st = "x is greater than y"
    print st

    st = "x is less than y" if (x<y) else "x is greater or equal to y"
    print st

if __name__ == "__main__":
 main()



