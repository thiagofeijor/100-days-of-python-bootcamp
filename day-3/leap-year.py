year = int(input("Type some year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  print("It is a leap year")
else:
  print("It isn't a leap year")

