import tkinter as tk
from tkinter import ttk

class Aplicacion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ### Title label
        self.titleLabel = ttk.Label(parent, text="Ingresa el estado inicial", font="Arial")
        self.titleLabel.place(x=70, y=20)

        ### Input value
        self.oneEntry = ttk.Entry(parent, font='Arial')
        self.oneEntry.place(x=65, y=70, width=35, height=35)
        self.twoEntry = ttk.Entry(parent, font='Arial')
        self.twoEntry.place(x=135, y=70, width=35, height=35)
        self.threeEntry = ttk.Entry(parent, font='Arial')
        self.threeEntry.place(x=205, y=70, width=35, height=35)
        
        self.fourEntry = ttk.Entry(parent, font='Arial')
        self.fourEntry.place(x=65, y=140, width=35, height=35)
        self.fiveEntry = ttk.Entry(parent, font='Arial')
        self.fiveEntry.place(x=135, y=140, width=35, height=35)
        self.sixEntry = ttk.Entry(parent, font='Arial')
        self.sixEntry.place(x=205, y=140, width=35, height=35)

        self.sevenEntry = ttk.Entry(parent, font='Arial')
        self.sevenEntry.place(x=65, y=210, width=35, height=35)
        self.eightEntry = ttk.Entry(parent, font='Arial')
        self.eightEntry.place(x=135, y=210, width=35, height=35)
        self.nineEntry = ttk.Entry(parent, font='Arial')
        self.nineEntry.place(x=205, y=210, width=35, height=35)

        #CheckButton
        self.var1 = tk.IntVar()
        self.showCheckButton = ttk.Checkbutton(parent, text='Mostrar solución', variable=self.var1)
        self.showCheckButton.place(x=55, y=280)
        #Button
        self.resolveButton = ttk.Button(parent, text="Resolver", command=self.resolveAction)
        self.resolveButton.place(x=180, y=280)

    def resolveAction(self):
        print(self.var1.get())

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("8-Puzzle :D")
    ventana.config(width=300, height=325)
    app = Aplicacion(ventana)
    ventana.mainloop()