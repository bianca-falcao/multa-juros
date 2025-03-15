# 📊 Projeto de Análise de Multas e Juros Pagos

Este projeto tem como objetivo analisar e demonstrar o total de multas e juros pagos com base em dados financeiros. Ele permite filtrar os dados por um período específico, classificar os valores conforme critérios definidos e gerar planilhas organizadas para análise.

## ⚙️ Funcionalidades

### Filtragem por Período:

- O usuário pode definir um intervalo de datas (inicial e final) para filtrar os registros da coluna **data_pagamento**.

### Classificação de Valores:

Os valores da coluna **encargos** são classificados como:

- **✅ "Selecionar"**: Quando o valor é maior ou igual a 100 (parâmetro definido pelo negócio)
- **❌ "Não selecionar"**: Quando o valor é menor que 100.

### Geração de Planilhas:

- **Planilha Geral:** Contém todos os registros filtrados onde **encargos > 0**.
- **Planilhas por Categoria:** Gera uma planilha separada para cada valor único da coluna **area_pagadora**, contendo apenas os casos classificados como **"Selecionar"**.

## 📋 Pré-requisitos

Para executar este projeto, você precisará ter instalado:

- **Python** (versão 3.6 ou superior).

### Bibliotecas Python:

- `pandas`
- `numpy`
- `datetime`

Instale as bibliotecas necessárias usando o comando:

```bash
pip install pandas numpy
```

## 🛠️ Como Usar

### Preparação dos Dados:

1. Coloque o arquivo Excel (**financeiro.xlsx**) na pasta `dados`.
2. Certifique-se de que o arquivo Excel tenha a seguinte estrutura:
   - **Coluna data_pagamento**: Contém as datas no formato `DD/MM/AAAA`.
   - **Coluna encargos**: Contém os valores de multas e juros.
   - **Coluna area_pagadora**: Contém as categorias ou descrições para agrupamento.

### Execução do Script:

Execute o script `analise.py` no terminal:

```bash
python analise.py
```

O script solicitará:

- **Data inicial**: Digite a data inicial no formato `DD/MM/AAAA`.
- **Data final**: Digite a data final no formato `DD/MM/AAAA`.

### Resultados:

O script gerará:

- Um arquivo `planilha_geral.xlsx` com todos os registros filtrados.
- Arquivos separados para cada valor único da coluna **area_pagadora** (apenas casos "Selecionar"), no formato `planilha_[area_pagadora].xlsx`.

## 📂 Estrutura do Projeto

```bash
projeto_financeiro/
│
├── dados/
│   └── financeiro.xlsx          
│
├── analise.py         
├── planilha_geral.xlsx           
├── planilhas_selecionar/         
├── planilha_Categoria_A.xlsx
├── planilha_Categoria_B.xlsx
├── ...
│
└── README.md                     
```

## 📄 Exemplo de Uso

**Entrada:**

```plaintext
Data inicial: 01/01/2023
Data final: 31/12/2023
```

**Processamento:**

1. O script filtra os registros onde a coluna **data_pagamento** está entre 01/01/2023 e 31/12/2023.
2. Classifica os valores da coluna **encargos** como "Selecionar" ou "Não selecionar".
3. Gera a planilha geral e as planilhas por categoria.

**Saída:**

- `planilha_geral.xlsx`: Contém todos os registros filtrados.
- `planilhas_selecionar/planilha_Categoria_A.xlsx`: Contém os registros da categoria **Categoria A** classificados como "Selecionar".

## 🎨 Personalização

### Alterar Critérios de Classificação:

Para modificar o valor de corte para **"Selecionar"**, edite a linha:

```python
df_filtrado['Status'] = np.where(df_filtrado['Total.2'] >= 100, 'Selecionar', 'Não selecionar')
```

Altere o valor `100` para o desejado.

### Alterar Colunas de Referência:

Se as colunas no arquivo Excel tiverem nomes diferentes, atualize os nomes no script (ex.: `data_pagamento`, `encargos`, `area_pagadora`).

## 🤝 Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para:

- Reportar problemas.
- Sugerir melhorias.
- Enviar pull requests.

## 📄 Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

##

Feito com ❤️ por Bianca Falcão.
