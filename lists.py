
fruits = ["Durian", "Papaya", "Mango","Pineapple","Watermelon"]
print(fruits)
fruits.append("Orange")
print(fruits)

fruits.remove("Pineapple")
print(fruits)

print(len(fruits))

print(fruits[0])
fruits[3] = "Grapes"
print(fruits)

print(fruits[:3])
print(fruits[2:4])

for fruit in fruits:
    print(fruit)