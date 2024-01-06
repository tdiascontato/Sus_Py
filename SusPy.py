import pandas as pd
pd.options.display.max_columns = None
dados = pd.read_csv('C:/Projects/Python/Sus/dbsus.csv', encoding='latin1', low_memory=False)
dados.columns
# Vamos tirar algumas colunas não interessantes
columns = ['DT_NOTIFIC', 'SEM_NOT', 'NU_ANO', 'SG_UF_NOT',
       'ID_MUNICIP', 'ID_REGIONA', 'DT_SIN_PRI', 'SEM_PRI', 'DT_NASC',
       'NU_IDADE_N', 'CS_SEXO', 'CS_GESTANT', 'CS_RACA', 'CS_ESCOL_N', 'SG_UF',
       'ID_MN_RESI', 'ID_RG_RESI', 'ID_PAIS', 'DT_INVEST', 'ID_OCUPA_N',
       'ANT_DT_ACI', 'ANT_UF', 'ANT_MUNIC_', 'ANT_LOCALI', 'ANT_ZONA',
       'ANT_TEMPO_', 'ANT_LOCA_1', 'MCLI_LOCAL', 'CLI_DOR', 'CLI_EDEMA',
       'CLI_EQUIMO', 'CLI_NECROS', 'CLI_LOCAL_', 'CLI_LOCA_1', 'MCLI_SIST',
       'CLI_NEURO', 'CLI_HEMORR', 'CLI_VAGAIS', 'CLI_MIOLIT', 'CLI_RENAL',
       'CLI_OUTR_2', 'CLI_OUTR_3', 'CLI_TEMPO_', 'TP_ACIDENT', 'ANI_TIPO_1',
       'ANI_SERPEN', 'ANI_ARANHA', 'ANI_LAGART', 'TRA_CLASSI', 'CON_SOROTE',
       'NU_AMPOLAS', 'NU_AMPOL_1', 'NU_AMPOL_8', 'NU_AMPOL_6', 'NU_AMPOL_4',
       'NU_AMPO_7', 'NU_AMPO_5', 'NU_AMPOL_9', 'NU_AMPOL_3', 'COM_LOC',
       'COM_SECUND', 'COM_NECROS', 'COM_COMPOR', 'COM_DEFICT', 'COM_APUTAC',
       'COM_SISTEM', 'COM_RENAL', 'COM_EDEMA', 'COM_SEPTIC', 'COM_CHOQUE',
       'DOENCA_TRA', 'EVOLUCAO', 'DT_OBITO', 'DT_ENCERRA', 'DT_DIGITA']
# dados[columns]
# Tirar indez pode ajudar a retirar futuros alertas
newdatas = dados[columns].reset_index(drop=True)
newdatas['MCLI_LOCAL'] = newdatas['MCLI_LOCAL'].replace({1:'Sim', 2:'Não', 9:'Ignorado'})
# newdatas
columns_yes_or_no = ['MCLI_LOCAL', 'CLI_DOR', 'CLI_EDEMA', 'CLI_EQUIMO',
                     'CLI_NECROS', 'CLI_LOCAL_', 'MCLI_SIST', 'CLI_NEURO',
                     'CLI_HEMORR', 'CLI_VAGAIS', 'CLI_MIOLIT', 'CLI_RENAL',
                     'CLI_OUTR_2', 'COM_LOC', 'CON_SOROTE', 'COM_SECUND',
                     'COM_NECROS', 'COM_COMPOR', 'COM_DEFICT', 'COM_APUTAC',
                     'COM_SISTEM', 'COM_RENAL', 'COM_EDEMA', 'COM_SEPTIC',
                     'COM_CHOQUE', 'DOENCA_TRA']
for coluna in columns_yes_or_no:
    newdatas[coluna] = newdatas[coluna].replace({1:'Sim', 2:'Não', 9:'Ignorado'}) 
# newdatas
# newdatas.info()
columns_datas = ['DT_NOTIFIC', 'DT_SIN_PRI', 'DT_NASC', 'DT_INVEST', 'DT_OBITO', 'DT_ENCERRA', 'DT_DIGITA']
for coluna_data in columns_datas:
    # colocando como as datas estão e o tipo do erro
    newdatas[coluna_data] = pd.to_datetime(newdatas[coluna_data], format='%Y%m%d', errors='coerce')
# newdatas
newdatas['ANT_ZONA'] = newdatas['ANT_ZONA'].replace({1: 'Urbana',
                                                      2: 'Rural',
                                                      3: 'Periurbana',
                                                      4: 'Ignorado'})
# newdatas
newdatas['ANT_TEMPO_'] = newdatas['ANT_TEMPO_'].replace({1: '0 - 1h',                                                         
                                                         2: '1 - 3h',
                                                         3: '3 - 6h',
                                                         4: '6 - 12h',
                                                         5: '12 e 24h',
                                                         6: '24 e +h',
                                                         9: 'Ignorado'})
newdatas['ANT_LOCA_1'] = newdatas['ANT_LOCA_1'].replace({1: 'Cabeça',
                                                        2: 'Braço',
                                                        3: 'Ante-Braço',
                                                        4: 'Mão',
                                                        5: 'Dedo da Mão',
                                                        6: 'Tronco',
                                                        7: 'Coxa',
                                                        8: 'Perna',
                                                        9: 'Pé',
                                                        10: 'Dedo do Pé',
                                                        99: 'Ignorado'
                                                        })                                                     
newdatas['CLI_TEMPO_'] = newdatas['CLI_TEMPO_'].replace({1: 'Normal',
                                                      2: 'Alterado',
                                                      3: 'Não realizado'})
newdatas['ANI_SERPEN'] = newdatas['ANI_SERPEN'].replace({ 1 : 'Botrópico',
                                                    2 : 'Crotálico',
                                                    3 : 'Elapídico',
                                                    4 : 'Laquético',
                                                    5 : 'Serpente não peçonhenta',
                                                    9 : 'Ignorado' })
newdatas['ANI_ARANHA'] = newdatas['ANI_ARANHA'].replace({ 1 : 'Foneutrismo',
                                                    2 : 'Loxoscelismo',
                                                    3 : 'Latrodectismo',
                                                    4 : 'Outra aranha',
                                                    9 : 'Ignorado'})
newdatas['ANI_LAGART'] = newdatas['ANI_LAGART'].replace({ 1 : 'Lonomia',
                                                    2 : 'Outra lagarta',
                                                    9 : 'Ignorado'})
newdatas['TRA_CLASSI'] = newdatas['TRA_CLASSI'].replace({ 1 : 'Leve',
                                                    2 : 'Moderado',
                                                    3 : 'Grave',
                                                    9 : 'Ignorado' })
newdatas['EVOLUCAO'] = newdatas['EVOLUCAO'].replace({ 1 : 'Cura',
                                                2 : 'Óbito por acidente por animais peçonhentos',
                                                3 : 'Óbito por outras causas',
                                                9 : 'Ignorado'  })
newdatas['CS_GESTANT'] = newdatas['CS_GESTANT'].replace({ 1: '1º Trimestre',
                                                    2: '2º Trimestre',
                                                    3: '3º Trimestre',
                                                    4: 'Idade gestacional ignorada',
                                                    5: 'Não',
                                                    6: 'Não se aplica',
                                                    9: 'Ignorado'  })
newdatas['CS_RACA'] = newdatas['CS_RACA'].replace({ 1: 'Branca',
                                              2: 'Preta',
                                              3: 'Amarela',
                                              4: 'Parda',
                                              5: 'Indígena',
                                              9: 'Ignorado' })
newdatas['CS_ESCOL_N'] = newdatas['CS_ESCOL_N'].replace({ 0: 'Analfabeto',
                                                    1: '1ª a 4ª série incompleta do EF',
                                                    2: '4ª série completa do EF ( antigo 1° grau)',
                                                    3: '5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau)',
                                                    4: 'Ensino fundamental completo (antigo ginásio ou 1° grau)',
                                                    5: 'Ensino médio incompleto (antigo colegial ou 2° grau)',
                                                    6: 'Ensino médio completo (antigo colegial ou 2° grau)',                                                    
                                                    7: 'Educação superior incompleta',
                                                    8: 'Educação superior completa',
                                                    9: 'Ignorado',
                                                    10: 'Não se aplica' })
# newdatas
# mostrando idades
idades = []
for i in newdatas['NU_IDADE_N']:
    if i > 4000:
        idades.append(i-4000)
        
    elif 4000 > i:
        idades.append(1)
        
    else:
        idades.append(0)
        
newdatas['NU_IDADE_N'] = idades
# newdatas
# pesquisando pelo link para encontrar os municípios do Rio
municipios = pd.read_csv('https://raw.githubusercontent.com/andrejarenkow/Curso_SINAN_Udemy/main/dados/populacao%20ibge%206%20municipio%20br.csv')
municipios = municipios[['IBGE6', 'Municipio']]
municipios = municipios.set_index('IBGE6')
dic_municipios = municipios.to_dict()['Municipio']
newdatas['ID_MUNICIP_nome'] = newdatas['ID_MUNICIP'].map(dic_municipios)
newdatas['ID_MN_RESI_nome'] = newdatas['ID_MN_RESI'].map(dic_municipios)
newdatas