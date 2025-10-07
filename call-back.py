#Das ist ein call-back Beispiel. Kunde gibt im Restaurant eine Bestellung auf und der Service bringt das Essen.
#it is a callBack example. customer in a restaurant put an order and the waiter delivers the order when it is ready
#--
#PS Code
#Beachte arr_length Reihe 16
#def food_exists = 0
#// i ist Array Indes
#   FOR i IST 0 BIS i <= arr_length i PLUS 1                (i PLUS 1 = i++)
#       IF food_name == arr_foods[i]
#           food_exists=1
#       END IF
#RETURN food_exist
##--

def checkExistence(food_name:str)->bool:
    arr_foods=["Pasta", "Pizza", "Döner"]
    if food_name in arr_foods:
        return True
    else:
        return False  
        

def bestellung(food_name:str, checkExistence):
    is_food_exists = checkExistence(food_name)
    if is_food_exists == True:
        print(f"Dein(e) {food_name} ist gleich fertig!")
    else:
        print(f"Unglücklicherweise haben wir {food_name} nicht auf der Karte.")

#-- actual program use upper defined methods --#
order_string = input ("Was möchten sie bestellen?")
bestellung(order_string, checkExistence)


