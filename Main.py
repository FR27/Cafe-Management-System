from tkinter import*
import random
import time;
import datetime
import tkinter.messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management Systems")
root.configure(background = 'Thistle' )

Tops = Frame(root, bg = 'Thistle', bd =15, pady=5,relief=RIDGE)
Tops.pack(side= TOP)
lblTitle = Label(Tops, font = ('arial',60,'bold','italic'),
            text = "Restaurant Management Systems", bd=21,bg='Thistle',
            fg='Ivory',justify=CENTER)
lblTitle.grid(row=0,column=0)

"""receipt calcucation frame"""
RCF = Frame(root, bg = 'Lavender', bd =10,relief=RIDGE)
RCF.pack(side= RIGHT)

Button_F = Frame(RCF, bg = 'Lavender', bd =3,relief=RIDGE)
Button_F.pack(side= BOTTOM)

CF = Frame(RCF, bg = 'Lavender', bd =6,relief=RIDGE)
CF.pack(side= TOP)

"""RECEIPT FRAME"""
RF = Frame(RCF, bg = 'Lavender', bd =4,relief=RIDGE)
RF.pack(side= BOTTOM)

"""menu frame"""
MF = Frame(root, bg = 'Thistle', bd =10,relief=RIDGE)
MF.pack(side= LEFT)
Cost_F = Frame(MF, bg = 'Thistle', bd =4)
Cost_F.pack(side= BOTTOM)
Drinks_F = Frame(MF, bg = 'Thistle', bd =10)
Drinks_F.pack(side= TOP)

Drinks_F = Frame(MF, bg = 'Lavender', bd =10,relief=RIDGE)
Drinks_F.pack(side= LEFT)
Cake_F = Frame(MF, bg = 'Lavender', bd =10,relief=RIDGE)
Cake_F.pack(side= RIGHT)

"""VARIABLES"""

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofCakes= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input = StringVar()
operator=""

E_Latte= StringVar()
E_Iced_Latte= StringVar()
E_Americano= StringVar()
E_Iced_Americano= StringVar()
E_Espresso= StringVar()
E_Cappuccino= StringVar()
E_Iced_Cappuccino= StringVar()
E_Milk_Tea= StringVar()
E_Milk_Shake= StringVar()


E_School_Cake= StringVar()
E_Chocolate_Cake= StringVar()
E_Blueberry_Cake= StringVar()
E_Cheese_Cake= StringVar()
E_Fruit_Tart= StringVar()
E_Chicken_Pie= StringVar()
E_Waffles= StringVar()
E_Classic_Burger= StringVar()
E_Chicken_Sandwich= StringVar()

E_Latte.set("0")
E_Iced_Latte.set("0")
E_Americano.set("0")
E_Iced_Americano.set("0")
E_Espresso.set("0")
E_Cappuccino.set("0")
E_Iced_Cappuccino.set("0")
E_Milk_Tea.set("0")
E_Milk_Shake.set("0")

E_School_Cake.set("0")
E_Chocolate_Cake.set("0")
E_Blueberry_Cake.set("0")
E_Cheese_Cake.set("0")
E_Fruit_Tart.set("0")
E_Chicken_Pie.set("0")
E_Waffles.set("0")
E_Classic_Burger.set("0")
E_Chicken_Sandwich.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

"""EXIT"""

def iExit() :
    iExit = tkinter.messagebox.askyesno("Exit The System", "CONFIRM IF YOU WANT TO EXIT")
    if iExit > 0:
        root.destroy()
    return

def Reset() :
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Latte.set("0")
    E_Iced_Latte.set("0")
    E_Americano.set("0")
    E_Iced_Americano.set("0")
    E_Espresso.set("0")
    E_Cappuccino.set("0")
    E_Iced_Cappuccino.set("0")
    E_Milk_Tea.set("0")
    E_Milk_Shake.set("0")

    E_School_Cake.set("0")
    E_Chocolate_Cake.set("0")
    E_Blueberry_Cake.set("0")
    E_Cheese_Cake.set("0")
    E_Fruit_Tart.set("0")
    E_Chicken_Pie.set("0")
    E_Waffles.set("0")
    E_Classic_Burger.set("0")
    E_Chicken_Sandwich.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    txtLatte.configure(state=DISABLED)
    txtI_Latte.configure(state=DISABLED)
    txtAmericano.configure(state=DISABLED)
    txtI_Americano.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtI_Cappuccino.configure(state=DISABLED)
    txtMT.configure(state=DISABLED)
    txtMS.configure(state=DISABLED)

    txtSchool_Cake.configure(state=DISABLED)
    txtChocolate_Cake.configure(state=DISABLED)
    txtBlueberry_Cake.configure(state=DISABLED)
    txtCheese_Cake.configure(state=DISABLED)
    txtFruit_Tart.configure(state=DISABLED)
    txtChicken_Pie.configure(state=DISABLED)
    txtWaffles.configure(state=DISABLED)
    txtClassic_Burger.configure(state=DISABLED)
    txtChicken_Sandwich.configure(state=DISABLED)

def CostofItem() :
    Item1 = float(E_Latte.get())
    Item2 = float(E_Iced_Latte.get())
    Item3 = float(E_Americano.get())
    Item4 = float(E_Iced_Americano.get())
    Item5 = float(E_Espresso.get())
    Item6 = float(E_Cappuccino.get())
    Item7 = float(E_Iced_Cappuccino.get())
    Item8 = float(E_Milk_Tea.get())
    Item9 = float(E_Milk_Shake.get())

    Item10 = float(E_School_Cake.get())
    Item11= float(E_Chocolate_Cake.get())
    Item12 = float(E_Blueberry_Cake.get())
    Item13= float(E_Cheese_Cake.get())
    Item14 = float(E_Fruit_Tart.get())
    Item15 = float(E_Chicken_Pie.get())
    Item16 = float(E_Waffles.get())
    Item17 = float(E_Classic_Burger.get())
    Item18 = float(E_Chicken_Sandwich.get())

    PriceofDrinks = (Item1 * 120) + (Item2 * 140) + (Item3 * 110) + (Item4 * 120) \
                    + (Item5 * 180)+ (Item6 * 200) + (Item7 * 250) + (Item8 * 90) + (Item9 * 180)
    PriceofCakes = (Item10 * 50) + (Item11 * 120) + (Item12 * 110) + (Item13 * 150) + (Item14 * 150)+ (Item15 * 200) + (Item16 * 190) + (Item17 * 200) + (Item18 * 190)

    DrinksPrice = "৳", str('%.2f'%(PriceofDrinks))
    CakesPrice = "৳", str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC= "৳",str('%.2f'%(40))
    ServiceCharge.set(SC)

    SubTotalofItems = "৳", str('%.2f'%(PriceofDrinks + PriceofCakes + 40))
    SubTotal.set(SubTotalofItems)
    Tax = "৳", str('%.2f'%((PriceofDrinks + PriceofCakes + 40)*0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 40)*0.15)
    TC = "৳", str('%.2f'%(PriceofDrinks + PriceofCakes + 40 + TT))
    TotalCost.set(TC)

def chkLatte() :
    if(var1.get() == 1) :
        txtLatte.configure(state = NORMAL)
        txtLatte.focus()
        txtLatte.delete('0',END)
        E_Latte.set("0")

def chkI_Latte() :
    if(var2.get() == 1) :
        txtI_Latte.configure(state = NORMAL)
        txtI_Latte.focus()
        txtI_Latte.delete('0',END)
        E_Iced_Latte.set("0")

def chkAmericano() :
    if(var3.get() == 1) :
        txtAmericano.configure(state = NORMAL)
        txtAmericano.focus()
        txtAmericano.delete('0',END)
        E_Americano.set("0")

def chkI_Americano() :
    if(var4.get() == 1) :
        txtI_Americano.configure(state = NORMAL)
        txtI_Americano.focus()
        txtI_Americano.delete('0',END)
        E_Iced_Americano.set("0")

def chkEspresso() :
    if(var5.get() == 1) :
        txtEspresso.configure(state = NORMAL)
        txtEspresso.focus()
        txtEspresso.delete('0',END)
        E_Espresso.set("0")

def chkCappuccino() :
    if(var6.get() == 1) :
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete('0',END)
        E_Cappuccino.set("0")

def chkI_Cappuccino() :
    if(var7.get() == 1) :
        txtI_Cappuccino.configure(state = NORMAL)
        txtI_Cappuccino.focus()
        txtI_Cappuccino.delete('0',END)
        E_Iced_Cappuccino.set("0")

def chkMT() :
    if(var8.get() == 1) :
        txtMT.configure(state = NORMAL)
        txtMT.focus()
        txtMT.delete('0',END)
        E_Milk_Tea.set("0")

def chkMS() :
    if(var9.get() == 1) :
        txtMS.configure(state = NORMAL)
        txtMS.focus()
        txtMS.delete('0',END)
        E_Milk_Shake.set("0")

def chkSC() :
    if(var10.get() == 1) :
        txtSchool_Cake.configure(state = NORMAL)
        txtSchool_Cake.focus()
        txtSchool_Cake.delete('0',END)
        E_School_Cake.set("0")

def chkChocolateCake() :
    if(var11.get() == 1) :
        txtChocolate_Cake.configure(state = NORMAL)
        txtChocolate_Cake.focus()
        txtChocolate_Cake.delete('0',END)
        E_Chocolate_Cake.set("0")

def chkBlueberryCake() :
    if(var12.get() == 1) :
        txtBlueberry_Cake.configure(state = NORMAL)
        txtBlueberry_Cake.focus()
        txtBlueberry_Cake.delete('0',END)
        E_Blueberry_Cake.set("0")

def chkCheeseCake() :
    if(var13.get() == 1) :
        txtCheese_Cake.configure(state = NORMAL)
        txtCheese_Cake.focus()
        txtCheese_Cake.delete('0',END)
        E_Cheese_Cake.set("0")

def chkFT() :
    if(var14.get() == 1) :
        txtFruit_Tart.configure(state = NORMAL)
        txtFruit_Tart.focus()
        txtFruit_Tart.delete('0',END)
        E_Fruit_Tart.set("0")

def chkChickenPie() :
    if(var15.get() == 1) :
        txtChicken_Pie.configure(state = NORMAL)
        txtChicken_Pie.focus()
        txtChicken_Pie.delete('0',END)
        E_Chicken_Pie.set("0")

def chkWaffles() :
    if(var16.get() == 1) :
        txtWaffles.configure(state = NORMAL)
        txtWaffle.focus()
        txtWaffle.delete('0',END)
        E_Waffles.set("0")

def chkCB() :
    if(var17.get() == 1) :
        txtClassic_Burger.configure(state = NORMAL)
        txtClassic_Burger.focus()
        txtClassic_Burger.delete('0',END)
        E_Classic_Burger.set("0")

def chkCS() :
    if(var18.get() == 1) :
        txtChicken_Sandwich.configure(state = NORMAL)
        txtChicken_Sandwich.focus()
        txtChicken_Sandwich.delete('0',END)
        E_Chicken_Sandwich.set("0")

def Receipt() :
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill "+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t'+ Receipt_Ref.get()+'\t\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END,"==============================================\n")

    txtReceipt.insert(END,'Items\t\t\t\t'+ "No. of Items \n")
    txtReceipt.insert(END,'Latte: \t\t\t\t\t'+ E_Latte.get()+"\n")
    txtReceipt.insert(END,'Iced Latte: \t\t\t\t\t'+ E_Iced_Latte.get()+"\n")
#    txtReceipt.insert(END,'Iced Latte: \t\t\t\t\t'+ E_Iced_Latte.get()+"\n")




"""Drinks"""
Latte = Checkbutton(Drinks_F,text="Latte", variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkLatte).grid(row=0, sticky=W)
Iced_Latte = Checkbutton(Drinks_F,text="Iced Latte", variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkI_Latte).grid(row=1, sticky=W)
Americano = Checkbutton(Drinks_F,text="Americano", variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkAmericano).grid(row=2, sticky=W)
Iced_Americano = Checkbutton(Drinks_F,text="Iced Americano", variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkI_Americano).grid(row=3, sticky=W)
Espresso = Checkbutton(Drinks_F,text="Espresso", variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkEspresso).grid(row=4, sticky=W)
Cappuccino = Checkbutton(Drinks_F,text="Cappuccino", variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkCappuccino).grid(row=5, sticky=W)
Iced_Cappuccino = Checkbutton(Drinks_F,text="Iced Cappuccino", variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkI_Cappuccino).grid(row=6, sticky=W)
Milk_Tea= Checkbutton(Drinks_F,text="Milk Tea", variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkMT).grid(row=7, sticky=W)
Milk_Shake= Checkbutton(Drinks_F,text="MilkShake", variable=var9, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkMS).grid(row=8, sticky=W)

"""entry box for drinks"""

txtLatte= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Latte,bd=8,width=6, justify=LEFT,state= DISABLED )
txtLatte.grid(row=0,column=1)
txtI_Latte= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Iced_Latte,bd=8,width=6, justify=LEFT,state= DISABLED)
txtI_Latte.grid(row=1,column=1)
txtAmericano= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Americano,bd=8,width=6, justify=LEFT,state= DISABLED)
txtAmericano.grid(row=2,column=1)
txtI_Americano= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Iced_Americano,bd=8,width=6, justify=LEFT,state= DISABLED)
txtI_Americano.grid(row=3,column=1)
txtEspresso= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Espresso,bd=8,width=6, justify=LEFT,state= DISABLED)
txtEspresso.grid(row=4,column=1)
txtCappuccino= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Cappuccino,bd=8,width=6, justify=LEFT,state= DISABLED)
txtCappuccino.grid(row=5,column=1)
txtI_Cappuccino= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Iced_Cappuccino,bd=8,width=6, justify=LEFT,state= DISABLED)
txtI_Cappuccino.grid(row=6,column=1)
txtMT= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Milk_Tea,bd=8,width=6, justify=LEFT,state= DISABLED)
txtMT.grid(row=7,column=1)
txtMS= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Milk_Shake,bd=8,width=6, justify=LEFT,state= DISABLED)
txtMS.grid(row=8,column=1)


"""Cakes"""
School_Cake= Checkbutton(Cake_F,text="School Cake", variable=var10, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkSC).grid(row=0, sticky=W)
Chocolate_Cake= Checkbutton(Cake_F,text="Chocolate Cake", variable=var11, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkChocolateCake).grid(row=1, sticky=W)
Blueberry_Cake= Checkbutton(Cake_F,text="Blueberry Cake", variable=var12, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkBlueberryCake).grid(row=2, sticky=W)
Cheese_Cake= Checkbutton(Cake_F,text="Cheese Cake", variable=var13, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkCheeseCake).grid(row=3, sticky=W)
Fruit_Tart= Checkbutton(Cake_F,text="Fruit Tart", variable=var14, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkFT).grid(row=4, sticky=W)
Chicken_Pie= Checkbutton(Cake_F,text="Chicken Pie", variable=var15, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkChickenPie).grid(row=5, sticky=W)
Waffles = Checkbutton(Cake_F,text="Waffles", variable=var16, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkWaffles).grid(row=6, sticky=W)
Classic_Burger= Checkbutton(Cake_F,text="Classic Burger", variable=var17, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkCB).grid(row=7, sticky=W)
Chicken_Sandwich= Checkbutton(Cake_F,text="Chicken Sandwich", variable=var18, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                    bg='Lavender', fg='Grey',command = chkCS).grid(row=8, sticky=W)

"""entry box for cakes"""
txtSchool_Cake= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_School_Cake)
txtSchool_Cake.grid(row=0,column=1)
txtChocolate_Cake= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Chocolate_Cake)
txtChocolate_Cake.grid(row=1,column=1)
txtBlueberry_Cake= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Blueberry_Cake)
txtBlueberry_Cake.grid(row=2,column=1)
txtCheese_Cake= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Cheese_Cake)
txtCheese_Cake.grid(row=3,column=1)
txtFruit_Tart= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Fruit_Tart)
txtFruit_Tart.grid(row=4,column=1)
txtChicken_Pie= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Chicken_Pie)
txtChicken_Pie.grid(row=5,column=1)
txtWaffles= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Waffles)
txtWaffles.grid(row=6,column=1)
txtClassic_Burger= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Classic_Burger)
txtClassic_Burger.grid(row=7,column=1)
txtChicken_Sandwich= Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6, justify=LEFT,state= DISABLED,textvariable= E_Chicken_Sandwich)
txtChicken_Sandwich.grid(row=8,column=1)

"""Total Cost"""
lblCOD = Label(Cost_F, font = ('arial',15,'bold',),
            text = "Cost of Drinks",bg='Thistle',fg='Grey')
lblCOD.grid(row=0,column=0,sticky=W)
txtCOD = Entry(Cost_F, bg="white", bd=7,textvariable=CostofDrinks, font=('arial', 14, 'bold'),insertwidth = 2,justify=RIGHT)
txtCOD.grid(row=0,column=1)

lblCOC = Label(Cost_F, font = ('arial',15,'bold',),
            text = "Cost of Cakes",bg='Thistle',fg='Grey')
lblCOC.grid(row=1,column=0,sticky=W)
txtCOC = Entry(Cost_F, bg="white", bd=7,textvariable=CostofCakes, font=('arial', 14, 'bold'),insertwidth = 2,justify=RIGHT)
txtCOC.grid(row=1,column=1)

lblSC = Label(Cost_F, font = ('arial',15,'bold',),
            text = "Service Charge",bg='Thistle',fg='Grey')
lblSC.grid(row=2,column=0,sticky=W)
txtSC = Entry(Cost_F, bg="white", bd=7,textvariable=ServiceCharge, font=('arial', 14, 'bold'),insertwidth = 2,justify=RIGHT)
txtSC.grid(row=2,column=1)
"""Payment info"""

lblST = Label(Cost_F, font = ('arial',15,'bold',),
            text = "Sub Total",bg='Thistle',fg='Grey')
lblST.grid(row=0,column=2,sticky=W)
txtST = Entry(Cost_F, bg="white", bd=7,textvariable=SubTotal, font=('arial', 14, 'bold'),insertwidth = 2,justify=RIGHT)
txtST.grid(row=0,column=3)

lblPaidTax = Label(Cost_F, font = ('arial',15,'bold',),
            text = "Paid Tax",bg='Thistle',fg='Grey')
lblPaidTax.grid(row=1,column=2,sticky=W)
txtPaidTax = Entry(Cost_F, bg="white", bd=7,textvariable=PaidTax, font=('arial', 14, 'bold'),insertwidth = 2,justify=RIGHT)
txtPaidTax.grid(row=1,column=3)


lblTotalCost = Label(Cost_F, font = ('arial',15,'bold',),
            text = "Total Cost",bg='Thistle',fg='Grey')
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F, bg="white", bd=7,textvariable=TotalCost, font=('arial', 14, 'bold'),insertwidth = 2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)


"""Receipt box"""

txtReceipt = Text(RF, width=46, height=12, bg="white", bd=4,font=('arial', 12, 'bold'))
txtReceipt.grid(row=0,column=0)

"""BUTTON"""
btnTotal = Button(Button_F, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="Total",bg="Lavender",command = CostofItem).grid(row=0,column=0)
btnReceipt = Button(Button_F, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="Receipt",bg="Lavender",command=Receipt).grid(row=0,column=1)
btnReset = Button(Button_F, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="Reset",bg="Lavender",command=Reset).grid(row=0,column=2)
btnExit = Button(Button_F, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="Exit",bg="Lavender", command=iExit).grid(row=0,column=3)

"""Calculator Display"""

def btnClick(numbers) :
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear() :
    global operator
    operator = ""
    text_Input.set("")

def btnEquals() :
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(CF, width=45, bg="white", bd=4, textvariable = text_Input, font=('arial', 12, 'bold'),justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

"""Calculator BUTTON"""
btn7 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="7",bg="Lavender",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="8",bg="Lavender",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="9",bg="Lavender",command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="+",bg="Lavender",command=lambda:btnClick("+")).grid(row=2,column=3)
btn4 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="4",bg="Lavender",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="5",bg="Lavender",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="6",bg="Lavender",command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="-",bg="Lavender",command=lambda:btnClick("-")).grid(row=3,column=3)
btn1 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="1",bg="Lavender",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="2",bg="Lavender",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="3",bg="Lavender",command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="*",bg="Lavender",command=lambda:btnClick("*")).grid(row=4,column=3)
btn0 = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="0",bg="Lavender",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="C",bg="Lavender",command=btnClear).grid(row=5,column=1)
btnEquals = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="=",bg="Lavender",command=btnEquals) .grid(row=5,column=2)
btnDiv = Button(CF, padx=16,pady=1,bd=7,fg="Grey",font=('arial',16,'bold'),width=4,
            text="/",bg="Lavender",command=lambda:btnClick("/")).grid(row=5,column=3)


root.mainloop()
