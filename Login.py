import tkinter
import vault

root = tkinter.Tk()
root.title('Login')

root.geometry('350x100')

uvar = tkinter.StringVar()
passvar = tkinter.StringVar()

def submit():
    root.destroy()
    uname = uvar.get()
    password = passvar.get()
    print(vault.authenticate(uname,password))



tkinter.Label(root, text='Enter your Username').grid(column=0, row=1)
tkinter.Entry(root, textvariable=uvar).grid(column=1, row=1)

tkinter.Label(root, text='Enter your password').grid(column=0, row=2)
tkinter.Entry(root, textvariable=passvar, show='*').grid(column=1, row=2)

tkinter.Button(root, text='Button', command=submit).grid(column=1, row=3)
root.mainloop()