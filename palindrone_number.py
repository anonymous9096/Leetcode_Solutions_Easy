def Palindrone(x):
    if -2147483648 < x < 2147483648:
        x = list(str(x))
        rev_x = []
        for i in range(len(x)):
            rev_x.append(x[-(i+1)])
        print(x)
        print(rev_x)
        if (rev_x == x):
            print('true')
        else:
            print('false')
    else:
        exit()


if __name__=="__main__":
    x = -121
    Palindrone(x)