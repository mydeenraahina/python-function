def year(year):
    if year%4==0:
        return "{} is a  leap year".format(year)
    else:
        return "{} is not a leap year".format(year)
print("checking whether the year is leap or not")
try:
    getting_input=int(input("Enter a year "))
    print(year(getting_input))
except ValueError:
    print("It is  not a valid input")
