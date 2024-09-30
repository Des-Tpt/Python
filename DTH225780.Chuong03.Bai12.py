for i in range(2, 10): 
    for j in range(1, 11): 
        line = "{} * {} = {}".format(i, j, i * j) 
        print(line, end='\t') 
    print()
