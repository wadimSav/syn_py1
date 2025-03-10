my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
length = 0

def pd(l):
    global length
    if length == len(l):
        print("Конец списка")
        return
        
    print(l[length])
    length += 1
    pd(l)
    
pd(my_list)