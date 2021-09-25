from beer_demand import *
Inv=540
order_cost=100
invnt_cost=0
total_cost_week=[None] * 20
cumm_cost=0
out_stock_cost=0
add_to_inv=0
add_aftr_weeks=0
def banner(text, num):
    border = "%"
    line = border * 2*len(text)
    print('\n')
    print(line)
    print(line,'\n')
    print(text,num)
    print(line)
    print(line, "\n")


for i in range(20):                                 #will itrate for 20 weeks
    msg= "The remaining inventory is:"
    banner(msg,Inv) #printing the inventory for the retail manager to take the decision
    dmnd = get_demand(i)  #getting the demand by beer_demand function
    print("The demand for the inventory is:", dmnd)
    if dmnd > Inv:
        out_stock_cost=dmnd-Inv
        total_cost_week[i]=total_cost_week[i]+out_stock_cost
    ordr=input("how many pallet you want to order? ")       # taking order from retail manager
    val = int(ordr)
    if val > 0: #checking if the order is greater than 0 to add order cost in total_cost
        Inv = Inv - dmnd  # deleting the demand from Inventory
        total_cost_week[i] = Inv+order_cost

        #print("\n\nThe total cost is: ",total_cost) #will delete this print,placed just for understanding

    elif val ==0:
        Inv = Inv - dmnd  # deleting the demand from Inventory
        total_cost_week[i] =  Inv #if no order is placed than no order cost will be added

    cumm_cost=cumm_cost+total_cost_week[i]
    print("\n\nThe weekly cost: ",total_cost_week[i])


    print("\n\nThe total cost is: ", cumm_cost)  # will delete this print,placed just for understanding











