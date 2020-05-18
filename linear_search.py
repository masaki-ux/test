def ss(number_list,n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0,100)
s1 = ss(numbers,37)
print(s1)
s2 = ss(numbers,208)
print(s2)
