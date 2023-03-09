# creating a list
Names_of_student=["andrews","micheal","godfred"]
print(Names_of_student)
#printing an item in a list
second_student = Names_of_student[1]
print(second_student)
# adding an item to a list
Names_of_student.append("fred")
print(Names_of_student)
# how to push code to github 
# git add . , git commit -m "", git push

#creating a dictionary
joels_info = {
            "name": "joel",
              "age": 13,
              "hobbies": {
                "outdoor": ["running","ampe"],
                "indoor": ["ludo","teletabies"]
                }
}
print(joels_info)

#selecting item in a dictionary
hobbies=joels_info["hobbies"]
print(hobbies)
outdoor=hobbies["outdoor"]
print(outdoor)

# asking for an input
age=input("what is your age?\n")
print(age)


students_grade={}
#adding to a dictionary
students_grade["mike"]="A"
print (students_grade)
students_grade["prince"]="B"
students_grade["andy"]="C"
students_grade["alex"]="D"
print(students_grade)
students_grade.pop("alex")
print(students_grade)