from beer_demand import *
Inv=540
out_stock_cost=100
invnt_cost=0
def banner(text, num):
    border = "%"
    line = border * 2*len(text)
    print('\n')
    print(line)
    print(line,'\n')
    print(text,num)
    print(line)
    print(line, "\n")


for i in range(20):
    msg= "The remaining inventory is:"
    banner(msg,Inv) #printing the inventory for the retail manager to take the decision
    dmnd = get_demand(i)
    print("The demand for the inventory is:", dmnd)
    ordr=input("how many pallet you want to order? ")
    if not ordr:
        invnt_cost = invnt_cost+Inv
    else:
        






