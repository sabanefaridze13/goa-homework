def str_int(string2, number):
   for i in range(number+1):
      return string2
str_int("Goa",10)

def stringlen(string):
   if len(string) > 10:
      return string
   return "too short"

#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number1):
   if number1 % 2 == 0:
      return "even"
   return "odd"