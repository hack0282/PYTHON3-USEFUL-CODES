#step1:importing needed for project

from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
import mysql.connector

#step2:creating a main wondow
path1="C:/Drive F/Rohith/Softwares/icons/v_avatar.ico"
root = Tk()
root.title("CUSTOMER ACCESS")
root.iconbitmap(path1)
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#METHODS
#step7: creating a Database logic and button logic
def Database():
    global conn, cursor, user_id, username, password
    conn = mysql.connector.connect(user="username", password="password", database="order_management")
    cursor = conn.cursor()

def Login(event=None):
    if USERNAME.get() == "" and PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        sql = "select password from users where username=%s"
        cursor.execute(sql, (USERNAME.get(),))
        usr = cursor.fetchone()
        if usr is not None:
            sql = "select username from users where password=%s"
            cursor.execute(sql, (PASSWORD.get(),))
            passwd = cursor.fetchone()
            if passwd is not None:
                showinfo("successfully logged in", "welcome to customer portal")
                HomeWindow()
                USERNAME.set('')
                PASSWORD.set('')
            else:
                lbl_text.config(text="Invalid Password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        else:
            lbl_text.config(text="Invalid Username", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close()

#method for when login is valid opening new window saying successfully logged in
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Logged in!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

#method for button back like exit button
def Back():
    Home.destroy()
    root.deiconify()

#creating a variables
USERNAME=StringVar()
PASSWORD=StringVar()

#step3: creating a frames
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#step4: creating a LABELS
lbl_title = Label(Top, text="Python: Simple Login Application", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_usrname = Label(Form, text="Username:", font=('arial', 14), bd=15)
lbl_usrname.grid(row=0, sticky="e")
lbl_passwd = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_passwd.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#step5: Creating a Entry widgets
en_username = Entry(Form, textvariable=USERNAME,font=(14))
en_username.grid(row=0,column=1)
en_password = Entry(Form,textvariable=PASSWORD, show="*", font=(14))
en_password.grid(row=1, column=1)

#step6: Button Widgets
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

#step10:running in loop the whole code
root.mainloop()



