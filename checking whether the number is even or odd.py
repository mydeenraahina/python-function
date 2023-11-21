def chk_even_odd(value):
    (print(f"It is a even number") if value%2==0 else print(f" It is a odd number"))
try:
    chk_even_odd((int(input(">"))))
except ValueError:
    print("Only Intergers are allowed")
