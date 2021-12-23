import tkinter as tk

#######################################

def convert(a):
    if a.isdecimal():
        a = int(a)
    else: 
        a = None
    return a

def suma():
    cresultado.delete(0,tk.END)
    a = cajauno.get()
    a = convert(a)
    b = cajados.get()
    b = convert(b)
    try: 
        c = a + b
    except:
        c = "Error en datos"
    cresultado.insert(0,c)

def resta():
    cresultado.delete(0,tk.END)
    a = cajauno.get()
    a = convert(a)
    b = cajados.get()
    b = convert(b)
    try: 
        c = a - b
    except:
        c = "Error en datos"
    cresultado.insert(0,c)

def multiplicacion():
    cresultado.delete(0,tk.END)
    a = cajauno.get()
    a = convert(a)
    b = cajados.get()
    b = convert(b)
    try: 
        c = a * b
    except:
        c = "Error en datos"
    cresultado.insert(0,c)

def division():
    cresultado.delete(0,tk.END)
    a = cajauno.get()
    a = convert(a)
    b = cajados.get()
    b = convert(b)
    if b == 0:
        cresultado.insert(0,"¡Error! Dato 2 = 0")
    else:
        try: 
            c = a / b
        except:
            c = "Error en datos"
        cresultado.insert(0,c)


#######################################


ventana = tk.Tk()
ventana.config(width=300,height=300)
ventana.title("Calculadora")

euno = tk.Label(text="Dato 1:")
euno.place(x=20, y=30)
cajauno = tk.Entry()
cajauno.place(x=20,y=50)

edos = tk.Label(text="Dato 2:")
edos.place(x=160, y=30)
cajados = tk.Entry()
cajados.place(x=160, y=50)

bsuma = tk.Button(text = " + ", command=suma)
bsuma.place(x=20, y=100)

bresta = tk.Button(text = " - ", command=resta)
bresta.place(x=100, y=100)

bmultiplicacion = tk.Button(text = " * ", command=multiplicacion)
bmultiplicacion.place(x=180, y=100)

bdiv = tk.Button(text = " / ", command=division)
bdiv.place(x=260, y=100)

eres = tk.Label(text="Resultado: ")
eres.place(x=90, y=180)
cresultado = tk.Entry()
cresultado.place(x=90, y=200)

ventana.mainloop()