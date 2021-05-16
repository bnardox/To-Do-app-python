from tkinter import *

#Definindo app
app = Tk()
app.title("To do")
app.configure(width = 300, height=450, bg='#262933')
app.resizable(False, False)
tasks = list()
cont = 10

#Definindo input
task = Entry(app)
task.place(x = 65, y = 405, width=150, height=20)

#Definindo ListBox
list = Listbox(app)
list.place(x = 65, y = 10, height = 300)
list.config(bg='#22242D', foreground='#fff')

#Função para enviar os dados para a ListBox
def print_task():
    t = task.get()
    tasks.append(t)
    for t in tasks:
        list.insert(END, t)
    tasks.clear()
    task.delete(0, END)
    

#Definindo botão de enviar dados
button = Button(app, text='OK', command=print_task)
button.place(x = 240, y = 400, width = 40, height = 30)

app.mainloop()