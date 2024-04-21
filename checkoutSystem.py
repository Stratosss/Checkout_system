import math
import json
import sys



file = open("newOrder.json")
fileLines = json.load(file) # Creates a list file containing the dictionaries

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
    for k,v in order.items():
        if k == 'A':
            if v == 3:
              total =  total + (v/3*140)
            elif v<3:
                total = total + (v*50)
            else:
                factor = math.floor(v/3)
                total = total + factor*140 + ((v-(factor*3))*50) #applies discount every three items they buy: e.g. 7 items: 2 discounts (2*3 items) + 1 item for full price
        elif k =='B':
            if v%2 == 0:
              total =  total + (v/2*60)
            elif v<2:
                total = total + (v*35)
            else:
                factor = math.floor(v/2)
                total = total + factor*60 + ((v-(factor*2))*35)
    return total
            
if __name__=="__main__":                   
    dict = fileFiltering(fileLines)
    sub_total = calculator(dict)
    print("Subtotal due: £",sub_total)
    


