import pandas as pd

def ler_excel_para_dicionario(caminho_excel):
    df = pd.read_excel(caminho_excel)
    departamentos = {}

    for index, row in df.iterrows():
        departamento_id = int(row['departamento_id'])
        horas_totais = int(row['horas_totais'])
        funcionario_id = int(row['funcionario_id'])

        if departamento_id not in departamentos:
            departamentos[departamento_id] = {
                'horas_totais': horas_totais,
                'funcionarios': [funcionario_id],
                'horas_funcionarios': []
            }
        else:
            departamentos[departamento_id]['funcionarios'].append(funcionario_id)

    return departamentos

def distribuir_horas_trabalho(horas_totais, qtd_funcionarios):
    incremento = 10
    horas_restantes = horas_totais
    horas_funcionarios = []
    
    for i in range(qtd_funcionarios):
        horas_funcionarios.append(20)
    horas_restantes -= 20 * qtd_funcionarios
    while (horas_restantes > 0):
        for i in range(qtd_funcionarios):
            if (horas_restantes > 0):
                horas_funcionarios[i] += incremento
                horas_restantes -= incremento
    return horas_funcionarios

# MAIN
caminho_excel = 'horas_trabalho_restaurante.xlsx'
departamentos = ler_excel_para_dicionario(caminho_excel)

# Criar listas para construir o DataFrame
departamento_id_list = []
funcionario_list = []
horas_funcionarios_list = []

for departamento_id, info_departamento in departamentos.items():
    horas_funcionarios = distribuir_horas_trabalho(info_departamento['horas_totais'], len(info_departamento['funcionarios']))
    for funcionario_id, horas_funcionario in zip(info_departamento['funcionarios'], horas_funcionarios):
        departamento_id_list.append(departamento_id)
        funcionario_list.append(funcionario_id)
        horas_funcionarios_list.append(horas_funcionario)

# Criar DataFrame
resultados_df = pd.DataFrame({
    'departamento_id': departamento_id_list,
    'funcionario_id': funcionario_list,
    'horas_funcionarios': horas_funcionarios_list
})

# Salvar DataFrame em um novo arquivo Excel
resultados_df.to_excel('horas_trabalho_corrigidas.xlsx', index=False)
