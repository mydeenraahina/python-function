leng=0
def str_len(str):
    global leng
    for i in str:
        leng=leng+1
    return "{}".format(leng)
print(str_len("raahina"))
