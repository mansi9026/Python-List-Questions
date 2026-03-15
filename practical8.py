# programmed By: Mansi 
# Roll no. 42
#List Assignment no.8
#Given a list of numbers 1-20, create a new list that contains only the even numbers.
List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
newlist=[]
for i in List:
    if i%2==0:
        newlist.append(i)
print(newlist)