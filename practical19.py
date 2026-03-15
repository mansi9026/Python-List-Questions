# programmed By: Mansi 
# Roll no. 42
#List Assignment no.19
# A teacher stored attendance of students in a list (1 = present, 0 = absent).
#Example: [1,1,0,1,0,1,1]
#Write a program to:
#Count total present
#Count total absent
#Print attendance percentage
Attendence=[1,1,0,1,0,1,1]
total=sum(Attendence)
Percentage=(total/len(Attendence))*100
present=Attendence.count(1)
Absent=Attendence.count(0)
print(present)
print(Absent)   
print(Percentage)
