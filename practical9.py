# programmed By: Mansi 
# Roll no. 42
#List Assignment no.9
#Write a program that takes a list of names and a "search_name" from the user. Print the index where the name is found, or "Not Found."
name=["Mansi","Khushi","Shaivi","Kashish","Sakshi"]
ask=input("Enter a name")
if ask in name:
  print("Found:",name.index(ask))
else:
    print("Not Found")

