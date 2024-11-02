def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.writelines("\n")

def DocFile(path):
    arrSo = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip() 
            arr = data.split(',')
            arrSo.append(arr)
    return arrSo
