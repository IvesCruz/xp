"""
Extrair os agregados do número de doses de vacinas aplicadas por dia,
dividindo pela vacina utilizada e a dose (1ª ou 2ª dose).
Montar gráficos com que julgar interessantes para compreender melhor os dados.
Exportar os agregados para o excel.

R: Será necessário apenas os dados:
    1 - vacina_fabricante_nome  = NOME DO FABRICANTE/FORNECEDOR
    2 - vacina_dataAplicacao = DATA DE APLICAÇÃO DA VACINA
    3 - vacina_descricao_dose =  DESCRIÇÃO DA DOSE
    4 - vacina_nome = NOME DA VACINA/PRODUTO
    
"""

import pandas as pd

#IMPORTAÇÃO DO ARQUIVO PARA TRATAMENTO
arquivo = pd.read_csv(r"C:/Users/Ives/Desktop/arquivo.csv", encoding='utf-8', sep=';')

#SELECIONANDO COLUNAS NECESSÁRIAS
df1 = arquivo.reindex(columns=['vacina_fabricante_nome', 'vacina_dataAplicacao','vacina_descricao_dose', 'vacina_nome'])

#EXPORTANDO ARQUIVO PARA VERIFICAÇÃO NO EXCEL
df1.to_excel("C:/Users/Ives/Desktop/output.xlsx") 


