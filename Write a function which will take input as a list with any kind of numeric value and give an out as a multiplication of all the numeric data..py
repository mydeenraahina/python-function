mul=1
list_elements=[1,2,3,4,5]
def mul_list(n):
    list_value=n
    global mul
    for i in list_value:
        mul*=i
    return "{}".format(mul)
print(mul_list(list_elements))
