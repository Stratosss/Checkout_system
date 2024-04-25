import math
import json
import sys



file = open("newOrder.json")
fileLines = json.load(file) # Creates a list file containing the dictionaries

pricebook = {
    "A" : {
        "discount" : 140,
        "quantity" : 3,
        "price" : 50
    },
    "B" : {
        "discount" : 60,
        "quantity" : 2,
        "price" : 35
    },
    "C" : {
        "discount" : "none",
        "quantity" : "none",
        "price" : 25
    },
    "D" : {
        "discount" : "none",
        "quantity" : "none",
        "price" : 12
    }
}
def fileFiltering (file):
    temp_dict = {file[i]['code']:file[i]['quantity'] for i in range(len(file))} #creates a dictionary out of the list of dictionaries
    item_list = ["A","B","C","D"]    #item list for reference
    
    for k,v in temp_dict.items():
        if k not in item_list:
            print(f"Item code: {k}, not recognised.")
            sys.exit()
        elif not isinstance(v,int):
            print("Quantity cannot be string character or decimal.")
            sys.exit()
        elif v < 0 :
            print("Quantity cannot be below zero.")
            sys.exit()
    return temp_dict

def calculator(order):
    total = 0
    for key,value in order.items():
            for k,v in pricebook.items():
                if key == k:
                    if isinstance(pricebook[k]["discount"], int):    #checks if the item has a discount price
                        if value % pricebook[k]["quantity"] == 0:
                            total =  total +  ((value/pricebook[k]["quantity"]) * pricebook[k]["discount"])
                        elif value < pricebook[k]["quantity"]:
                            total = total + (value * pricebook[k]["price"])
                        else:
                            factor = math.floor(value/pricebook[k]["quantity"])
                            total = total + factor*pricebook[k]["discount"] + ((value-(factor*pricebook[k]["quantity"]))*pricebook[k]["price"])
                    else:
                        total= total + value * pricebook[k]["price"]
    return total
            
if __name__=="__main__":                   
    dict = fileFiltering(fileLines)
    total = calculator(dict)
    print("Total amount due: £",total)
    


