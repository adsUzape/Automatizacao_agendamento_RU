
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from Funcionalidade import agendar_almoço
from datetime import datetime

# Lista para armazenar os dias selecionados
dias_selecionados = []

def alternar_dia(cal, event):
    dia_clicado = cal.get_date()  # Obtém a data selecionada no calendário
    dia_numero = datetime.strptime(dia_clicado, "%d/%m/%Y").day  # Extrai o dia em número

    # Verifica se o dia já está selecionado
    if dia_numero in dias_selecionados:
        # Se estiver, desmarca (volta para a cor padrão)
        dias_selecionados.remove(dia_numero)
        cal.calevent_remove('all', date=datetime.strptime(dia_clicado, "%d/%m/%Y"))
    else:
        # Se não estiver, marca (altera para azul)
        dias_selecionados.append(dia_numero)
        cal.calevent_create(datetime.strptime(dia_clicado, "%d/%m/%Y"), 'Selecionado', 'selecionado')

    print(f'Dias selecionados: {dias_selecionados}')

def agendar():
    user = entry_user.get()
    senha = entry_senha.get()

    # Chama a função de agendamento com os dados de entrada
    try:
        agendar_almoço(user, senha, dias_selecionados)
        messagebox.showinfo("Sucesso", "Almoço agendado com sucesso!")
    except ValueError as ve:
        messagebox.showerror("Erro", str(ve))
    except RuntimeError as re:
        messagebox.showerror("Erro", str(re))

# Interface gráfica
root = tk.Tk()
root.title("Agendamento de Almoço")
root.geometry("400x400")

# Rótulos e campos de entrada
label_user = tk.Label(root, text="Usuário:")
label_user.pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

label_senha = tk.Label(root, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

# Calendário para seleção de dias
label_cal = tk.Label(root, text="Selecione os dias para agendar:")
label_cal.pack(pady=5)
cal = Calendar(root, selectmode='day', date_pattern='dd/mm/yyyy')
cal.pack(pady=10)

# Vincula o clique do mouse à função de alternar seleção de dias
cal.bind("<<CalendarSelected>>", lambda event: alternar_dia(cal, event))

# Botões
btn_agendar = tk.Button(root, text="Agendar", command=agendar)
btn_agendar.pack(pady=10)

btn_fechar = tk.Button(root, text="Fechar", command=root.quit)
btn_fechar.pack(pady=5)

# Loop principal da interface
root.mainloop()
