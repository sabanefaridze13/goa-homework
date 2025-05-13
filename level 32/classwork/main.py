a=5
b=a+1
c=a+2
total= sum({a,b,c})
if total % 3==0:
    print ("ჯამი იყოფა 3-ზე")
else:
    print ("ჯამი არ იყოფა 3-ზე")


def subtract(a,b):
   return a-b
result=subtract (a,b)
print ("შედეგი არის:, result")



def multifly(a,b):
   return a*b
result=multifly (7,6)
print ("ნამრავლი არის:", result)


def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
