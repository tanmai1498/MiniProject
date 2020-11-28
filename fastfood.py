from tkinter import*
import random
import time
import datetime
from tkinter import Tk,StringVar,ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
root=Tk()
root.geometry("1350x750+0+0")
root.title("D.p's Fast Food")

Tops = Frame(root,width=1350,height=100,bd=12,relief="raise")
Tops.pack(side=TOP)

lblTitle= Label(Tops,font=('arial',50,'bold'),text="\tD.P's Fast Food\t",fg="Red")
lblTitle.grid(row=0,column=0)
#time
localtime=time.asctime(time.localtime(time.time()))
#print(localtime)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Blue",bd=10,anchor='s')
lblInfo.grid(row=1,column=0)



BottomMainFrame = Frame(root,width=1350,height=650,bd=12,relief="raise")
BottomMainFrame.pack(side=BOTTOM)

F1= Frame(BottomMainFrame,width=450,height=650,bd=12,relief="raise")
F1.pack(side=LEFT)
F2 = Frame(BottomMainFrame,width=450,height=650,bd=12,relief="raise")
F2.pack(side=LEFT)
F2Top = Frame(F2,width=450,height=350,bd=4,relief="raise")
F2Top.pack(side=TOP)
F2Bottom = Frame(F2,width=550,height=300,bd=4,relief="raise")
F2Bottom.pack(side=BOTTOM)

F3 = Frame(BottomMainFrame,width=450,height=650,bd=12,relief="raise")
F3.pack(side=RIGHT)



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
var18=StringVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()

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
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
varDosa=StringVar()
varDosa.set("0")
varmDosa=StringVar()
varmDosa.set("0")
varmyDosa=StringVar()
varmyDosa.set("0")
varpaper=StringVar()
varpaper.set("0")
varravaDosa=StringVar()
varravaDosa.set("0")
varcheesesandwich=StringVar()
varcheesesandwich.set("0")
varfishsandwich=StringVar()
varfishsandwich.set("0")
varchickensandwich=StringVar()
varchickensandwich.set("0")

def Database():
    global connection,cursor
    connection=sqlite3.connect("database.db")
    
    cursor=connection.cursor()
    #cursor.execute("CREATE TABLE IF NOT EXISTS 'Dosas'(Reference INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Fries INTEGER,Noodles INTEGER,Soup INTEGER,Burger INTEGER,Sandwich INTEGER,Drinks INTEGER,Cost INTEGER)")
    connection.commit()
def add():
    Database()
    #conn=sqlite3.connect("restrnt.db")
    #cursor=conn.cursor()
    #cursor.execute("INSERT INTO `Table1`(Reference,SadaDosa,MasalaDosa,MysoreDosa,PaperDosa,RavaDosa,cheesesandwich,fishsandwich,chickensandwich,fruitbeer,gingerlemon,coldcofee,softdrink,tea,pizza,jainpizza,cheesepizza,mushroompizza,sweetcorn,chillygarlic,paneercheese,tax,subtotal,total)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(str(varref.get()),str(varDosa.get()),str(varmDosa.get()),str(varmyDosa.get()),str(varpaper.get()),str(varravaDosa.get()),str(varcheesesandwich.get()),str(varfishsandwich.get()),str(varchickensandwich.get()),str(varfruitbeer.get()),str(vargingerlemon.get()),str(varcoldcofee.get()),str(varsoftdrink.get()),str(vartea.get()),str(varpizza.get()),str(varjain.get()),str(varcheese.get()),str(varmush.get()),str(varcorn.get()),str(varchilly.get()),str(varpc.get()),str(vartax.get()),str(varsubtotal.get()),str(vartotal.get())))
    cursor.execute("INSERT INTO `Orders`(Reference,Orderdate,Total,Address,Contact)VALUES(?,?,?,?,?)",(str(varref.get()),str(localtime),str(vartotal.get()),str(varaddress.get()),str(varcontact.get())))
    connection.commit()
    cursor.close()

'''def orderdetail():
    Database()
    cursor.execute('''

def qExit():
    e=tkMessageBox.askquestion('system','Do you want to exit?',icon="warning")
    if e=='yes':
        root.destroy()
        exit()
def Reset():
    varDosa.set("")
    varmDosa.set("")
    varmyDosa.set("")
    varpaper.set("")
    varravaDosa.set("")
    varcheesesandwich.set("")
    varfishsandwich.set("")
    varchickensandwich.set("")
    varpizza.set("")
    varjain.set("")
    varcheese.set("")
    varmush.set("")
    varcorn.set("")
    varchilly.set("")
    varpc.set("")
    varfruitbeer.set("")
    vargingerlemon.set("")
    varcoldcofee.set("")
    vartea.set("")
    varsoftdrink.set("")
    varchange.set("")
    vartax.set("")
    varsubtotal.set("")
    vartotal.set("")
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var6.set("")
    var7.set("")
    var8.set("")
    var9.set("")
    var10.set("")
    var11.set("")
    var12.set("")
    var13.set("")
    var14.set("")
    var15.set("")
    var16.set("")
    var17.set("")
    var24.set("")
    var25.set("")
    var26.set("")
    varref.set("")
    varaddress.set("")
    varcontact.set("")














    txtDosa.configure(state = DISABLED)
    txtmDosa.configure(state = DISABLED)
    txtmyDosa.configure(state = DISABLED)
    txtPaper.configure(state = DISABLED)
    txtravaDosa.configure(state = DISABLED)

    txtcheesesandwich.configure(state = DISABLED)
    txtfishsandwich.configure(state=DISABLED)
    txtcs.configure(state = DISABLED)
    
    txtfruitbeer.configure(state = DISABLED)
    txtgingerlemon.configure(state = DISABLED)
    txtcoldcofee.configure(state = DISABLED)
    txtsoftdrink.configure(state = DISABLED)
    txttea.configure(state = DISABLED)

    txtpizza.configure(state = DISABLED)
    txtjain.configure(state = DISABLED)
    txtcheese.configure(state = DISABLED)
    txtmush.configure(state = DISABLED)
    txtcorn.configure(state = DISABLED)
    txtchillyg.configure(state = DISABLED)
    txtp.configure(state = DISABLED)

    txttax.configure(state = DISABLED)
    txtsubtotal.configure(state = DISABLED)
    txttotal.configure(state = DISABLED)

    
    
























def chksadadosa():
    if(var1.get() == 1):
        txtDosa.configure(state=NORMAL)
        varDosa.set("")
    elif(var1.get() == 0):
        txtDosa.configure(state=DISABLED)
        varDosa.set("0")
def chkmasaladosa():
    if(var2.get() == 1):
        txtmDosa.configure(state=NORMAL)
        varmDosa.set("")
    elif(var2.get() == 0):
        txtmDosa.configure(state=DISABLED)
        varmDosa.set("0")

def chkmysoredosa():
    if(var3.get() == 1):
        txtmyDosa.configure(state=NORMAL)
        varmyDosa.set("")
    elif(var3.get() == 0):
        txtmyDosa.configure(state=DISABLED)
        varmyDosa.set("0")
def chkpapersada():
    if(var4.get() == 1):
        txtPaper.configure(state=NORMAL)
        varpaper.set("")
    elif(var4.get() == 0):
        txtPaper.configure(state=DISABLED)
        varpaper.set("0")

def chkravadosa():
    if(var5.get() == 1):
        txtravaDosa.configure(state=NORMAL)
        varravaDosa.set("")
    elif(var5.get() == 0):
        txtravaDosa.configure(state=DISABLED)
        varravaDosa.set("0")
def chkcheesesandwich():
    if(var24.get() == 1):
        txtcheesesandwich.configure(state=NORMAL)
        varcheesesandwich.set("")
    elif(var24.get() == 0):
        txtcheesesandwich.configure(state=DISABLED)
        varcheesesandwich.set("0")

def chkfishsandwich():
    if(var25.get() == 1):
        txtfishsandwich.configure(state=NORMAL)
        varfishsandwich.set("")
    elif(var25.get() == 0):
        txtfishsandwich.configure(state=DISABLED)
        varfishsandwich.set("0")

def chkchickensandwich():
    if(var26.get() == 1):
        txtcs.configure(state=NORMAL)
        varchickensandwich.set("")
    elif(var26.get() == 0):
        txtcs.configure(state=DISABLED)
        varchickensandwich.set("0")

def chkfruitbeer():
    if(var6.get() == 1):
        txtfruitbeer.configure(state=NORMAL)
        varfruitbeer.set("")
    elif(var6.get() == 0):
        txtfruitbeer.configure(state=DISABLED)
        varfruitbeer.set("0")
def chkgingerlemon():
    if(var7.get() == 1):
        txtgingerlemon.configure(state=NORMAL)
        vargingerlemon.set("")
    elif(var7.get() == 0):
        txtgingerlemon.configure(state=DISABLED)
        vargingerlemon.set("0")
def chkcoldcofee():
    if(var8.get() == 1):
        txtcoldcofee.configure(state=NORMAL)
        varcoldcofee.set("")
    elif(var8.get() == 0):
        txtcoldcofee.configure(state=DISABLED)
        varcoldcofee.set("0")
def chksoftdrink():
    if(var9.get() == 1):
        txtsoftdrink.configure(state=NORMAL)
        varsoftdrink.set("")
    elif(var9.get() == 0):
        txtsoftdrink.configure(state=DISABLED)
        varsoftdrink.set("0")
def chktea():
    if(var10.get() == 1):
        txttea.configure(state=NORMAL)
        vartea.set("")
    elif(var10.get() == 0):
        txttea.configure(state=DISABLED)
        vartea.set("0")

def chkpizza():
    if(var11.get() == 1):
        txtpizza.configure(state=NORMAL)
        varpizza.set("")
    elif(var11.get() == 0):
        txtpizza.configure(state=DISABLED)
        varpizza.set("0")
def chkjainpizza():
    if(var12.get() == 1):
        txtjain.configure(state=NORMAL)
        varjain.set("")
    elif(var12.get() == 0):
        txtjain.configure(state=DISABLED)
        varjain.set("0")
def chkonlycheese():
    if(var13.get() == 1):
        txtcheese.configure(state=NORMAL)
        varcheese.set("")
    elif(var13.get() == 0):
        txtcheese.configure(state=DISABLED)
        varcheese.set("0")
def chkmushroom():
    if(var14.get() == 1):
        txtmush.configure(state=NORMAL)
        varmush.set("")
    elif(var14.get() == 0):
        txtmush.configure(state=DISABLED)
        varmush.set("0")
def chkchillygarlic():
    if(var16.get() == 1):
        txtchillyg.configure(state=NORMAL)
        varchilly.set("")
    elif(var16.get() == 0):
        txtchillyg.configure(state=DISABLED)
        varchilly.set("0")
def chkpaneercheese():
    if(var17.get() == 1):
        txtp.configure(state=NORMAL)
        varpc.set("")
    elif(var17.get() == 0):
        txtp.configure(state=DISABLED)
        varpc.set("0")
def chkcorn():
    if(var15.get() == 1):
        txtcorn.configure(state=NORMAL)
        varcorn.set("")
    elif(var15.get() == 0):
        txtcorn.configure(state=DISABLED)
        varcorn.set("0")

def costofmeal():
    meal1=float(varDosa.get())
    meal2=float(varmDosa.get())
    meal3=float(varmyDosa.get())
    meal4=float(varpaper.get())
    meal5=float(varravaDosa.get())
    meal6=float(varcheesesandwich.get())
    meal7=float(varfishsandwich.get())
    meal8=float(varchickensandwich.get())
    meal9=float(varfruitbeer.get())
    meal10=float(vargingerlemon.get())
    meal11=float(varcoldcofee.get())
    meal12=float(varsoftdrink.get())
    meal13=float(vartea.get())
    meal14=float(varpizza.get())
    meal15=float(varjain.get())
    meal16=float(varcheese.get())
    meal17=float(varmush.get())
    meal18=float(varcorn.get())
    meal19=float(varchilly.get())
    meal20=float(varpc.get())


    itotal1=((meal1*25)+(meal2*35)+(meal3*60)+(meal4*55))
    itotal2=((meal5*45)+(meal6*40)+(meal7*35)+(meal8*45))
    itotal3=((meal9*40)+(meal10*15)+(meal11*30)+(meal12*25))
    itotal4=((meal13*20)+(meal14*80)+(meal15*75)+(meal16*100))
    itotal5=((meal17*120)+(meal18*100)+(meal19*130)+(meal20*150))

    if (var18.get() == 'Cash'):
        ichange = float(varpay.get())
        icost = (itotal1+itotal2+itotal3+itotal4+itotal5)
        itax = (icost*3.4)/100
        itaxq="Rs",str('%.2f'%(itax))
        vartax.set(itaxq)

        icostq = "Rs", str('%.2f'%(icost))
        varsubtotal.set(icostq)
        itotalq="Rs",str('%.2f'%((icost+itax)))
        vartotal.set(itotalq)
        cchange=(ichange-(icost+itax))
        cchangeq = "Rs", str('%.2f'%(cchange))
        varchange.set(cchangeq)
    elif(var18.get() =="Master Card" or "Visa Card" or "Debit Card"):
        varpay.set("")
        icost = (itotal1+itotal2+itotal3+itotal4+itotal5)
        itax = (icost*3.4)/100
        itaxq="Rs",str('%.2f'%(itax))
        vartax.set(itaxq)
        icostq = "Rs", str('%.2f'%(icost))
        varsubtotal.set(icostq)
        itotalq="Rs",str('%.2f'%((icost+itax)))
        vartotal.set(itotalq)
        varchange.set("")

def newwinreceipt():
    global receiptform
    receiptform=Toplevel()
    receiptform.title("receipt")
    receiptform.geometry("1000x5000")
    #s=Frame(receiptform,width=100,relief=RAISED)
    lblReceipt=Label(receiptform,font=('arial',12,'bold'),text="Receipt",bd=10)
    lblReceipt.grid(row=0,column=0,sticky=W)
    txtReceipt=Text(receiptform,font=('arial',11,'bold'),bd=7,width=40,height=4)
    txtReceipt.grid(row=1,column=1,sticky=W)
    #txtReceipt.insert(END,"aaaa")
    txtReceipt.delete("1.0",END)
    
    txtReceipt.insert(END,'Reference \t\t\t ' + str(varref.get()) + "\n")
    
    txtReceipt.insert(END,'SadaDosa \t\t\t ' + str(varDosa.get()) + "\n")
    txtReceipt.insert(END,'Masala Dosa\t\t\t ' + str(varmDosa.get()) + "\n")
    txtReceipt.insert(END,'MysoreDosa \t\t\t ' + str(varmyDosa.get()) + "\n")
    txtReceipt.insert(END,'PaperDosa\t\t\t ' + str(varpaper.get()) + "\n")
    txtReceipt.insert(END,'RavaDosa \t\t\t ' + str(varravaDosa.get()) + "\n")
    txtReceipt.insert(END,'CheeseSandwich\t\t\t ' + str(varcheesesandwich.get()) + "\n")
    txtReceipt.insert(END,'FishSandwich \t\t\t ' + str(varfishsandwich.get()) + "\n")
    txtReceipt.insert(END,'Chicken Sandwich \t\t\t ' + str(varchickensandwich.get()) + "\n")
    txtReceipt.insert(END,'FruitBeer \t\t\t ' + str(varfruitbeer.get()) + "\n")
    txtReceipt.insert(END,'GingerLemon\t\t\t ' + str(vargingerlemon.get()) + "\n")
    txtReceipt.insert(END,'ColdCofee\t\t\t ' + str(varcoldcofee.get()) + "\n")
    txtReceipt.insert(END,'Softdrink\t\t\t ' + str(varsoftdrink.get()) + "\n")
    txtReceipt.insert(END,'Tea\t\t\t ' + str(vartea.get()) + "\n")
    txtReceipt.insert(END,'Pizza\t\t\t ' + str(varpizza.get()) + "\n")
    txtReceipt.insert(END,'JainPizza\t\t\t ' + str(varjain.get()) + "\n")
    txtReceipt.insert(END,'CheesePizza\t\t\t ' + str(varcheese.get()) + "\n")
    txtReceipt.insert(END,'MushroomPizza\t\t\t ' + str(varmush.get()) + "\n")
    txtReceipt.insert(END,'SweetCorn\t\t\t ' + str(varcorn.get()) + "\n")
    txtReceipt.insert(END,'ChillyGarlic\t\t\t ' + str(varchilly.get()) + "\n")
    txtReceipt.insert(END,'PaneerCheese\t\t\t ' + str(varpc.get()) + "\n")
    txtReceipt.insert(END,'Tax\t\t\t ' + str(vartax.get()) + "\n")
    txtReceipt.insert(END,'SubTotal\t\t\t ' + str(varsubtotal.get()) + "\n")
    txtReceipt.insert(END,'Total\t\t\t ' + str(vartotal.get()) + "\n")
    lbltext=Label(receiptform,font=('arial',12,'bold'),text="Have a nice day,visit again!",bd=10)
    lbltext.grid(row=3,column=1,sticky=W)
'''def order():
    global orderdetail
    orderdetail=Toplevel()
    orderdetail.title("order")
    orderdetail.geometry("1000x5000")
    lblorderdetailid=Label(orderdetail,font=('arial',12,'bold'),text="orderdetailid",bd=10)
    lblorderdetailid.grid(row=0,column=0,sticky=W)
    txtorderdetailid=Text(orderdetail,font=('arial',11,'bold'),bd=7,width=40,height=4)
    txtorderdetailid.grid(row=1,column=1,sticky=W)'''
    
    
varref=StringVar()
varaddress=StringVar()
varcontact=IntVar()
varcontact.set("")
varref.set("")
varaddress.set("")
lblreference= Label(F3,font=('arial',18,'bold'),text="Reference")
lblreference.grid(row=9,column=0)
txtreference= Entry(F3,font=('arial',18,'bold'),textvariable=varref,width=10)
txtreference.grid(row=9,column=1)

lblAddress= Label(F3,font=('arial',18,'bold'),text="Address")
lblAddress.grid(row=10,column=0)
txtAddress= Entry(F3,font=('arial',18,'bold'),textvariable=varaddress,width=10)
txtAddress.grid(row=10,column=1)

lblContact= Label(F3,font=('arial',18,'bold'),text="Contact")
lblContact.grid(row=11,column=0)
txtContact= Entry(F3,font=('arial',18,'bold'),textvariable=varcontact,width=10)
txtContact.grid(row=11,column=1)

       

#frame1
lblDosas= Label(F1,font=('arial',18,'bold'),text="DOSAS")
lblDosas.grid(row=0,column=0)
sadadosa=Checkbutton(F1,text="Sada Dosa\t₹25",variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chksadadosa).grid(row=1,column=0,sticky=W)
txtDosa= Entry(F1,font=('arial',18,'bold'),textvariable=varDosa,width=6,justify='left',state=DISABLED)
txtDosa.grid(row=1,column=1)

masaladosa=Checkbutton(F1,text="Masala Dosa\t₹35",variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkmasaladosa).grid(row=2,column=0,sticky=W)
txtmDosa= Entry(F1,font=('arial',18,'bold'),textvariable=varmDosa,width=6,justify='left',state=DISABLED)
txtmDosa.grid(row=2,column=1)

Mysoredosa=Checkbutton(F1,text="Mysore Dosa\t₹60",variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkmysoredosa).grid(row=3,column=0,sticky=W)
txtmyDosa= Entry(F1,font=('arial',18,'bold'),textvariable=varmyDosa,width=6,justify='left',state=DISABLED)
txtmyDosa.grid(row=3,column=1)

papersada=Checkbutton(F1,text="Paper Sada\t₹55",variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkpapersada).grid(row=4,column=0,sticky=W)
txtPaper= Entry(F1,font=('arial',18,'bold'),textvariable=varpaper,width=6,justify='left',state=DISABLED)
txtPaper.grid(row=4,column=1)

ravadosa=Checkbutton(F1,text="Rava Dosa\t₹45",variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkravadosa).grid(row=5,column=0,sticky=W)
txtravaDosa= Entry(F1,font=('arial',18,'bold'),textvariable=varravaDosa,width=6,justify='left',state=DISABLED)
txtravaDosa.grid(row=5,column=1)




lblSandwich= Label(F1,font=('arial',18,'bold'),text="Sandwiches")
lblSandwich.grid(row=6,column=0)

cheesesandwich=Checkbutton(F1,text="Cheese Sandwich\t₹40",variable=var24,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkcheesesandwich).grid(row=7,column=0,sticky=W)
txtcheesesandwich= Entry(F1,font=('arial',18,'bold'),textvariable=varcheesesandwich,width=6,justify='left',state=DISABLED)
txtcheesesandwich.grid(row=7,column=1)

fishsandwich=Checkbutton(F1,text="Fish Sandwich\t₹35",variable=var25,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkfishsandwich).grid(row=8,column=0,sticky=W)
txtfishsandwich= Entry(F1,font=('arial',18,'bold'),textvariable=varfishsandwich,width=6,justify='left',state=DISABLED)
txtfishsandwich.grid(row=8,column=1)

chickensandwich=Checkbutton(F1,text="Chicken Sandwich\t₹45",variable=var26,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkchickensandwich).grid(row=9,column=0,sticky=W)
txtcs= Entry(F1,font=('arial',18,'bold'),textvariable=varchickensandwich,width=6,justify='left',state=DISABLED)
txtcs.grid(row=9,column=1)


lblSpace=Label(F1,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
lblSpace.grid(row=10,column=0)

varfruitbeer=StringVar()
vargingerlemon=StringVar()
varcoldcofee=StringVar()
vartea=StringVar()
varsoftdrink=StringVar()

varfruitbeer.set("0")
vargingerlemon.set("0")
varcoldcofee.set("0")
vartea.set("0")
varsoftdrink.set("0")
#frame2
lblBeverages= Label(F2Top,font=('arial',18,'bold'),text="BEVERAGES")
lblBeverages.grid(row=0,column=0)
Fruitbeer=Checkbutton(F2Top,text="Fruit Beer\t₹40",variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkfruitbeer).grid(row=1,column=0,sticky=W)
txtfruitbeer= Entry(F2Top,font=('arial',18,'bold'),textvariable=varfruitbeer,width=6,justify='left',state=DISABLED)
txtfruitbeer.grid(row=1,column=1)

gingerlemon=Checkbutton(F2Top,text="Ginger Lemon\t₹15",variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkgingerlemon).grid(row=2,column=0,sticky=W)
txtgingerlemon= Entry(F2Top,font=('arial',18,'bold'),textvariable=vargingerlemon,width=6,justify='left',state=DISABLED)
txtgingerlemon.grid(row=2,column=1)

coldcofee=Checkbutton(F2Top,text="Cold Coffee\t₹30",variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkcoldcofee).grid(row=3,column=0,sticky=W)
txtcoldcofee= Entry(F2Top,font=('arial',18,'bold'),textvariable=varcoldcofee,width=6,justify='left',state=DISABLED)
txtcoldcofee.grid(row=3,column=1)

softdrink=Checkbutton(F2Top,text="Soft Drink\t₹25",variable=var9,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chksoftdrink).grid(row=4,column=0,sticky=W)
txtsoftdrink= Entry(F2Top,font=('arial',18,'bold'),textvariable=varsoftdrink,width=6,justify='left',state=DISABLED)
txtsoftdrink.grid(row=4,column=1)

tea=Checkbutton(F2Top,text="Tea\t₹20",variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chktea).grid(row=5,column=0,sticky=W)
txttea= Entry(F2Top,font=('arial',18,'bold'),textvariable=vartea,width=6,justify='left',state=DISABLED)
txttea.grid(row=5,column=1)

lblSpace2=Label(F2Top,text="\n\n\n\n\n")
lblSpace2.grid(row=6,column=0)

varpizza=StringVar()
varjain=StringVar()
varcheese=StringVar()
varmush=StringVar()
varcorn=StringVar()
varchilly=StringVar()
varpc=StringVar()

varpizza.set("0")
varjain.set("0")
varcheese.set("0")
varmush.set("0")
varcorn.set("0")
varchilly.set("0")
varpc.set("0")

#frame3

lblpizza= Label(F3,font=('arial',18,'bold'),text="PIZZERIA")
lblpizza.grid(row=0,column=0)

pizza=Checkbutton(F3,text="Pizza\t\t₹80",variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkpizza).grid(row=1,column=0,sticky=W)
txtpizza= Entry(F3,font=('arial',18,'bold'),textvariable=varpizza,width=8,justify='left',state=DISABLED)
txtpizza.grid(row=1,column=1)

jainpizza=Checkbutton(F3,text="JainPizza\t₹75",variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkjainpizza).grid(row=2,column=0,sticky=W)
txtjain= Entry(F3,font=('arial',18,'bold'),textvariable=varjain,width=8,justify='left',state=DISABLED)
txtjain.grid(row=2,column=1)

onlycheese=Checkbutton(F3,text="CheesePizza\t₹100",variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkonlycheese).grid(row=3,column=0,sticky=W)
txtcheese= Entry(F3,font=('arial',18,'bold'),textvariable=varcheese,width=8,justify='left',state=DISABLED)
txtcheese.grid(row=3,column=1)

mushroom=Checkbutton(F3,text="MushroomPizza\t₹120",variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkmushroom).grid(row=4,column=0,sticky=W)
txtmush= Entry(F3,font=('arial',18,'bold'),textvariable=varmush,width=8,justify='left',state=DISABLED)
txtmush.grid(row=4,column=1)

veg=Checkbutton(F3,text="SweeCorn\t₹100",variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkcorn).grid(row=5,column=0,sticky=W)
txtcorn= Entry(F3,font=('arial',18,'bold'),textvariable=varcorn,width=8,justify='left',state=DISABLED)
txtcorn.grid(row=5,column=1)

chillygarlic=Checkbutton(F3,text="ChillyGarlic\t₹130",variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkchillygarlic).grid(row=6,column=0,sticky=W)
txtchillyg= Entry(F3,font=('arial',18,'bold'),textvariable=varchilly,width=8,justify='left',state=DISABLED)
txtchillyg.grid(row=6,column=1)

pannercheese=Checkbutton(F3,text="Paneer Cheese\t₹150",variable=var17,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkpaneercheese).grid(row=7,column=0,sticky=W)
txtp= Entry(F3,font=('arial',18,'bold'),textvariable=varpc,width=8,justify='left',state=DISABLED)
txtp.grid(row=7,column=1)

lblSpace3=Label(F3,text="\n\n\n\n\n")
lblSpace3.grid(row=8,column=0)

varchange=StringVar()
vartax=StringVar()
varpay=StringVar()
varsubtotal=StringVar()
vartotal=StringVar()

varchange.set("0")
vartax.set("0")
varpay.set("0")
varsubtotal.set("0")
vartotal.set("0")

                
                
#payment
lblpayment= Label(F2Bottom,font=('arial',18,'bold'),text="Payment",bd=10,width=16,anchor='w')
lblpayment.grid(row=0,column=0)

"""lblchange= Label(F2Bottom,font=('arial',18,'bold'),text="Change",bd=10,anchor='w')
lblchange.grid(row=0,column=1)
txtchange= Entry(F2Bottom,font=('arial',18,'bold'),textvariable=varchange,width=6,state=DISABLED)
txtchange.grid(row=0,column=2)"""

cmbpaymentmethod=ttk.Combobox(F2Bottom,font=('arial',18,'bold'),textvariable=var18 ,state='readonly',width=20)
cmbpaymentmethod['value']=('Cash','Master Card','Visa Card','Debit Card')
cmbpaymentmethod.current(0)
cmbpaymentmethod.grid(row=1,column=0)

lbltax= Label(F2Bottom,font=('arial',18,'bold'),text="Tax",bd=10,anchor='w')
lbltax.grid(row=1,column=1)
txttax= Entry(F2Bottom,font=('arial',18,'bold'),textvariable=vartax,width=6,state=DISABLED)
txttax.grid(row=1,column=2)

#txtpayment= Entry(F2Bottom,font=('arial',18,'bold'),textvariable=varpay,width=6,justify='left',state=DISABLED)
#txtpayment.grid(row=2,column=0)

lblsubtotal= Label(F2Bottom,font=('arial',18,'bold'),text="Sub Total",bd=10,width=8,anchor='w')
lblsubtotal.grid(row=2,column=1)
txtsubtotal= Entry(F2Bottom,font=('arial',18,'bold'),textvariable=varsubtotal,width=6,justify='left',state=DISABLED)
txtsubtotal.grid(row=2,column=2)

lbltotal= Label(F2Bottom,font=('arial',18,'bold'),text="Total",bd=10,width=8,anchor='w')
lbltotal.grid(row=3,column=1)
txttotal= Entry(F2Bottom,font=('arial',18,'bold'),textvariable=vartotal,width=6,justify='left',state=DISABLED)
txttotal.grid(row=3,column=2)

#buttons
btntotal=Button(F2Bottom,padx=2,pady=1,bd=4,fg="Black",font=('arial',18,'bold'),width=5,text="Total",command=costofmeal).grid(row=2,column=0)
btnReset=Button(F2Bottom,padx=2,pady=1,bd=4,fg="Black",command=Reset,font=('arial',18,'bold'),width=5,text="Reset").grid(row=3,column=0)
btnExit=Button(F2Bottom,padx=2,pady=1,bd=4,fg="Black",command=qExit,font=('arial',18,'bold'),width=3,text="Exit").grid(row=0,column=1)
btnReceipt=Button(F2Bottom,padx=2,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Receipt",command=newwinreceipt).grid(row=2,column=4)
btn=Button(F1,padx=16,pady=2,bd=1,fg="black",font=('arial',16,'bold'),width=10,text="add",command=add).grid(row=10,column=0)
#btn=Button(F3,padx=16,pady=2,bd=1,fg="black",font=('arial',16,'bold'),width=10,text="orderdetails",command=order).grid(row=5,column=1)

lblSpace4=Label(F2Bottom,text="\n\n\n\n\n\n\n")
lblSpace4.grid(row=5,column=0)








root.mainloop()
