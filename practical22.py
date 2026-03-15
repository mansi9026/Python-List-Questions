# programmed By: Mansi 
# Roll no. 42
#List Assignment no.22
"""Marks of students are stored in a list.
marks = [78, 35, 90, 40, 55]
Write a program to:
Print PASS if marks ≥ 40
Print FAIL if marks < 40
Count how many students passed"""
marks = [78, 35, 90, 40, 55]
Count=0
for i in marks:
            if i >=40:
                print("Pass",i)
                Count+=1
            else:
                    print("Fail",i)

print(Count) 
