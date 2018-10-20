# runnian
year = eval( input("input year: ") )
if year % 4 == 0 and year % 100 != 0:
    print("February has 29 days")
elif year % 4 ==0 and (year % 400 ==0 or year % 500 ==0):
    print("February has 29 days")
else:
    print("February has 28 days")
