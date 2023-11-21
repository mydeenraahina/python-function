def rev_str(str_value):
    leng=len(str_value)
    reversed_string=str_value[leng::-1]
    return f"{reversed_string=}"
print(rev_str(input(">")))
