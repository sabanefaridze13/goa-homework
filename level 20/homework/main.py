


# 1)მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ ამ რიცხვის თითოეული ციფრი / მაგ: (შემოიტანა 25156, დაბეჭდეთ ცალკე 2 ცალკე 4 ცცალკე 1 ცალკე 5 ცალკე 6) for ციკლის გამოყენებით
num = input("Enter your number: ")

for i in num:
    print(i)

# 2)მომხმარებელს შემოატანინეთ რაღაც რიცხვი და შემდეგ შეამოწმეთ თუ ეს რიცხვი არის ლუწი, დაბეჭდეთ "even", ხოლო თუ კენტია "odd"
num = int(input("Enter your number: "))

if num % 2 == 0:
    print("Even!")
else:
    print("Odd!")

# 3)ცვლადში შეინახეთ თქვენი სახელი, მომხმარებელს შემოატანინეთ მისი სახელი და თუ თქვენი სახელები ემთხვევა დაუპრინტეთ "Hello" სხვა შემთხვევაში "Bye"
my_name = "saba"
user_name = input("Enter your name: ")

if my_name == user_name:
    print("Hello!")
else:
    print("Bye!")

# 4)მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ, თუ რიცხვი მეტია 90-ზე, დაბეჭდეთ "A", თუ რიცხვი ნაკლებია 90-ზე და მეტია 70-ზე, დაბეჭდეთ "B", თუ რიცხვი ნაკლებია 70-ზე და მეტია 50-ზე, დაბეჭდეთ "C", სხვა შემთხვევაში დაბეჭდეთ "D"
score = int(input("Enter your number: "))

if score >= 90:
    print("A")
elif score < 90 and score > 70:
    print("B")
elif score < 70 and score > 50:
    print("C")
else:
    print("D")

# 5)while ციკლის მეშვეობით, შექმენით რიცხვების დიაპაზონი 1-დან 100 ჩათვლით, შეამოწმეთ თუ რიცხვი არის ლუწი, დაბეჭდეთ ეს რიცხვი while ციკლში და მიუწერეთ რომ ლუწია, თუ კენტია, დაბეჭდეთ ეს რიცხვი და გვერძე მიუწერეთ რომ კენტია / მაგ: (1 კენტიტა, 2 ლუწია, 3 კენტია, 4 ლუწია...)
i = 1

while i <= 100:
    if i % 2 == 0:
        print(i, "is Even!")
    else:
        print(i, "is Odd!")
    i = i + 1















