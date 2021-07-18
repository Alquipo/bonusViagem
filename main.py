import pandas as pd
from twilio.rest import Client

# Configuração Twilio
account_id = '' # Adicionar twilio ID
auth_token = '' # Adicionar twilio Token
client = Client(account_id, auth_token)

#abrir arquivo em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        message = client.messages \
            .create(
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}',
            from_='', # Adicionar telefone twilio
            to="", # Adicionar seu telefone
        )
