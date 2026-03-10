from tkinter import *

root = Tk()
root.title("Calculador De Propina")
root.geometry("385x150")
root.config(bg="light blue")

titulo_1 = Label(root,
                text="Calculador De Propina",
                bg="light green").grid(row=0, column=0)

relleno_1 = Label(root,
                text="",
                bg="light blue").grid(row=1, column=0)

subtitulo_1 = Label(root,
                    text="La factura a pagar hoy es de: $",
                    bg="light green").grid(row=2, column=0)

entrada_1 = Entry(root)
entrada_1.grid(row=2, column=1)

subtitulo_2 = Label(root,
                    text="Cuanto porcentaje quiere usar para propina?: %",
                    bg="light green").grid(row=3, column=0)

entrada_2 = Entry(root)
entrada_2.grid(row=3, column=1)

def enviar_boton():
    try:
        ventana_resultado = Toplevel()
        ventana_resultado.config(bg="light yellow")
        valor_entrada_1 = entrada_1.get()
        valor_entrada_2 = entrada_2.get()
        obtencion_valor = float(valor_entrada_1)
        obtencion_porcentaje = float(valor_entrada_2)
        porcentaje = obtencion_valor * obtencion_porcentaje / 100
        resultado = porcentaje + obtencion_valor
        obtencion_str = str(resultado)

        titulo_2 = Label(ventana_resultado,
                        text="Resultado",
                        bg="light green").pack()
        subtitulo_2 = Label(ventana_resultado,
                                text="El total a pagar contando la propina es de $" + obtencion_str,
                                bg="light green").pack()
        boton_despejar = Button(ventana_resultado,
                                text="Despejar",
                                bg="red",
                                fg="white",
                                command=ventana_resultado.destroy).pack()

    except ValueError:
        entrada_1.delete(0, END)
        entrada_1.insert(0, "ERROR!!!")

boton_1 = Button(root,
                text="Calcular",
                bg="Green",
                fg="white",
                command=enviar_boton).grid(row=4, column=1)

mainloop()