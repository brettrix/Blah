import pandas as pd

#______________________________________________________

#student_info = {
#    "name" : "Zendaya",
#    "year" : "Freshman",
#    "age" : 30,
#    "graduated" : False,
#    "fav_class" : "Accounting 310"
#}

#df = pd.DataFrame([student_info])

#print(df)

#______________________________________________________

#words = [["Jam", "Bread"], ["Butter", "Robert"], ["Larping", "Inquisitive"]]

#result = pd.DataFrame(words)

#print(result)

#______________________________________________________

student_info_2 = {
    "name" : ["Tom", "LeBron", "George", "LaFawnda"],
    "gpa" : [2.7, 4.0, 1.1, 3.5]
}

result2 = pd.DataFrame(student_info_2)

print(result2)

