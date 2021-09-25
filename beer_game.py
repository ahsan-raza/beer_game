from beer_demand import *
from time import sleep

Inv=540
order_cost=100
total_cost_week=[None] * 21
flag_day=[None] * 21
cumm_cost=0
out_stock_cost=0



### Cosmetic Code#######

def banner(text, num):
    border = "%"
    line = border * 2*len(text)
    print('\n')
    print(line)
    print(line,'\n')
    print(text,num)
    print(line)
    print(line, "\n")

##main for loop that  will itrate for 20 weeks
for i in range(1,21,1):
    msg= "The remaining inventory is:"
    banner(msg,Inv) #printing the inventory for the retail manager to take the decision
    dmnd = get_demand(i)  #getting the demand by beer_demand function
    print("The demand for the inventory is:", dmnd)
    if Inv<0:
        total_cost_week[i] = 0
        total_cost_week[i] = dmnd
    elif (dmnd > Inv) and (Inv >0):
        out_stock_cost=dmnd-Inv
        total_cost_week[i]=0
        total_cost_week[i]=total_cost_week[i]+int(out_stock_cost)
    for j in range(1,21,1):
        #print("flag_day is:",flag_day[j])
        if flag_day[j] != None:
            print("im in flag_day loop")
            if (j is i) and (flag_day[j] !=None):
                print(i,j)
                Inv = Inv + flag_day[j]
                print("The supply is added to inventory, it was :", flag_day[j])
                flag_day=[None] * 21
    ordr=input("how many pallet you want to order? ")       # taking order from retail manager
    val = int(ordr)
    if val > 0:             #checking if the order is greater than 0 to add order cost in total_cost
        Inv = Inv - dmnd  # deleting the demand from Inventory
        #devicing a check to add the inv in the 3rd week

        flag_day[i+3]=val
        for k in range(len(flag_day)):
            print(flag_day[k])


        if inv <0:
            total_cost_week[i] = order_cost
        else:
            total_cost_week[i] = Inv+order_cost
        print("********the order value is greater than 0****")


        #print("\n\nThe total cost is: ",total_cost) #will delete this print,placed just for understanding

    elif val ==0:
        Inv = Inv - dmnd  # deleting the demand from Inventory
        if Inv >0:
            total_cost_week[i] =  Inv #if no order is placed than no order cost will be added
        print("********the order value is less than 0****")

    cumm_cost=cumm_cost+total_cost_week[i]
    print("\n\nThe weekly cost: ",total_cost_week[i])
    print("this is week: ",i)

    print("\n\nThe total cost is: ", cumm_cost)  # will delete this print,placed just for understanding
    print('\n\nStarting Next week in 3 . . .\n')
    sleep(1)
    print('2 . . . \n')
    sleep(1)
    print('1 . . . \n')
    sleep(1)
    print("\nThis is E.O.W...")










