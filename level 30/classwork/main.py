

# len-(სიგრძე)
# append-სიის ბოლოში ამატებს ელემენტს
# insert-სიაში კონკრეტულ ინდექსზე ამატებს ელემენტს
# poop-სიიდან შლის კონკრეტულ ელემენტს


things=[1,3,True,7,"hello"]
name=input("Whats your name")
things.append(name)
print(len(things)) 
print(things)

fruits = ["Melon", "Orange", "Banana", "Watermelon", "Kiwi"]
fruits.pop(4)
fruits.insert(3,"Pomegranate")
print(fruits)