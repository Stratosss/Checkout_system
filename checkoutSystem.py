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
    },
}

def fileFiltering (file):
    temp_dict = {file[i]['code']:file[i]['quantity'] for i in range(len(file))}
    item_list = ["A","B","C","D"]
    
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
    for key, value in order.items():
        item = pricebook[key]
        if isinstance(item["discount"], int):
            factor = value // item["quantity"]
            total += factor * item["discount"] + (value - factor * item["quantity"]) * item["price"]
        else:
            total += value * item["price"]
    return total
            
if __name__=="__main__":                   
    dict = fileFiltering(fileLines)
    total = calculator(dict)
    print("Total due: £",total)
    


