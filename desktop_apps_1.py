# se importa lalibreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox 

#----------------------
# funciones de la app
#----------------------
def calcular():
    messagebox.showinfo("Minicalculadora 1.0","Hizo click en el boton Calcular")
    s =int(a.get())+int(b.get())
    r = int(a.get())-int(b.get())
    m = int(a.get())*int(b.get())
    d = int(a.get())/int(b.get())
    mod = int(a.get())%int(b.get())
    de = int(a.get())//int(b.get())
    p = int(a.get())**int(b.get())
    
    t_resultados.insert(INSERT, f"{a.get()} + {b.get()} = {s}\n")
    t_resultados.insert(INSERT, f"{a.get()} - {b.get()} = {r}\n")
    t_resultados.insert(INSERT, f"{a.get()} * {b.get()} = {m}\n")
    t_resultados.insert(INSERT, f"{a.get()} / {b.get()} = {d}\n")
    t_resultados.insert(INSERT, f"{a.get()} % {b.get()} = {mod}\n")
    t_resultados.insert(INSERT, f"{a.get()} // {b.get()} = {de}\n")
    t_resultados.insert(INSERT, f"{a.get()} ** {b.get()} = {p}\n")

def borrar():
    messagebox.showinfo("Minicalculadora 1.0","Los datos serán borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Minicalculadora 1.0", "La app se cerrará")
    ventana_principal.destroy()


#----------------------
# ventana principal
#----------------------
# se declara una variable llamada ventana_principal , que adquiere las caracteristicas de un objeto tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

# tamaño de la ventana
ventana_principal.geometry("500x500")
# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)
# color de fondo de la ventana
ventana_principal.config(bg="dark green")
#------------------------------
# variables de control
#------------------------------
a = StringVar()
b= StringVar()
#------------------------------
# frame ntrada datos
#------------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="snow", width=480, height=180)
frame_entrada.place(x=10,y=10)

# logo de la app

logo = PhotoImage(file= "img/uis.png")
lb_logo = Label(frame_entrada, image=logo, bg = "snow")
lb_logo.place(x = 11,y = 40)

#etiqueta para titulo

lb_titulo = Label(frame_entrada, text= "Minicalculadora 1.0")
lb_titulo.config(bg="snow", fg="dark green", font=("Helvetica",20))
lb_titulo.place(x= 240, y= 10)

# etiqueta para el primer numero

lb_a = Label(frame_entrada , text="a : ")
lb_a.config(bg="snow", fg="dark green", font=("Helvetica",20))
lb_a.place(x = 250,y = 60 )

# caja de texto (entry) para el primer numer0

entry_a = Entry(frame_entrada, textvariable= a)
entry_a.config(bg = "snow", fg ="dark green", font=("courier",20))
entry_a.focus_set()
entry_a.place(x=290,y= 60, width=100 , height=30)

# etiqueta segundo numero

lb_b = Label(frame_entrada , text="b : ")
lb_b.config(bg="snow", fg="dark green", font=("Helvetica",20))
lb_b.place(x = 250,y = 100 )

# caja de texto (entry) para el segundo numer0

entry_b = Entry(frame_entrada, textvariable = b)
entry_b.config(bg = "snow", fg ="dark green", font=("courier",20))
entry_b.place(x=290,y= 100, width=100 , height=30)

#------------------------------
# frame operaciones
#------------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="snow", width=480, height=100)
frame_operaciones.place(x=10,y=200)
# boton calcular
button_a = Button(ventana_principal, text = "Calcular",command = calcular)
button_a.config(bg="snow3", fg="dark green", font =("Helvetica",10))
button_a.place(x = 45,y = 235, width=100 , height=35)
# boton borrar
button_b = Button(ventana_principal, text = "Borrar",command = borrar)
button_b.config(bg="snow3", fg="dark green", font =("Helvetica",10))
button_b.place(x = 190,y = 235, width=100 , height=35)
# boton salir 
button_c = Button(ventana_principal, text = "Salir",command = salir)

button_c.config(bg="snow3", fg="dark green", font =("Helvetica",10))
button_c.place(x = 335,y = 235, width=100 , height=35)

#------------------------------
# frame resultados
#------------------------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="snow", width=480, height=180)
frame_resultados.place(x=10,y=310)
# area de texto para resultados 
t_resultados = Text(frame_resultados)
t_resultados.config(bg = "snow3", fg ="dark green", font=("courier",20))
t_resultados.place(x = 10 , y = 10, width=460, height=160)
#run
# se ejecuta la funcion (metodo) mainloop de la clase Tk a traves de la instancia ventana_principal este metodo despliega una ventana simple 
# en la pantalla y queda a la espera de lo que el usuario haga, cada accion del usuario se conoce como evento. el mainloop es un bucle infinito
ventana_principal.mainloop()