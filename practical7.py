# programmed By: Mansi 
# Roll no. 42
#List Assignment no.7
#Ask a user for a fruit name. Check if it exists in your fruit_basket list using the in keyword.
Basket=["Apple","Mango","Banana","Pine-Apple","Guava"]
fruit=input("Enter a fruit name")
if fruit in Basket:
    print("This fruit",fruit," in basket")
else:
    print("This fruit",fruit," in not a basket")