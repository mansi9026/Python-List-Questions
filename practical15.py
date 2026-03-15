# programmed By: Mansi 
# Roll no. 42
#List Assignment no.15
# A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)
Days = [34, 36, 38, 33, 37, 35, 39]
hot_days=0
for i in Days:
    if i>35:
        hot_days=hot_days+1
        print("Hot Days")
    else:
        print("Normal Days")
