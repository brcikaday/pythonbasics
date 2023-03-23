#userdetails = []
#userinput = input("enter a name:")
#userdetails.append(userinput)
#userinput = input("enter age")
#userdetails.append(userinput)
#userinput = input("enter class:")
#userdetails.append(userinput)
#userinput = input("enter gender:")
#userdetails.append(userinput)
#print(f"your name is {userdetails[0]}, your agejeo is {userdetails[1]}, your class {userdetails[2]},your gender is {userdetails[3]}")

userdetails = {}
userinput = input("enter a name:")
userdetails["name"]=userinput
userinput = input("enter age")
userdetails["age"] = userinput
userinput = input("enter class:")
userdetails["class"] = userinput
userinput = input("enter gender:")
userdetails["gender"] = userinput
print(userinput)
print (userdetails)