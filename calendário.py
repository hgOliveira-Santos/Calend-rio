from tkinter import *
from tkinter import ttk
import calendar

def mostrarCalendário():
    nova_janela = Tk()
    nova_janela.title(f"CALENDÁRIO {int(ano_calendário.get())}")
    nova_janela.resizable(False, False)

    ano = int(ano_calendário.get())
    conteúdo_calendário = calendar.calendar(ano)
    label_calendário = Label(master=nova_janela, text=conteúdo_calendário, font=("Consolas 10 bold"))
    label_calendário.grid(row=5, column=0, padx=20)
    nova_janela.mainloop()


# Cria uma instância da janela principal
janela = Tk()

# Configurações da janela
janela.title("Calendário")  # Título da janela
janela.geometry("400x250")  # Tamanho inicial da janela
janela.maxsize("600", "350")  # Tamanho máximo que a janela pode ser redimensionada
janela.config(background="#076464")  # Cor de fundo da janela

# Rótulo de título "Calendário"
Label(master=janela, text="Calendário", font=("Arial 18 bold"), bg="#076464", fg="white").pack(pady=20)

# Rótulo para instrução "Insira o ano"
Label(master=janela, text="Insira o ano", bg="#076464", fg="white").pack()

# Entrada de texto para o ano do calendário
ano_calendário = ttk.Entry(master=janela, font=("Arial 14 bold"))
ano_calendário.pack()

# Botão para exibir o calendário (chama a função mostrarCalendário quando clicado)
botão_mostra_calendário = ttk.Button(master=janela, text="Exibir calendário", command=mostrarCalendário).pack(pady=20)

# Botão para sair do programa
botão_sair = ttk.Button(master=janela, text="Sair do programa", command=exit).pack(pady=10)

if __name__ == "__main__":
    janela.mainloop()