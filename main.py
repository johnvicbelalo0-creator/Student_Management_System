import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.title('Student Management System')

bg_color = '#273b7a'

login_student_icon = tk.PhotoImage(file='Img/login_student_img.png')
login_admin_icon = tk.PhotoImage(file='Img/admin_img.png')
add_student_icon = tk.PhotoImage(file='Img/add_student_img.png')
locked_icon = tk.PhotoImage(file='Img/locked.png')
unlocked_icon = tk.PhotoImage(file='Img/unlocked.png')

def welcome_page():

    # ---Welcome Page Frame---
    welcome_page_fm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

    heading_lb = tk.Label(welcome_page_fm, text= 'Welcome To \nStudent Management System', bg=bg_color, fg='white', font=('Bold', 18))
    heading_lb.place(x=0, y=0, width=400) 

    # ---Student Login Button---
    student_login_btn = tk.Button(welcome_page_fm, text='Login Student', bg=bg_color, fg='white', font=('Bold', 15), bd=0)
    student_login_btn.place(x=120, y=125, width=200)

    student_login_img = tk.Button(welcome_page_fm, image=login_student_icon, bd=0)
    student_login_img.place(x=60, y=100)


    # ---Admin Login Button---
    admin_login_btn = tk.Button(welcome_page_fm, text='Login Admin', bg=bg_color, fg='white', font=('Bold', 15), bd=0)
    admin_login_btn.place(x=120, y=225, width=200)

    admin_login_img = tk.Button(welcome_page_fm, image=login_admin_icon, bd=0)
    admin_login_img.place(x=60, y=200)


    # ---Student Create Button---
    add_student_btn = tk.Button(welcome_page_fm, text='Create Account', bg=bg_color, fg='white', font=('Bold', 15), bd=0)
    add_student_btn.place(x=120, y=325, width=200)

    add_student_img = tk.Button(welcome_page_fm, image=add_student_icon, bd=0)
    add_student_img.place(x=60, y=300)


    welcome_page_fm.pack(pady=30)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=400, height=420)

def student_login_page():

    def show_hide_password():

        if password_ent['show'] == '*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon)
        
        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon)

    # ---Student Login Page Frame---
    student_login_page_fm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

    heading_lb = tk.Label(student_login_page_fm, text= 'Student Login Page', bg=bg_color, fg='white', font=('Bold', 18))
    heading_lb.place(x=0, y=0, width=400) 

    # ---Student Login Icon---
    stud_icon_lb = tk.Label(student_login_page_fm, image=login_student_icon)
    stud_icon_lb.place(x=150, y=40)

    # ---Student ID Number Entry Box---
    id_number_lb = tk.Label(student_login_page_fm, text='Enter Student ID Number:', font=('Bold', 15), fg=bg_color)
    id_number_lb.place(x=80, y=140)

    id_number_ent = tk.Entry(student_login_page_fm, font=('Bold', 15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    id_number_ent.place(x=80, y=190)

    # ---Student Password Entry Box---
    password_lb = tk.Label(student_login_page_fm, text='Enter Password:', font=('Bold', 15), fg=bg_color)
    password_lb.place(x=80, y=240)

    password_ent = tk.Entry(student_login_page_fm, font=('Bold', 15), justify=tk.CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2, show='*')
    password_ent.place(x=80, y=290)

    show_hide_btn = tk.Button(student_login_page_fm, image=locked_icon, bd=0, command=show_hide_password)
    show_hide_btn.place(x=310, y=280)

    # ---Login Button---
    login_btn = tk.Button(student_login_page_fm, text='Login', font=('Bold', 15), bg=bg_color, fg='white')
    login_btn.place(x=95, y=340, width=200, height=40)

    # ---Forgot Password---
    forgot_password_btn = tk.Button(student_login_page_fm, text='Forgot Password', fg=bg_color, bd=0)
    forgot_password_btn.place(x=150, y=390)

    student_login_page_fm.pack(pady=30)
    student_login_page_fm.pack_propagate(False)
    student_login_page_fm.configure(width=400, height=450)


root.mainloop()
