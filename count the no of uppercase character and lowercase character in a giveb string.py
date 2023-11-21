upper_case=lower_case=0
def chk_str(str):
    global upper_case,lower_case
    value=str
    for i in value:
        if i==i.upper():
            upper_case+=1
        else:
            lower_case+=1
    print("given string :{}".format(value))
    print(f"total {lower_case=}")
    print(f"total {upper_case=}")
chk_str("raahiNNA")
