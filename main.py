from tkinter import *

############################ inicio do loop
# Janelas - Configurações
menu = Tk()

#menu.grid()
menu.title("Manutenção Carta Fabril")
menu.geometry("300x600")
#menu.resizable(width=0, height=0)

#Funções
def Proced():
    menu.withdraw()
    Proc = Tk()
    Proc.title("Manutenção Carta Fabril")
    Proc.geometry("300x600")

def voltar():
    Proc.destroy()
    menu.deiconify()

button = Button(Proc, text="Voltar", command=voltar)
button.pack()

def pag3():
    Proc.withdraw()
    pag_3 = Tk()
    pag_3.title("Manutenção Carta Fabril")
    pag_3.geometry("300x600")

button2 = Button(Proc, text="Pag3", command=pag3)
button2.pack()

# Definiçoes
canvas = Canvas(menu, width = 200, height = 200, background="red")      
img = PhotoImage(file="electrical.png")      
canvas.create_image(100,100, image=img) 
titulo1 = Label(menu, text="Manutenção", justify="center", font=("Arial", 20))
titulo2 = Label(menu, text="Carta Fabril", justify="center", font=("Arial", 16))
btproc = Button(menu, text="Procedimentos", padx=5, command=Proced)
btsug = Button(menu, text="Sugestões", padx=5)

# Chamando Layout
canvas.pack()
#canvas.place(relx=.5, rely=.5, anchor="center")
titulo1.pack()
titulo2.pack()
btproc.pack()
btsug.pack(padx=30, pady=30)

menu.mainloop()
############################ fim do loop