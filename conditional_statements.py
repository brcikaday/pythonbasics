age=int(input("enter age")) 
if age >= 18:
   print("you can drive")
else:
    print("you cannot drive")  
    
age=int(input("enter age")) 
if age >= 18 and age <= 80:
   print("you can drive")
else:
    print("you cannot drive")   

#Nesting 
age=int(input("enter age")) 
if age <= 0:
   print("invalid")
elif age >= 18 and age <= 80:
    print("you can drive")
else:
   print("you cannot drive") 

size = input("L for large M for medium S for small;")
add_pepperoni = input("yes or no;")
extra_cheese= input("yes or no;")
if size == "L" and add_pepperoni=="yes" and extra_cheese== "yes":
    amount= 120 + 10 + 5
    print(amount)
elif size== "M" and add_pepperoni=="yes" and extra_cheese=="yes":
    amount=85 + 10 + 5
    print(amount)
elif size == "S" and add_pepperoni =="yes" and extra_cheese=="yes":
    amount= 50 + 10 + 5
    print(amount)

# alternative
bill=0

size = input("what size do you want")
add_pepperoni=input("do want pepperoni")
extra_cheese= input("do you want cheese")

if size == "L":
    bill += 100
elif size =="M":
    bill += 85
else:
    bill += 50

if add_pepperoni == "yes":
    bill += 10

if extra_cheese =="yes":
    bill += 5

print(f"the total bill is {bill}")