from forex_python.converter import CurrencyRates, CurrencyCodes
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
root  = tk.Tk()
root.title("Currency Converter with Python")
root.geometry("300x200")
c = CurrencyRates()
d = CurrencyCodes()
divisa = ["USD","JPY","BGN","CYP","CZK","DKK","EEK","GBP","HUF","LTL","LVL","MTL","PLN","ROL","RON","SEK",
          "SIT","SKK","CHF","ISK","NOK","HRK","RUB","TRL","TRY","AUD","BRL","CAD","CNY","HKD","IDR","ILS",
          "INR","KRW","MXN","MYR","NZD","PHP","SGD","THB","ZAR","EUR"]

def is_valid_char(char):
    return char in "0123456789"

def convertirMoneda():
    entryResultado.config(state="normal")
    entryResultado.delete(0,END)
    entryResultado.config(state="disable")

    if entryValor.get()=="" or desde.get() =="" or hasta.get()=="":
        messagebox.showinfo(title="Mensaje de Aviso",message="Faltan datos")
    else:
        val = entryValor.get()
        if val.isnumeric():
            valor= float(entryValor.get())

            resultado = c.convert(desde.get(),hasta.get(),valor)
            entryResultado.config(state="normal")
            entryResultado.insert(0,round(resultado,3))
            entryResultado.config(state="disable")
        else:
            messagebox.showerror(title="ERROR",message="Dato ingresado es incorrecto")






lbl = Label(root,text="Ingrese valor a cambiar: ")
validatecommand = root.register(is_valid_char)

entryValor= Entry(root, validate="key", validatecommand=(validatecommand,"%S"))
entryValor.place(x=140,y=20)



lbl.place(x=0,y=20)
desde = ttk.Combobox(state="readonly",width=7)
desde.place(x=50,y=50)
desde['values'] = divisa

hasta =ttk.Combobox(state="readonly",width=7)
hasta.place(x=200,y=50)
hasta['values'] = divisa


btnConverter = Button(root,text="Convertir",bg="gold",command=convertirMoneda).place(x=200,y=20)

lblResultado = Label(root,text="Conversión: ").place(x=50,y=100)
entryResultado=Entry(root,width=10)
entryResultado.place(x=140,y=100)
entryResultado.config(state="disable")

root.mainloop()
