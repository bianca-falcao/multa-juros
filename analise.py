import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_excel('dados/financeiro.xlsx')

data_inicio = input("Digite a data inicial (formato DD/MM/AAAA): ")
data_fim = input("Digite a data final (formato DD/MM/AAAA): ")

data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
data_fim = datetime.strptime(data_fim, '%d/%m/%Y')

df['data_pagamento'] = pd.to_datetime(df['data_pagamento'], format='%d/%m/%Y', errors='coerce')

df_filtrado = df[(df['data_pagamento'] >= data_inicio) & (df['data_pagamento'] <= data_fim)]

df_filtrado['Status'] = np.where(df_filtrado['encargos'] >= 100, 'Selecionar', 'Não selecionar')

df_filtrado = df_filtrado[df_filtrado['encargos'] > 0]

df_filtrado.to_excel('planilha_geral.xlsx', index=False)
print('Planilha geral salva: planilha_geral.xlsx')

df_selecionar = df_filtrado[df_filtrado['Status'] == 'Selecionar']

grupos = df_selecionar.groupby('area_pagadora')

for nome_grupo, grupo in grupos:
    nome_arquivo = f'planilha_{nome_grupo}.xlsx'.replace('/', '_').replace('\\', '_')
    grupo.to_excel(nome_arquivo, index=False)
    print(f'Planilha salva: {nome_arquivo}')




