def num_chk(num):
    (print(f"{num} is a positive integer") if num>0 else(print(f"{num} is a negative integer") if num<0 else print(f"{num} is a Zero")))
try:
    num_chk((int(input(">"))))
except ValueError:
    print("only numbers are allowed")
 
