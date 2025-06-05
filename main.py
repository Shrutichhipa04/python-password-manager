from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    passw = "".join(password_list)
    input_pass.insert(0,passw)
    pyperclip.copy(passw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_save = input_website.get()
    email_save = input_email.get()
    password_save = input_pass.get()
    new_data = {
        website_save:{
            "email": email_save,
            "password": password_save,
        }
    }
    if len(website_save)==0 or len(password_save)==0 and len(email_save)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"These are the details entered: \nEmail: {email_save}\nPassword: {password_save}\nIs it ok to save")
        if is_ok:
            try:
                with open(".json", "r") as file :
                    data = json.load(file)
            except FileNotFoundError:
                with open("myfile.json", "w") as file :
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                with open("myfile.json", "w") as file:
                    json.dump(data,file,indent=4)
            finally:
                input_website.delete(0,END)
                input_pass.delete(0,END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_data():
    website_save = input_website.get()
    try:
        with open("myfile.json", "r") as file :
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website_save in data:
            email_save = data[website_save]["email"]
            password_save = data[website_save]["password"]
            messagebox.showinfo(title=website_save,message=f"email: {email_save}\npassword: {password_save}")
        else:
            messagebox.showinfo(title="Error",message=f"No Data for {website_save} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager") 
window.config(padx=50,pady=50)

canvas = Canvas(width=160,height=200)
img =  PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website = Label(text="Website:")
website.grid(column=0,row=1)
email = Label(text="Email/Username:")
email.grid(column=0,row=2)
password = Label(text="Password:")
password.grid(column=0,row=3)

add_button= Button(text="Add",width=37,command=save)
add_button.grid(column=1,row=4,columnspan=2)
passbutton = Button(text="Generate Password",width=14,command=generate_password)
passbutton.grid(column=2,row=3)
search_button = Button(text="Search",width=14,command=search_data)
search_button.grid(column=2,row=1)

input_website = Entry(width=26)
input_website.grid(column=1,row=1)
input_website.focus()
input_email = Entry(width=44)
input_email.grid(column=1,row=2,columnspan=2)
input_email.insert(0,"xyz@gmail.com")
input_pass = Entry(width=26)
input_pass.grid(column=1,row=3)

window.mainloop()