from beer_demand import *
import csv

#Variables initialization
Inv = 540
order_cost = 100
total_cost_week = [0] * 21
flag_week = [0] * 24
cumm_cost = 0
out_stock_cost = 0


### Cosmetic Code#######

def banner(text, num):
    border = "%"
    line = border * len(text)
    print('\n')
    print(line, '\n')
    print(text, num, '\n')
    print(line, "\n")

## main for loop that  will itrate for 20 weeks

file = open('stats.csv', 'w', newline='') #creating and writing the csv file
# The CSV file gets generated only after week 20 is reached
with file:
    # identifying header
    header = ['Week #', 'Demand', 'Inv level', 'Cost at E.o.W']
    writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
    writer.writeheader()

    for i in range(1, 21):  # generic week counter
        print("Week #", i)
        for j in range(1, 21):  # order week counter
            if flag_week[j] != 0: # Check if there is a pending order that needs to be added in inventory
                if (j is i) and (flag_week[j] != 0):  # Check if there is an order that has been placed already
                    # j is the traversing variable. When i = j the order gets added to the inventory
                    Inv = Inv + flag_week[j]  # orderd gets added to the inventory
                    print("The supply is added to inventory, it was :", flag_week[j])
                    flag_week = [0] * 24 #re-initializing the flag_week as empty

        msg = "Inventory level:"
        banner(msg, Inv)  # printing the inventory for the retail manager to take the decision
        dmnd = get_demand(i)  # getting the demand by beer_demand function

        print("The demand for the inventory is:", dmnd)




        if Inv <= 0: #checking if inventory is negative
            Inv = 0 # Initializing the inventory to zero
            total_cost_week[i] = 0
            total_cost_week[i] = dmnd #If the inventory is zero then the cost will be the demand cost
        elif (dmnd > Inv) and (Inv > 0):
            out_stock_cost = dmnd - Inv #calculating the out of stock cost
            total_cost_week[i] = 0
            total_cost_week[i] = total_cost_week[i] + int(out_stock_cost)

        ordr = input("How many pallets do you want to order? ")  # taking the order from command line
        val = int(ordr)
        if val > 0:  # checking if the order is greater than 0 to add order cost in total_cost
            Inv = Inv - dmnd  # deleting the demand from Inventory

            # If the user orders something we are setting the flag to add the order after two weeks
            flag_week[i + 2] = val

            # If the user orders something we add the order cost
            if Inv < 0:
                total_cost_week[i] = order_cost + dmnd
                Inv = 0
            else:
                total_cost_week[i] = Inv + order_cost


        #Check if the user has not ordered anything
        elif val == 0:
            if Inv > 0:
                total_cost_week[i] = abs(Inv - dmnd)  # if no order is placed than no order cost will be added
                Inv = Inv - dmnd  # deleting the demand from Inventory
                if Inv < 0:
                    Inv = 0

        cumm_cost = cumm_cost + total_cost_week[i]  #cumulative cost
        print("\n\nThe weekly cost: ", total_cost_week[i])
        print("The remaining inventory is:", Inv)
        print("This is end of week: ", i)

        print("\n\nThe total cost is: ", cumm_cost)  # will delete this print,placed just for understanding

        print("_______________________________________\n\n")

        #writing in the csv file
        writer.writerow({'Week #': i,
                         'Demand': str(dmnd),
                         'Inv level': str(Inv),
                         'Cost at E.o.W': total_cost_week[i]})

#This line automatically opens the plot of the demand when week 20 is reached
from plotting_function import *

