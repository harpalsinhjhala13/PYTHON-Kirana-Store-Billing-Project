from datetime import date, datetime


name = input("Enter your Name:\t")

#List of avilable Items
available = '''
kurkure       Rs 10
Noodles       Rs 25
Maggi         Rs 45
Lays          Rs 10
Pepsi         Rs 40
Fanta         Rs 40
CocaCola      Rs 40
borunvita     Rs 100
Vimbar        Rs 25
munch         Rs 10
DairyMilk     Rs 25
MilkyBar      Rs 20
Milk (1/ltr)  Rs 45
Lassi         Rs 20
Butter        Rs 25
Cheese        Rs 35
rice(1/kg)    Rs 20
wheat(1/kg)   Rs 45
\n '''


#Declaration
cost = 0
pricelist=[]
totalcost =0
Finalfinalprice=0
ITEMlist =[]
quantitylist=[]
costlist=[]


#Rates of Items
rates = {'kurkure':10,'noodles':25,'maggi': 45,
'lays' : 10,'pepsi': 40,'fanta': 40,
'cocacola': 40,'bournvita':100,'vimbar':25,
'munch':10,'dairymilk':25,'milkybar' : 20,
'milk':45,'lassi':20,'butter':25,
'cheese':35,'rice': 20,'wheat':45,}

#program to print AVAILABLE ITEMS IN MENU
option = int(input("for list of available Items, Press 1:\t"))
if option == 1:
    print(available)


#program to process the entered ITEMS, QUANTITY, PRICE, COST
for i in range(len(rates)):
    prod1 = int(input("To continue BUYING press 1 OR To checkout press 0:\t"))
    if prod1 == 0:
        break
    if prod1 == 1:
        ITEM=input("Enter your choosen product:\t")
        quantity=int(input("Enter yout quantity:\t"))        
        if ITEM in rates.keys():
                cost =quantity*(rates[ITEM]) 
                pricelist.append((available,quantity,rates,cost))
                totalcost += cost
                ITEMlist.append(ITEM)
                quantitylist.append(quantity)
                costlist.append(cost)
                GST = (totalcost*5)/100
                finalamount = GST + totalcost
        else:
            print("Sorry your entered PRODUCT is not available")
    else:
        print("YOU ENTERED WRONG INPUT!!, Press 1 for buy or Press 0 to exit")    

    val =input("To checkout type 'yes' OR to continue shopping press 'no':-\t")
    if val == 'yes':
        pass
        if finalamount != 0:
            print("\n")
            print(25*"=","HARPAL'S GROCERY APP", 25*"=")
            print(28*"=","Happy Shopping", 28*"=")

            print("\n")
            print(75*"-")
            print("CustomerName:",name,25*" ","Date:",datetime.now())
            print(75*"-")
            print("No.",8*" ","ITEMS",8*" ","QUANTITY",3*" ","PRICE")
            for i in range(len(pricelist)):
                print(i,10*" ",ITEMlist[i],12*" ",quantitylist[i],8*" ",costlist[i])
                print(80*"-")
                
            print(50*" ",'TotalAmount:',"\tRs",totalcost)
            print(50*" ","GST Amount:",5*" ","\tRs",GST)
            print(80*"-")
            print("Final Amount = ",finalamount)
            print(80*"-")
            print(25*"=","Thanks for shopping",28*"=")
            print(80*"-")
               
 




