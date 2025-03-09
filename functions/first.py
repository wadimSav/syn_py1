def fact(num):
    res = 1
    
    while num > 1:
        res = res * num
        num = num - 1
    return res
    
fact_3 = fact(3)
fact_list = []

while fact_3 > 0:
    fact_list.append(fact(fact_3))
    fact_3 = fact_3 - 1
    
print(fact_list)