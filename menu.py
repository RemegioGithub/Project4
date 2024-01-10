

def menu(line,no,product,price):
    print(line," ", no, " ",product, " ",price)



        
      
print("\n                        M  E  N  U\n")
print("       -------------------------------------------")
print("           No.           Product           Price")
print("       -------------------------------------------")

menu("        ",1,"         CornedBeef       ", 50.00)
menu("        ",2,"          Meatloaf        ", 40.00)
menu("        ",3,"         Spaghetti        ", 75.00)
menu("        ",4,"          Hamburger       ", 70.00)
print("        ___________________________________________\n")


while True:
    select = int(input("\n                    Select index number :"))
    
    if select == 1:
        print("\n        CORNEDBEEF")
        print("           50.00")
        print("        -------------")
        
        qty = int(input("\n        Quantity  :"))
        print("        Total     :",qty * 50,".00")
        
    elif select == 2:
        print("\n        MEATLOAF")
        print("           40.00")
        print("        -------------")
        
        qty = int(input("\n        Quantity  :"))
        print("        Total     :",qty * 40,".00")

 
    elif select ==3:
        print("\n        SPAGHETTI")
        print("           75.00")
        print("        -------------")
        
        qty = int(input("\n        Quantity  :"))
        print("        Total     :",qty * 75,".00")
        
    elif select == 4:
        print("\n        HAMBURGER")
        print("           70.00")
        print("        -------------")
        
        qty = int(input("\n        Quantity  :"))
        print("        Total     :",qty * 70,".00")
        
    else:
       print("Sorry !!!")
       
       