def distinct_list(values):
    val=values
    list_value=[]
    for i in val:
        if i not in list_value:
            list_value.append(i)
        else:
            continue
    print(f"Given list {val} ")
    print(f"distinct elements i the list {list_value}")
distinct_list([1,8,0,1,0,9,6,8])
