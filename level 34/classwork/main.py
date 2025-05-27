def multiply(n1,n2):
    if not isinstance(n1,int) or not isinstance(n2,int):
        print(0)
    print(n1 * n2)
multiply(5,5)

def greet():
  return "hello world!"

def greeter(name):
   return f"hello {name}"

john=greeter("john")
print(john)
saba = greeter("saba")
print(saba)

def iterate(num):
   if not isinstance(num, int):
      num = 10
   return list(range(num))
iterate(20)

def stringlen(string):
   if len(string) > 10:
      return string
   return "too short"