# programmed By: Mansi 
# Roll no. 42
#List Assignment no.2
#Question: 
"""A cricket player scored runs in 6 matches.
Example: [45, 60, 10, 80, 55, 90]

Write a program to:

Find total runs

Find highest score

Count how many matches player scored more than 50 runs"""

Matches=[45,60,10,80,55,90]
count=0
total=sum(Matches)
highest=max(Matches)
for i in Matches:
    if i>50:
       count+=1
print(total)
print(highest)
print(count)