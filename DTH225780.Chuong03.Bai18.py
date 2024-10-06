n=4
n2=7

def ve_hinh_1_2(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ", end=" ")

        for j in range(n - i + 1):
            print(" ", end=" ")
        for k in range(i + 1):
            print("*", end=" ")
        print()

def ve_hinh_3(n2):
    for i in range(n2):
        if i == n2 // 2:
            print("* "*n2)
        else:
            if i < n2 // 2 and i != 0:
                print("* " + "  " * (i-1) + "*")
            elif i > n2 // 2 and i != n2 - 1:
                print(" " * i*2 + "*" + "  " * (n2 - (i+2)) + " *")
            else:
                print(" " * i*2 + "*")
                
ve_hinh_1_2(n)
print()
ve_hinh_3(n2)



        