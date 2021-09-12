from tkinter import *
from functools import *
from tkinter import messagebox

root = Tk()
root.title("RESISTENCIAS EN SERIE O PARALELO")
root.geometry("1200x500")
varOpcion = IntVar()
states = []
one = 0
two = 0
three = 0
four = 0
nre = StringVar()
res = IntVar()
var = DoubleVar()
vi = int()
rt = float()
rr = float()
s = IntVar()
n = IntVar()
ciclo = int(res.get())
varuno = IntVar()
vardos = IntVar()
fac = IntVar()
tole = IntVar()


# -----------------------IMPRIMIR SERIE O PARALELO-----------------------------------------------------------------
def imprimir():
    if varOpcion.get() == 1:
        etiqueta.config(text="HAS ELEGIDO PARALELO")
    else:
        etiqueta.config(text="HAS ELEGIDO SERIE")


# -----------------------IMPRIMIR BANDA UNO-----------------------------------------------------------------------------
def imprimiruno():
    if varuno.get() == 1:  # negro
        one = 0
    elif varuno.get() == 2:  # marron
        one = 10
    elif varuno.get() == 3:  # rojo
        one = 20
    elif varuno.get() == 4:  # naranja
        one = 30
    elif varuno.get() == 5:  # amarillo
        one = 40
    elif varuno.get() == 6:  # verde
        one = 50
    elif varuno.get() == 7:  # azul
        one = 60
    elif varuno.get() == 8:  # violeta
        one = 70
    elif varuno.get() == 9:  # gris
        one = 80
    elif varuno.get() == 10:  # blanco
        one = 90
    return one


# -----------------------IMPRIMIR BANDA UNO-----------------------------------------------------------------------------
def imprimirdos():
    if vardos.get() == 1:  # negro
        two = 0
    elif vardos.get() == 2:  # marron
        two = 1
    elif vardos.get() == 3:  # rojo
        two = 2
    elif vardos.get() == 4:  # naranja
        two = 3
    elif vardos.get() == 5:  # amarillo
        two = 4
    elif vardos.get() == 6:  # verde
        two = 5
    elif vardos.get() == 7:  # azul
        two = 6
    elif vardos.get() == 8:  # violeta
        two = 7
    elif vardos.get() == 9:  # gris
        two = 8
    elif vardos.get() == 10:  # blanco
        two = 9
    return two


# -----------------------IMPRIMIR BANDA UNO-----------------------------------------------------------------------------
def imprimirfactor():
    if fac.get() == 1:  # negro
        three = 1
    elif fac.get() == 2:  # marron
        three = 10
    elif fac.get() == 3:  # rojo
        three = 100
    elif fac.get() == 4:  # naranja
        three = 1000
    elif fac.get() == 5:  # amarillo
        three = 10000
    elif fac.get() == 6:  # verde
        three = 100000
    elif fac.get() == 7:  # azul
        three = 1000000
    elif fac.get() == 8:  # oro
        three = 0.1
    elif fac.get() == 9:  # plata
        three = 0.01
    return three


# -----------------------IMPRIMIR BANDA UNO-----------------------------------------------------------------------------
def imprimirtolerancia():
    if tole.get() == 1:  # marron
        four = 1
    elif tole.get() == 2:  # rojo
        four = 2
    elif tole.get() == 3:  # oro
        four = 5
    elif tole.get() == 4:  # plata
        four = 10
    elif tole.get() == 5:  # nada
        four = 20
    return four


# ---------------------IMPRIMIR NUMERO DE RESISTENCIAS------------------------------------------------------------------
def call_result(etiqueta_2, nnn):
    res = int(nnn.get())
    etiqueta_2.config(text="RESISTENCIAS = %d" % res)
    return


def totalfinal():
    i = 0
    if i <= ciclo:
        while i <= ciclo:  # Comienzo del programa
            num1 = imprimiruno()
            num2 = imprimirdos()
            facto = imprimirfactor()
            tolerancia = imprimirtolerancia()
            res1 = num1 + num2
            res2 = res1 * facto
            # -----comiendo de la calsificacion-----------------------
            if res2 <= 990:
                resf = str(res2)
                tolf = str(tolerancia)
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s ohmios +- %s" % (resf, tolf))
            elif res2 == 1000 or res2 == 2000 or res2 == 3000 or res2 == 4000 or res2 == 5000 or res2 == 6000 or res2 == 7000 or res2 == 8000 or res2 == 9000:
                tolf = str(tolerancia)
                num = res2 / 1000
                num2 = str(num)
                resf = num2 + "K"
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif (res2 >= 1100 and res2 <= 1900) or (res2 >= 2100 and res2 <= 2900) or (
                    res2 >= 3100 and res2 <= 3900) or (res2 >= 4100 and res2 <= 4900) or (
                    res2 >= 5100 and res2 <= 5900) or (res2 >= 6100 and res2 <= 6900) or (
                    res2 >= 7100 and res2 <= 7900) or (res2 >= 8100 and res2 <= 8900) or (
                    res2 >= 9100 and res2 <= 9900):
                tolf = str(tolerancia)
                num = str(res2)
                resf = num[0] + "K" + num[1]
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif res2 >= 10000 and res2 <= 99000:
                tolf = str(tolerancia)
                num = str(res2)
                resf = num[0] + num[1] + "K"
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif res2 >= 100000 and res2 <= 990000:
                tolf = str(tolerancia)
                num = str(res2)
                resf = num[0] + num[1] + num[2] + "K"
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif res2 == 1000000 or res2 == 2000000 or res2 == 3000000 or res2 == 4000000 or res2 == 5000000 or res2 == 6000000 or res2 == 7000000 or res2 == 8000000 or res2 == 9000000:
                tolf = str(tolerancia)
                num = res2 / 1000000
                num2 = str(num)
                resf = num2 + "M"
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif (res2 >= 1100000 and res2 <= 1900000) or (res2 >= 2100000 and res2 <= 2900000) or (
                    res2 >= 3100000 and res2 <= 3900000) or (res2 >= 4100000 and res2 <= 4900000) or (
                    res2 >= 5100000 and res2 <= 5900000) or (res2 >= 6100000 and res2 <= 6900000) or (
                    res2 >= 7100000 and res2 <= 7900000) or (res2 >= 8100000 and res2 <= 8900000) or (
                    res2 >= 9100000 and res2 <= 9900000):
                tolf = str(tolerancia)
                num = str(res2)
                resf = num[0] + "M" + num[1]
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif res2 >= 10000000 and res2 <= 99000000:
                tolf = str(tolerancia)
                num = str(res2)
                resf = num[0] + num[1] + "M"
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            elif res2 >= 100000000 and res2 <= 990000000:
                tolf = str(tolerancia)
                num = str(res2)
                resf = num[0] + num[1] + num[2] + "M"
                messagebox.showinfo("hola", "La resistencia tiene un valor de %s +- %s" % (resf, tolf))
            print("Pulse 0 para volver a calcular otra resistencia")
            print("Pulse 1 para salir")
            op = input('> ')
            if op == 0:
                continue
            quit()


# ---------------------SELECCION ENTRE PARALELO O EN SERIE-------------------------------------------------------------
Radiobutton(root, text="PARALELO", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="SERIE", variable=varOpcion, value=2, command=imprimir).pack()
etiqueta = Label(root)
etiqueta.pack()
# -----------------------INTRODUCCION DE RESISTENCIAS-------------------------------------------------------------------
nr = Label(root, text="INTRODUCE EL NUMERO DE RESISTENCIAS").pack()
n = Entry(root, textvariable=nre).pack()

etiqueta2 = Label(root)
etiqueta2.pack()
call_result = partial(call_result, etiqueta2, nre)  # se manda los parametros a la funcion
enviarvalor = Button(root, text="ACEPTAR VALOR",
                     command=call_result).pack()  # boton que imprime y manda el parametro en la pantalla

# ----------------------BANDAS UNO--------------------------------------------------------------------------------------
nbu = Label(root, text="SELECCIONA EL COLOR DE LA BANDA UNO").place(x=60, y=170)
Radiobutton(root, text="NEGRO", fg="black", variable=varuno, value=1, command=imprimiruno).place(x=60, y=190)
Radiobutton(root, text="MARRON", fg="brown", variable=varuno, value=2, command=imprimiruno).place(x=60, y=210)
Radiobutton(root, text="ROJO", fg="red", variable=varuno, value=3, command=imprimiruno).place(x=60, y=230)
Radiobutton(root, text="NARANJA", fg="orange", variable=varuno, value=4, command=imprimiruno).place(x=60, y=250)
Radiobutton(root, text="AMARILLO", fg="yellow", variable=varuno, value=5, command=imprimiruno).place(x=60, y=270)
Radiobutton(root, text="VERDE", fg="green", variable=varuno, value=6, command=imprimiruno).place(x=60, y=290)
Radiobutton(root, text="AZUL", fg="blue", variable=varuno, value=7, command=imprimiruno).place(x=60, y=310)
Radiobutton(root, text="VIOLETA", fg="purple", variable=varuno, value=8, command=imprimiruno).place(x=60, y=330)
Radiobutton(root, text="GRIS", fg="grey", variable=varuno, value=9, command=imprimiruno).place(x=60, y=350)
Radiobutton(root, text="BLANCO", fg="black", variable=varuno, value=10, command=imprimiruno).place(x=60, y=370)

# ----------------------BANDAS DOS-------------------------------------------------------------------------------------
nbd = Label(root, text="SELECCIONA EL COLOR DE LA BANDA DOS").place(x=330, y=170)
Radiobutton(root, text="NEGRO", fg="black", variable=vardos, value=1, command=imprimirdos).place(x=330, y=190)
Radiobutton(root, text="MARRON", fg="brown", variable=vardos, value=2, command=imprimirdos).place(x=330, y=210)
Radiobutton(root, text="ROJO", fg="red", variable=vardos, value=3, command=imprimirdos).place(x=330, y=230)
Radiobutton(root, text="NARANJA", fg="orange", variable=vardos, value=4, command=imprimirdos).place(x=330, y=250)
Radiobutton(root, text="AMARILLO", fg="yellow", variable=vardos, value=5, command=imprimirdos).place(x=330, y=270)
Radiobutton(root, text="VERDE", fg="green", variable=vardos, value=6, command=imprimirdos).place(x=330, y=290)
Radiobutton(root, text="AZUL", fg="blue", variable=vardos, value=7, command=imprimirdos).place(x=330, y=310)
Radiobutton(root, text="VIOLETA", fg="purple", variable=vardos, value=8, command=imprimirdos).place(x=330, y=330)
Radiobutton(root, text="GRIS", fg="grey", variable=vardos, value=9, command=imprimirdos).place(x=330, y=350)
Radiobutton(root, text="BLANCO", fg="black", variable=vardos, value=10, command=imprimirdos).place(x=3300, y=370)

# ----------------------FACTOR------------------------------------------------------------------------------------------
nbf = Label(root, text="SELECCIONA EL COLOR DE LA BANDA FACTOR").place(x=600, y=170)
Radiobutton(root, text="NEGRO", fg="black", variable=fac, value=1, command=imprimirfactor).place(x=600, y=190)
Radiobutton(root, text="MARRON", fg="brown", variable=fac, value=2, command=imprimirfactor).place(x=600, y=210)
Radiobutton(root, text="ROJO", fg="red", variable=fac, value=3, command=imprimirfactor).place(x=600, y=230)
Radiobutton(root, text="NARANJA", fg="orange", variable=fac, value=4, command=imprimirfactor).place(x=600, y=250)
Radiobutton(root, text="AMARILLO", fg="yellow", variable=fac, value=5, command=imprimirfactor).place(x=600, y=270)
Radiobutton(root, text="VERDE", fg="green", variable=fac, value=6, command=imprimirfactor).place(x=600, y=290)
Radiobutton(root, text="AZUL", fg="blue", variable=fac, value=7, command=imprimirfactor).place(x=600, y=310)
Radiobutton(root, text="ORO", fg="gold", variable=fac, value=8, command=imprimirfactor).place(x=600, y=330)
Radiobutton(root, text="PLATA", fg="silver", variable=fac, value=9, command=imprimirfactor).place(x=600, y=350)
# ----------------------TOLERANCIA-------------------------------------------------------------------------------------
nbu = Label(root, text="SELECCIONA EL COLOR DE LA BANDA TOLERANCIA").place(x=870, y=170)
Radiobutton(root, text="MARRON", fg="brown", variable=tole, value=1, command=imprimirtolerancia).place(x=870, y=190)
Radiobutton(root, text="ROJO", fg="red", variable=tole, value=2, command=imprimirtolerancia).place(x=870, y=210)
Radiobutton(root, text="ORO", fg="gold", variable=tole, value=3, command=imprimirtolerancia).place(x=870, y=230)
Radiobutton(root, text="PLATA", fg="silver", variable=tole, value=4, command=imprimirtolerancia).place(x=870, y=250)
Radiobutton(root, text="NADA", fg="black", variable=tole, value=5, command=imprimirtolerancia).place(x=870, y=270)
# -----------------------BOTON DE RESULTADO----------------------------------------------------------------------------
resultadofinal = Button(root, text="OBTENER VALOR", command=totalfinal).place(x=547, y=400)

z = Label(root)
z.place(x=547, y=450)
z.config(text="HOLA MUNDO............")

root.mainloop()
