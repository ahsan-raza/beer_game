from beer_demand import *

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
with open("demand.txt", "w") as dem:
    for i in range(1, 21):  # contatore generico settimana
        print("Week #", i)
        for j in range(1, 21):  # contatore settimana ordine
            if flag_week[j] != 0:
                if (j is i) and (flag_week[j] != 0):  # Controllo sulla settimana. i è la generica settimana,
                    # j è la settimana in cui giunge l'ordine. Quando coincidono l'ordine viene inserito nell'inventario
                    Inv = Inv + flag_week[j]
                    print("The supply is added to inventory, it was :", flag_week[j])
                    flag_week = [0] * 24

        msg = "Inventory level:"
        banner(msg, Inv)  # printing the inventory for the retail manager to take the decision
        dmnd = get_demand(i)  # getting the demand by beer_demand function
        dem.write(str(dmnd) + '\n')
        print("The demand for the inventory is:", dmnd)

        if Inv <= 0:
            Inv = 0
            total_cost_week[i] = 0
            total_cost_week[i] = dmnd
        elif (dmnd > Inv) and (Inv > 0):
            out_stock_cost = dmnd - Inv
            total_cost_week[i] = 0
            total_cost_week[i] = total_cost_week[i] + int(out_stock_cost)

        ordr = input("How many pallets do you want to order? ")  # taking order from retail manager
        val = int(ordr)
        if val > 0:  # checking if the order is greater than 0 to add order cost in total_cost
            Inv = Inv - dmnd  # deleting the demand from Inventory
            # devicing a check to add the inv in the 3rd week

            flag_week[i + 2] = val

            if Inv < 0:
                total_cost_week[i] = order_cost + dmnd
                Inv = 0
            else:
                total_cost_week[i] = Inv + order_cost

            # print("\n\nThe total cost is: ",total_cost) #will delete this print,placed just for understanding

        elif val == 0:
            if Inv > 0:
                total_cost_week[i] = abs(Inv - dmnd)  # if no order is placed than no order cost will be added
                Inv = Inv - dmnd  # deleting the demand from Inventory
                if Inv < 0:
                    Inv = 0

        cumm_cost = cumm_cost + total_cost_week[i]
        print("\n\nThe weekly cost: ", total_cost_week[i])
        print("The remaining inventory is:", Inv)
        print("This is end of week: ", i)

        print("\n\nThe total cost is: ", cumm_cost)  # will delete this print,placed just for understanding

        print("_______________________________________\n\n")

from plotting_function import *