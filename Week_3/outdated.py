months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

'''
Criar um loop infinito para pedir uma data válida
Enquanto True:
Solicitar entrada do usuário (data = input("Date: "))
Remover espaços extras do início e fim da entrada
Verificar se a data está no formato numérico (M/D/YYYY)
Se "/" estiver na string:
Dividir data por "/" → mes, dia, ano = data.split("/")
Verificar se mes, dia, e ano são números válidos:
mes entre 1 e 12
dia entre 1 e 31
ano tem 4 dígitos
Se válido: sair do loop
Verificar se a data está no formato textual (Month D, YYYY)
Se "," estiver na string:
Remover "," → data = data.replace(",", "")
Dividir data por " " → mes_texto, dia, ano = data.split()
Verificar se mes_texto está na lista meses
Converter mes_texto para número: mes = meses.index(mes_texto) + 1
Verificar se dia e ano são válidos
Se válido: sair do loop
Se nenhuma verificação for válida, repetir o loop pedindo nova entrada
Formatar a data no padrão ISO 8601 (YYYY-MM-DD)

ano = int(ano)
mes = int(mes)
dia = int(dia)
data_formatada = f"{ano:04}-{mes:02}-{dia:02}"
Exibir a data formatada

print(data_formatada)'''