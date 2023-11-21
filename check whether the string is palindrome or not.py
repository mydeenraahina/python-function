def str_palindrom_chk(value):
    length=len(value)
    (print(f"{value} is palindrom") if value==value[length::-1] else print(f"{value}is not a palindrome"))
getting_str=input("> ")
str_palindrom_chk(getting_str)
