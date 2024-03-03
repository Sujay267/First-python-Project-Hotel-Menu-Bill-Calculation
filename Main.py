#loop control-While
#Restourant veg non veg food and bill
print("Hello sir/Madam ,\n  Welcome to 'Maharaja Restaurant'")
print("Which one food did you want ?(Veg or Non-Ved)\n Enter '1' for veg or '2' for non veg. ")
a=int(input(""))
while (a!=1) and (a!=2):
    print("Wrong choice , please Enter right choice.")
    print("e.g., If you want veg food then Enter 1")
    print("And If you want Non-veg food then Enter 2")
    a=input("")
bill=0
while (a==1) or (a==2):
    if (a==1):
        print("1.Paneer tikka  -  100rs")
        print("2.Palak Paneer  -  150rs")
        print("3.Paneer Kabab  -  200rs")
        print("4.Roti          -  20rs")
        print("Enter sr. no. of one of above food item")
        i_no=int(input(""))
        while (i_no>4) or (i_no<1):
            print("wrong choice ,\n  Enter valid choice between 1 to 4")
            i_no=int(input(""))
        while (4>=i_no>=1) :
            if (i_no)==1:
                print('Ok, your order will be provided to you soon.')
                bill=bill+100
            elif (i_no)==2:
                print('Ok, your order will be provided to you soon.')
                bill=bill+150
            elif (i_no)==3:
                print('Ok, your order will be provided to you soon.')
                bill=bill+200
            elif (i_no)==4:
                print('Ok, your order will be provided to you soon.')
                bill=bill+20
            print("Did you want some more veg food ?")
            b=input("")
            while (b!="yes") and (b!="no"):
                print("wrong choice ,\n  Please Enter yes or no")
                b=input("")
            if (b=="yes"):
                print("Enter sr. no. of one of above food item")
                i_no = int(input(""))
                while (i_no>4) or (i_no<1):
                    print("wrong choice ,\n  Enter valid choice between 1 to 4")
                    i_no=int(input(""))
            elif (b=="no"):
                print("Did you want some Non veg food ?")
                c=input("")
                while (c!="no") and (c!="yes"):
                    print("Wrong Choice ,\n Please Enter yes or no")
                    c=input("")
                if (c=="no"):
                    print("Your bill is ",bill,"rs.")
                    bill=bill*0
                    i_no=0
                    a=0
                    print("Thank you , for visiting our Restaurant")
                elif (c=="yes"):
                    i_no = 0
                    a=2
    elif(a==2):
        print("1.Better Chicken  - 100rs")
        print("2.Mutton Handi    -  150rs")
        print("3.Mutton Tali     -  200rs")
        print("4.Roti            -  20rs")
        print("Enter sr. no. of one of above food item")
        i_no=int(input(""))
        while (i_no>4) or (i_no<1):
            print("wrong choice ,\n  Enter valid choice between 1 to 4")
            i_no=int(input(""))
        while (4>=i_no>=1) :
            if (i_no)==1:
                print('Ok, your order will be provided to you soon.')
                bill=bill+100
            elif (i_no)==2:
                print('Ok, your order will be provided to you soon.')
                bill=bill+150
            elif (i_no)==3:
                print('Ok, your order will be provided to you soon.')
                bill=bill+200
            elif (i_no)==4:
                print('Ok, your order will be provided to you soon.')
                bill=bill+20
            print("Did you want some more non veg food ?")
            b=input("")
            while (b!="yes") and (b!="no"):
                print("wrong choice ,\n  Please Enter yes or no")
                b=input("")
            if (b=="yes"):
                print("Enter sr. no. of one of above food item")
                i_no = int(input(""))
                while (i_no>4) or (i_no<1):
                    print("wrong choice ,\n  Enter valid choice between 1 to 4")
                    i_no=int(input(""))
            elif (b=="no"):
                print("Did you want some more veg food ?")
                c=input("")
                while (c!="yes") and (c!="no"):
                    print("Wrong Choice ,\n please Enter valid choice.(yes or no)")
                    c=input("")
                if (c=="no"):
                    print("Your bill is ", bill,"rs.")
                    bill = bill * 0
                    i_no = 0
                    a = 0
                    print("Thank you , for visiting our Restaurant.")
                elif (c=="yes"):
                    i_no = 0
                    a = 1
