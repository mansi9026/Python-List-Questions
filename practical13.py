# programmed By: Mansi 
# Roll no. 42
#List Assignment no.13
#Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
age=[20,8,30,28,5,45,76,19,18,17,19]
minor=[]
adults=[]
for i in age:
    if i < 18:
       minor.append(i)
       
    else:
      adults.append(i)
     
print("minor",minor)
print("adults",adults)    