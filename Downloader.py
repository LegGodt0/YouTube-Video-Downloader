from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
    enlace=videos.get()
    video = YouTube(enlace, use_oauth=True, allow_oauth_cache=True)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup(): #Para crear barra
	MessageBox.showinfo("Sobre mí","Programa creado por LegGodt#1549, para más información contactar a través de Discord")


#Ventana del script
root = Tk() #Crear ventana
root.config(bd=15) #Borde o Margen
root.title("Programa de prueba para descargar videos") #Título

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0) 
foto.grid(row=0, column=0) #Posición de la imagen en la fila 0 y columna 0
#Fin ventana

#Creando menú
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)
#Fin menú

#Instrucciones
instrucciones = Label(root, text="Programa creado para descargar videos de YouTube,\n seleccionar calidad:")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

#Limpiar entrada de url
def clear_text():
    videos.delete(0, "end")

botonreinicio = Button(root, text="Reiniciar", command=clear_text)
botonreinicio.grid(row=7,column=1)
#Fin limpieza

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)



root.mainloop()