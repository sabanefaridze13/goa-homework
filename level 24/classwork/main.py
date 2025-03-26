
number = int(input("შეიყვანეთ მთელი რიცხვი: "))

if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")


correct_password = "mypassword"  
user_password = input("შეიყვანეთ პაროლი: ")

while user_password != correct_password:
    print("incorrect password")
    user_password = input("შეიყვანეთ პაროლი: ")

print("correct password")