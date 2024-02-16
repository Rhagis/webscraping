from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)
    
def borrar():
    visor_calculadora.delete(0,END)
    global operador
    operador = ""
    
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0, resultado)
    operador = ""

def revisar_check():
    x = 0
    for c in cuadros_comidas:
        if variable_comida[x].get() == 1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get() == '0':
                cuadros_comidas[x].delete(0,END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_bebidas:
        if variable_bebida[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_postres:
        if variable_postre[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total *0.07
    total = sub_total + impuestos
    
    var_costo_comida.set(f'${round(sub_total_comida,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)}')
    var_costo_postres.set(f'${round(sub_total_postre,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuesto.set(f'${round(impuestos,2)}')
    var_total.set(f'${round(total,2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N° - {random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 57 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f"-"*65 + '\n')
    
    
    x=0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get())*precios_comida[x]}\n")
        x +=1
    x=0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f"{lista_bebida[x]}\t\t{bebida.get()}\t${int(bebida.get())*precios_bebida[x]}\n")
        x +=1
    x=0
    for postres in texto_postre:
        if postres.get() != '0':
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t${int(postres.get())*precios_postres[x]}\n")
        x +=1
    texto_recibo.insert(END, f"*" * 57 + '\n')
    texto_recibo.insert(END, f"Costo de la comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo del postre: \t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(END, f"*" * 57 + '\n')
    texto_recibo.insert(END, f"Sub-total: \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos: \t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 57 + '\n')
    texto_recibo.insert(END, "Lo esperamos pronto")

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')
    

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set(0)
    for texto in texto_bebida:
        texto.set(0)
    for texto in texto_postre:
        texto.set(0)
        
    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
        
    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postre:
        v.set(0)
    
    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")
#iniciar tkinter
aplicacion = Tk()

#Tamaño pantalla
aplicacion.geometry('1280x800+0+0')

#evitar maximizar
aplicacion.resizable(0,0)

#titulo ventana
aplicacion.title("Mi Restaurante - Sistema de facturación")

#color Fondo
aplicacion.config(bg='burlywood')


#Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)


#Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg="azure4",
                        font=("Dosis", 50), bg="burlywood", width=27)
etiqueta_titulo.grid(row=0,column=0)

#Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4',padx=80)
panel_costo.pack(side=BOTTOM)

#panel comida
panel_comida = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis",19,"bold"),
                          bd=1, relief=FLAT, fg="azure4")
panel_comida.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis",19,"bold"),
                          bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis",19,"bold"),
                          bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_botones.pack()


#lista productos
lista_comidas=['pollo','cordero', 'pescado', 'salmon', 'pizza1', 'pizza2','pizza3', 'pizza4']
lista_bebida = ['cola', 'lima limon', 'naranja','fernet','cerveza1', 'cerveza2', 'vino1', 'vino2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'gelatina','pastel1', 'pastel2','budin']

variable_comida = []
cuadros_comidas = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    #crear checkbutton
    variable_comida.append("")
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comida, text=comida.title(), font=("Dosis", 19,"bold"),
                         onvalue=1,offvalue=0, variable=variable_comida[contador],command=revisar_check)
    comida.grid(row=contador,column=0,sticky=W)
    
    #crear los cuadros de entrada
    cuadros_comidas.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set(0)
    cuadros_comidas[contador] = Entry(panel_comida,font=('Dosis',18,'bold'), bd=1,width=6,
                                      state=DISABLED, textvariable=texto_comida[contador])
    
    cuadros_comidas[contador].grid(row=contador, column=1) 
    
    contador +=1
    
variable_bebida = []
cuadros_bebidas = []
texto_bebida = []
contador = 0
for bebida in lista_bebida:
    variable_bebida.append("")
    variable_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Dosis", 19,"bold"),
                         onvalue=1,offvalue=0, variable=variable_bebida[contador],command=revisar_check)
    bebida.grid(row=contador,column=0,sticky=W)
    
    
    cuadros_bebidas.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set(0)
    cuadros_bebidas[contador] = Entry(panel_bebidas,font=('Dosis',18,'bold'), bd=1,width=6,
                                      state=DISABLED, textvariable=texto_bebida[contador])
    
    cuadros_bebidas[contador].grid(row=contador, column=1) 
    contador +=1

variable_postre = []
cuadros_postres = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variable_postre.append("")
    variable_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=("Dosis", 19,"bold"),
                         onvalue=1,offvalue=0, variable=variable_postre[contador],command=revisar_check)
    postre.grid(row=contador,column=0,sticky=W)
    
    
    cuadros_postres.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set(0)
    cuadros_postres[contador] = Entry(panel_postres,font=('Dosis',18,'bold'), bd=1,width=6,
                                      state=DISABLED, textvariable=texto_postre[contador])
    
    cuadros_postres[contador].grid(row=contador, column=1) 
    contador +=1
    
#etiqueta y campo de entrada panel costo
etiqueta_costo_comida = Label(panel_costo,
                              text="Costo Comida",
                              font=("Dosis",12,'bold'),
                              bg='azure4',
                              fg="white")
etiqueta_costo_comida.grid(row=0,column=0)
#variables
var_costo_comida = StringVar()
texto_costo_comida = Entry(panel_costo,
                           font=("Dosis",12,'bold'),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)


#etiqueta y campo de entrada panel costo
etiqueta_costo_bebida = Label(panel_costo,
                              text="Costo Bebida",
                              font=("Dosis",12,'bold'),
                              bg='azure4',
                              fg="white")
etiqueta_costo_bebida.grid(row=1,column=0)
#variables
var_costo_bebida = StringVar()
texto_costo_bebida = Entry(panel_costo,
                           font=("Dosis",12,'bold'),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)


#etiqueta y campo de entrada panel costo
etiqueta_costo_postres = Label(panel_costo,
                              text="Costo Postres",
                              font=("Dosis",12,'bold'),
                              bg='azure4',
                              fg="white")
etiqueta_costo_postres.grid(row=2,column=0)
#variables
var_costo_postres = StringVar()
texto_costo_postres = Entry(panel_costo,
                           font=("Dosis",12,'bold'),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1,padx=41)

var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#etiqueta y campo de entrada panel costo
etiqueta_subtotal = Label(panel_costo,
                              text="Subtotal",
                              font=("Dosis",12,'bold'),
                              bg='azure4',
                              fg="white")
etiqueta_subtotal.grid(row=0,column=2)
#variables
var_subtotal = StringVar()
texto_subtotal = Entry(panel_costo,
                           font=("Dosis",12,'bold'),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)

#etiqueta y campo de entrada panel costo
etiqueta_impuesto = Label(panel_costo,
                              text="Impuesto",
                              font=("Dosis",12,'bold'),
                              bg='azure4',
                              fg="white")
etiqueta_impuesto.grid(row=1,column=2)
#variables
var_impuesto = StringVar()
texto_impuesto = Entry(panel_costo,
                           font=("Dosis",12,'bold'),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3,padx=41)

#etiqueta y campo de entrada panel costo
etiqueta_total = Label(panel_costo,
                              text="Total",
                              font=("Dosis",12,'bold'),
                              bg='azure4',
                              fg="white")
etiqueta_total.grid(row=2,column=2)
#variables
var_total = StringVar()
texto_total = Entry(panel_costo,
                           font=("Dosis",12,'bold'),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_total)
texto_total.grid(row=2,column=3,padx=41)

#botones

botones =['total','recibo','guardar','resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis",14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
#area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',15,'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,column=0)

#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("Dosis",16,'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4)

lista_botones_calculadora =['7','8','9','+',
                            '4','5','6','-',
                            '1','2','3','x',
                            'CE','Borrar','0','/']
botones_guardados = []
fila = 1
columnas = 0
for boton in lista_botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',15,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,column=columnas)
    if columnas == 3:
        fila += 1
    columnas += 1
    
    if columnas == 4:
        columnas = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))
botones_guardados[13].config(command=borrar)
botones_guardados[12].config(command=obtener_resultado)

#evitar que la pantalla se cierre
aplicacion.mainloop()