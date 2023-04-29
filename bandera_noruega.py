from tkinter import *
ventana_principal = Tk()
ventana_principal.title("Bandera noruega")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="red3")

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=90, height=500)
frame_entrada.place(x=200,y=0)
frame_b = Frame(ventana_principal)
frame_b.config(bg="white", width=800, height=90)
frame_b.place(x=0,y=200)
frame_c = Frame(ventana_principal)
frame_c.config(bg="blue4", width=50, height=500)
frame_c.place(x=220,y=0)
frame_d = Frame(ventana_principal)
frame_d.config(bg="blue4", width=800, height=50)
frame_d.place(x=0,y=220)




















ventana_principal.mainloop()