
from prettytable import PrettyTable
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox


#------------Addmedicine---------
def new_page5(self):
      ro=Tk()
      ro.title("Pharmacy Managment system")
      ro.geometry("1550x1000+0+0") 
      ro.config(bg="black")
      back=Button(ro,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & ro.destroy()).place(x=9,y=720,width=100,height=50)
      f1=Frame(ro,bg="white",borderwidth=6,relief=SUNKEN)
      f1.place(x=480,y=30,height=550,width=500)
      title=Label(f1,text="Add New Medicine",font=("Arial",25,"bold"),fg="black",bg="white")
      title.place(x=30,y=30)
      medi=Label(f1,text="Medicine Name",font="Time 20 bold").place(x=90,y=140)
      price=Label(f1,text="Price",font="Time 20 bold").place(x=90,y=210)
      medicine_name=StringVar()
      price_name=StringVar()
      userEntry=Entry(f1,font="Time 20 bold",textvariable=medicine_name).place(x=90,y=180,width=350,height=35)
      passwEntry=Entry(f1,font="Time 20 bold",textvariable=price_name).place(x=90,y=260,width=350,height=35)



      #----------------------salary-------
      Quantity=Label(f1,text="Quantity",font="Time 20 bold").place(x=90,y=310)
      Type=Label(f1,text="Type",font="Time 20 bold").place(x=90,y=400)
      Quant=StringVar()
      global Date
      mt=StringVar()

      salentry=Entry(f1,font="Time 20 bold",textvariable=Quant).place(x=90,y=360,width=350,height=35)
      dateEntry=Entry(f1,font="Time 20 bold",textvariable=mt).place(x=90,y=450,width=350,height=35)
      subm=Button(ro,text="Submit",font=("arial",19,"bold"),bg="#8DB7EC",fg="black",height=4,width=50,command=lambda:submit_medicine(medicine_name.get(),price_name.get(),Quant.get(),mt.get()) & ro.destroy()).place(x=525,y=550,width=420,height=40)





#-----------Function of Add new ----- medicine
def submit_medicine(name,pric,quat,dos):
      file=open('medicine.txt','a')
      file.write(name +"," + pric+","+quat+","+dos+"\n")
      new_page3(self)
      file.close()







#-----------Sales record------------------#


def new_page7(self):
      root7=Tk()
      root7.title("Pharmacy Managment system")
      root7.geometry("1550x1000+0+0") 
      root7.config(bg="black")
      f=open('sales.txt','r')
      back=Button(root7,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root7.destroy()).place(x=9,y=720,width=100,height=50)
      x=PrettyTable()
      t=Text(root7)
      x.field_names = ["Medicine Name", "Rs", "Quantity", "Dose"]
      for  item  in f:
         a,b,c,d=item.strip().split(",")
         x.add_row([a, b,c,d])
      t.insert(INSERT,x)#Inserting table in text widget 
      t.pack()



# --------deleted mdicine-----------


def new_page8(self):
      root8=Tk()
      root8.title("Pharmacy Managment system")
      root8.geometry("1550x1000+0+0") 
      root8.config(bg="black")
      back=Button(root8,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root8.destroy()).place(x=9,y=720,width=100,height=50)
      f1=Frame(root8,bg="white",borderwidth=6,relief=SUNKEN)
      f1.place(x=480,y=30,height=550,width=500)
      title=Label(f1,text="Delete Medicine",font=("Arial",25,"bold"),fg="black",bg="white")
      title.place(x=30,y=30)
      user=Label(f1,text="Medicine Name",font="Time 20 bold").place(x=90,y=140)
      passwo=Label(f1,text="Price",font="Time 20 bold").place(x=90,y=210)
      me=StringVar()
      rs=StringVar()
      userEntry=Entry(f1,font="Time 20 bold",textvariable=me).place(x=90,y=180,width=350,height=35)
      passwEntry=Entry(f1,font="Time 20 bold",textvariable=rs).place(x=90,y=260,width=350,height=35)
      
     
      #----------------------salary-------
      qn=Label(f1,text="Quantity",font="Time 20 bold").place(x=90,y=310)
      d=Label(f1,text="Type",font="Time 20 bold").place(x=90,y=400)

      Q=StringVar()
      Ds=StringVar()

      salentry=Entry(f1,font="Time 20 bold",textvariable=Q).place(x=90,y=360,width=350,height=35)
      dateEntry=Entry(f1,font="Time 20 bold",textvariable=Ds).place(x=90,y=450,width=350,height=35)
      delet=Button(root8,text="Deleted",font=("arial",19,"bold"),bg="#8DB7EC",fg="black",height=4,width=50,command=lambda:de(me.get(),rs.get(),Q.get(),Ds.get()) & root8.destroy()).place(x=525,y=550,width=420,height=40)







#----------Deleted Function-------------





def de(nam,passwor,salry,da):
           with open("medicine.txt", "r") as file_input:
             with open("medicineempty.txt", "w") as output: 
              for line in file_input:
               if line.strip("\n") != nam+","+passwor+","+salry+","+da:
                output.write(line)
           new_page3(self)












#----------- Employ Details--------

def new_page9(self):
      root10=Tk()
      root10.title("Pharmacy Managment system")
      root10.geometry("1550x1000+0+0") 
      root10.config(bg="Black")
      f=open('empty.txt','r')
      back=Button(root10,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root10.destroy()).place(x=9,y=720,width=100,height=50)
      x=PrettyTable()
      t=Text(root10)
      x.field_names = ["Medicine Name", "Rs", "Quantity", "Dose"]
      for  item  in f:
         a,b,c,d=item.strip().split(",")
         x.add_row([a, b, c, d])
      t.insert(INSERT,x)#Inserting table in text widget 
      t.pack()





#-------------Add sales----------------------#






def Add_sales(self):
      root15=Tk()
      root15.title("Pharmacy Managment system")
      root15.geometry("1550x1000+0+0") 
      root15.config(bg="black")
      back=Button(root15,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root15.destroy()).place(x=9,y=720,width=100,height=50)
      f1=Frame(root15,bg="white",borderwidth=6,relief=SUNKEN)
      f1.place(x=480,y=30,height=550,width=500)
      title=Label(f1,text="Add New Medicine",font=("Arial",25,"bold"),fg="black",bg="white")
      title.place(x=30,y=30)
      medi=Label(f1,text="Enter date",font="Time 20 bold").place(x=90,y=140)
      price=Label(f1,text="Enter price",font="Time 20 bold").place(x=90,y=210)
      sale=StringVar()
      de=StringVar()
      userEntry=Entry(f1,font="Time 20 bold",textvariable=sale).place(x=90,y=180,width=350,height=35)
      passwEntry=Entry(f1,font="Time 20 bold",textvariable=de).place(x=90,y=260,width=350,height=35)



      #----------------------salary-------
      Quantity=Label(f1,text="Format",font="Time 20 bold").place(x=90,y=310)
      Type=Label(f1,text="Time",font="Time 20 bold").place(x=90,y=400)
      ca=StringVar()
      ti=StringVar()


      salentry=Entry(f1,font="Time 20 bold",textvariable=ca).place(x=90,y=360,width=350,height=35)
      dateEntry=Entry(f1,font="Time 20 bold",textvariable=ti).place(x=90,y=450,width=350,height=35)
      subm=Button(root15,text="Submit",font=("arial",19,"bold"),bg="#8DB7EC",fg="black",height=4,width=50,command=lambda:submit_sales(sale.get(),de.get(),ca.get(),ti.get()) & root15.destroy()).place(x=525,y=550,width=420,height=40)























#-----------Function of Add new ----- medicine
def submit_sales(name,pric,quat,dos):
      file=open('sales.txt','a')
      file.write(name +"," + pric+","+quat+","+dos+"\n")
      new_page3(self)
      file.close()






#-------Add Employ---------


def new_page10(self):
      root11=Tk()
      root11.title("Pharmacy Managment system")
      root11.geometry("1550x1000+0+0") 
      root11.config(bg="black")
      back=Button(root11,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root11.destroy()).place(x=9,y=720,width=100,height=50)
      f1=Frame(root11,bg="white",borderwidth=6,relief=SUNKEN)
      f1.place(x=480,y=30,height=550,width=500)
      title=Label(f1,text="Add New Employ",font=("Arial",25,"bold"),fg="black",bg="white")
      title.place(x=30,y=30)
      user=Label(f1,text="Employ Name",font="Time 20 bold").place(x=90,y=140)
      passwo=Label(f1,text="Password",font="Time 20 bold").place(x=90,y=210)
      na=StringVar()
      psd=StringVar()
      userEntry=Entry(f1,font="Time 20 bold",textvariable=na).place(x=90,y=180,width=350,height=35)
      passwEntry=Entry(f1,font="Time 20 bold",textvariable=psd).place(x=90,y=260,width=350,height=35)

      #----------------------salary-------
      salary=Label(f1,text="Salary",font="Time 20 bold").place(x=90,y=310)
      salary=Label(f1,text="Date of Joining",font="Time 20 bold").place(x=90,y=400)

      salary=StringVar()
      global Date
      Date=StringVar()

      salentry=Entry(f1,font="Time 20 bold",textvariable=salary).place(x=90,y=360,width=350,height=35)
      dateEntry=Entry(f1,font="Time 20 bold",textvariable=Date).place(x=90,y=450,width=350,height=35)
      subm=Button(root11,text="Submit",font=("arial",19,"bold"),bg="#8DB7EC",fg="black",height=4,width=50,command=lambda:submit(na.get(),psd.get(),salary.get(),Date.get()) & root11.destroy()).place(x=525,y=550,width=420,height=40)

##-------------Submit------
def submit(name,password,salary,date):
      file=open('empty.txt','a')
      file.write(name +"," + password +","+salary+","+date+"\n")
      new_page3(self)
      file.close()




def new_page16(self):
      root16=Tk()
      root16.title("Pharmacy Managment system")
      root16.geometry("1550x1000+0+0") 
      root16.config(bg="black")
      back=Button(root16,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root16.destroy()).place(x=9,y=720,width=100,height=50)
      f1=Frame(root16,bg="white",borderwidth=6,relief=SUNKEN)
      f1.place(x=480,y=30,height=550,width=500)
      title=Label(f1,text="update",font=("Arial",25,"bold"),fg="black",bg="white")
      title.place(x=30,y=30)
      medi=Label(f1,text="Enter name",font="Time 20 bold").place(x=90,y=140)
      price=Label(f1,text="Enter password",font="Time 20 bold").place(x=90,y=210)
      up=StringVar()
      ud=StringVar()
      userEntry=Entry(f1,font="Time 20 bold",textvariable=up).place(x=90,y=180,width=350,height=35)
      passwEntry=Entry(f1,font="Time 20 bold",textvariable=ud).place(x=90,y=260,width=350,height=35)

      #----------------------salary-------
      salary=Label(f1,text="Salary",font="Time 20 bold").place(x=90,y=310)
      salary=Label(f1,text="Date of Joining",font="Time 20 bold").place(x=90,y=400)

      us=StringVar()
      ue=StringVar()

      salentry=Entry(f1,font="Time 20 bold",textvariable=us).place(x=90,y=360,width=350,height=35)
      dateEntry=Entry(f1,font="Time 20 bold",textvariable=ue).place(x=90,y=450,width=350,height=35)
      subm=Button(root16,text="Submit",font=("arial",19,"bold"),bg="#8DB7EC",fg="black",height=4,width=50,command=lambda:update(up.get(),ud.get(),us.get(),ue.get()) & root16.destroy()).place(x=525,y=550,width=420,height=40)

def update(name,pas,sal,date):
      file=open('pra.txt','a')
      for item in file:
        a,b,c,d=item.strip().split(",")
        if a==name or b==pas or d==date:
              file.write(name +"," + pas +","+sal+","+date+"\n",'w')
        else:
              messagebox.showinfo("Alert","GO to Add employ section")
              new_page3(self)
             

      file.close()










#
# ''''''''''''''''deleted employ''''''''#
def new_page11(self):
      root12=Tk()
      root12.title("Pharmacy Managment system")
      root12.geometry("1550x1000+0+0") 
      root12.config(bg="black")
      back=Button(root12,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root12.destroy()).place(x=9,y=720,width=100,height=50)
      f1=Frame(root12,bg="white",borderwidth=6,relief=SUNKEN)
      f1.place(x=480,y=30,height=550,width=500)
      title=Label(f1,text="Delete Employ",font=("Arial",25,"bold"),fg="black",bg="white")
      title.place(x=30,y=30)
      user=Label(f1,text="Employ Name",font="Time 20 bold").place(x=90,y=140)
      passwo=Label(f1,text="Password",font="Time 20 bold").place(x=90,y=210)
      nam=StringVar()
      psdw=StringVar()
      userEntry=Entry(f1,font="Time 20 bold",textvariable=nam).place(x=90,y=180,width=350,height=35)
      passwEntry=Entry(f1,font="Time 20 bold",textvariable=psdw).place(x=90,y=260,width=350,height=35)
      
     
      #----------------------salary-------
      salary=Label(f1,text="Salary",font="Time 20 bold").place(x=90,y=310)
      d=Label(f1,text="Date of Joining",font="Time 20 bold").place(x=90,y=400)

      salar=StringVar()
      Dat=StringVar()

      salentry=Entry(f1,font="Time 20 bold",textvariable=salar).place(x=90,y=360,width=350,height=35)
      dateEntry=Entry(f1,font="Time 20 bold",textvariable=Dat).place(x=90,y=450,width=350,height=35)
      delete=Button(root12,text="Deleted",font=("arial",19,"bold"),bg="#8DB7EC",fg="black",height=4,width=50,command=lambda:deleted(nam.get(),psdw.get(),salar.get(),Dat.get()) & root12.destroy()).place(x=525,y=550,width=420,height=40)


#----------Deleted Function-------------





def deleted(nam,passwor,salry,da):
           with open("pra.txt", "r") as file_input:
             with open("empty.txt", "w") as output: 
              for line in file_input:
               if line.strip("\n") != nam+","+passwor+","+salry+","+da:
                output.write(line)
           new_page3(self)





#"'''''''''''''''''''medicine stock page'''-------------

def new_page12(self):
      root11=Tk()
      root11.title("Pharmacy Managment system")
      root11.geometry("1550x1000+0+0") 
      root11.config(bg="black")
      f = open('medicine.txt', 'r')
      x=PrettyTable()
      t=Text(root11)
      back=Button(root11,text="Back",font=("arial",18,"bold"),bg="white",fg="black",height=1,width=3,command=lambda:new_page2(self) & root11.destroy()).place(x=9,y=720,width=100,height=50)
      x.field_names = ["Medicine Name", "Rs", "Quantity", "Dose"]
      for  item  in f:
         a,b,c,d=item.strip().split(",")
         x.add_row([a, b, c, d])
      t.insert(INSERT,x)#Inserting table in text widget 
      t.pack()






#-----------Admin-------loginarea-----------






def login(usernam,password):
    result = 0
    f = open('abc.txt', 'r')
    for item in f:
       a,b,c = item.split(",")
       if (a == usernam and b == password):
           result = 1
           break
    f.close()
    if result == 1:
        roo = Tk()
        roo.geometry("1550x1000+0+0")
        roo.title("Pharmacy Managment system")
        Frame_login=Frame(roo,bg="#003399",borderwidth=4,relief=SUNKEN)
        Frame_login.place(x=500,y=200,height=500,width=500)
        title=Label(roo,text ="Admin Authority",fg="#003399",bg="black",font =("arial",30," bold")).place(x=0,y=0,width=1600,height=100)
        btn2=Button(Frame_login,text="Add Medicine",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page5(roo) & roo.destroy()).place(x=120,y=40,width=200,height=50)
        btn2=Button(Frame_login,text="Deleted Medicine",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page8(roo) & roo.destroy()).place(x=120,y=100,width=200,height=50)
        btn2=Button(Frame_login,text="Employ Details",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page9(roo) & roo.destroy()).place(x=120,y=170,width=200,height=50)
        btn2=Button(Frame_login,text="Add Employ ",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page10(roo) & roo.destroy()).place(x=120,y=230,width=200,height=50)
        btn2=Button(Frame_login,text="Deleted Employ ",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page11(roo) & roo.destroy()).place(x=120,y=300,width=200,height=50)
        btn2=Button(Frame_login,text="Medicine stock ",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page12(roo) & roo.destroy()).place(x=120,y=370,width=200,height=50)
        btn2=Button(roo,text="Sales Record ",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page7(roo) & roo.destroy()).place(x=0,y=170,width=200,height=50)
        btn2=Button(roo,text="Add Sales",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : Add_sales(roo) & roo.destroy()).place(x=0,y=240,width=200,height=50)
    else:
        messagebox.showinfo("Alert!","Username or password you entered is not valid")
        new_page2(self)


#--------------Employ Login------------





def login2(user,pas):
    result=0
    f = open('empty.txt', 'r')
    for item in f:
        a,b,c,d=item.strip().split(",")
        if (a==user and b==pas):
           result = 1
           break
    f.close()
    if result==1:
        root9=Tk()
        root9.title("Pharmacy Managment system")
        root9.geometry("1550x1000+0+0")
        Frame_login=Frame(root9,bg="#003399",borderwidth=4,relief=SUNKEN)
        Frame_login.place(x=500,y=200,height=400,width=500)
        title=Label(root9,text ="Admin Authority",fg="#003399",bg="black",font =("arial",30," bold")).place(x=0,y=0,width=1600,height=100)
        title1=Label(Frame_login,text="Name :",font=("arial",15,"bold"),bg="#003399",fg="black").place(x=50,y=70)
        name=Label(Frame_login,text=a,font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=150,y=70)
        title2=Label(Frame_login,text="Password :",font=("arial",15,"bold"),bg="#003399",fg="Black").place(x=50,y=100)
        pas=Label(Frame_login,text=b,font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=160,y=100)
        title3=Label(Frame_login,text="salary :",font=("arial",15,"bold"),bg="#003399",fg="black").place(x=50,y=130)
        salary=Label(Frame_login,text=c,font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=160,y=130)
        title4=Label(Frame_login,text="Date of Joining :",font=("arial",15,"bold"),bg="#003399",fg="black").place(x=50,y=200)
        date=Label(Frame_login,text=d,font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=230,y=200)
       
    else:
             messagebox.showinfo("Alert!","Error Try Again")
             new_page2(self)



#-------------Admin Details-----------







def new_page3(self):
      root3=Tk()
      root3.title("Pharmacy Managment system")
      root3.geometry("1550x1000+0+0")
      Frame_login=Frame(root3,bg="#003399",borderwidth=4,relief=SUNKEN)
      Frame_login.place(x=500,y=200,height=400,width=500)
      title=Label(Frame_login,text="Admin Details",font=("Impact",30,"bold"),bg="#003399",fg="black").place(x=50,y=30)
      user_name=Label(Frame_login,text="Username",font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=50,y=100)
      user=StringVar()
      name=Entry(Frame_login,font=("arial",15,"bold"),bg="lightgray",textvariable=user).place(x=170,y=100,width=250,height=35)
      pass_name=Label(Frame_login,text="Password",font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=50,y=200)
      passs=StringVar()
      pas=Entry(Frame_login,font=("arial",15,"bold"),bg="lightgray",textvariable=passs).place(x=170,y=200,width=250,height=35)
      forget=Button(Frame_login,text="Admin Area",bg="#003399",fg="black",font=("arial",15,"bold"),bd=0,command=lambda : login(user.get(),passs.get())& root3.destroy()).place(x=150,y=280)
     




#__________Employ Details______________







def new_page4(self):
      root2=Tk()
      root2.title("Pharmacy Managment system")
      root2.geometry("1550x1000+0+0")
      Frame_login=Frame(root2,bg="#003399",borderwidth=4,relief=SUNKEN)
      Frame_login.place(x=500,y=200,height=400,width=500)
      title=Label(Frame_login,text="Employee Details",font=("Impact",30,"bold"),bg="#003399",fg="black").place(x=50,y=30)
      user_name=Label(Frame_login,text="Username",font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=50,y=100)
      use=StringVar()
      nam=Entry(Frame_login,font=("arial",15,"bold"),bg="lightgray",textvariable=use).place(x=170,y=100,width=250,height=35)
      pass_nam=Label(Frame_login,text="Password",font=("arial",15,"bold"),bg="#003399",fg="gray").place(x=50,y=200)
      pa=StringVar()
      pos=Entry(Frame_login,font=("arial",15,"bold"),bg="lightgray",textvariable=pa).place(x=170,y=200,width=250,height=35)
      forget=Button(Frame_login,text="Click  Here",bg="#003399",fg="black",font=("arial",15,"bold"),bd=0,command=lambda : login2(use.get(),pa.get())& root2.destroy()).place(x=150,y=280)
     





#_____________LOgin Area_______________






def new_page2(self):
    root1=Tk()
    root1.geometry("1550x800+0+0")
    root1.minsize(200,100)
    root1.maxsize(1550,1000)
    root1.title("Login system")
    root1.configure(bg="#00e6e6")
    frame=Frame(root1,bg="#003399",borderwidth=4,relief=SUNKEN)
    frame.place(x=500,y=200,height=400,width=500)
    
    title=Label(frame,text="Login Here",fg="#99bbff",bg="#003399",font=("impact",35, "bold")).place(x=130,y=30)
    sta=Label(frame,text=' "Login According To Your Status" ',fg="#99bbff",bg="#003399",font=("arial" ,15 ,"bold")).place(x=80,y=100)
    des_1=Label(frame,text="If you are  Admin then click admin login icon.",bg="#003399",fg="#99bbff",font=("arial",12,"bold")).place(x=80,y=150)
    btn1=Button(frame,text="ADMIN LOGIN AREA",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page3(self) & root1.destroy()).place(x=120,y=200,width=200,height=50)
    des_2=Label(frame,text="If you are  Employee  then click Employ login icon.",bg="#003399",fg="#99bbff",font=("arial",12,"bold")).place(x=80,y=270)
    btn2=Button(frame,text="EMPLOYEE LOGIN AREA",fg="white",bg="black",borderwidth=4,relief=SUNKEN,height=6,width=20,
                command=lambda : new_page4(self) & root1.destroy()).place(x=120,y=320,width=200,height=50)
    back_1=Button(root1,text="BACK",fg="white",bg="black",borderwidth=4,font=("arial",15,"bold"),relief=SUNKEN,height=6,width=20,
                  command=lambda : page1(self) & root1.destroy()).place(x=5,y=730,width=200,height=50)




#---------------mainpage-------------

















































































































   
def page1(self):
      root=Tk()
      root.geometry("1550x800+0+0")
      root.minsize(200,100)
      root.maxsize(1550,1000)
      image=Image.open("pic.jpg")
      image=image.resize((1550,800),Image.ANTIALIAS)
      photo=ImageTk.PhotoImage(image)
      label=Label(root,image=photo)
      label.place(x=0,y=0,relheight=1,relwidth=1)  
      my_button=Button(root,
               text="Get started",
               font=("arial 20 bold"),
               fg="white",
               bg="black",
               height=4,
               width=30,
               command=lambda : new_page2(self) & root.destroy()).place(x=1190,y=750,width=400,height=60)
      root.mainloop()



app=page1(Tk)
