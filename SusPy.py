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
columns_yes_or_no = ['MCLI_LOCAL', 'CLI_DOR', 'CLI_EDEMA', 'CLI_EQUIMO', 'CLI_NECROS', 'CLI_LOCAL_', 'MCLI_SIST', 'CLI_NEURO', 'CLI_HEMORR', 'CLI_VAGAIS', 'CLI_MIOLIT', 'CLI_RENAL', 'CLI_OUTR_2', 'COM_LOC', 'CON_SOROTE', 'COM_SECUND', 'COM_NECROS', 'COM_COMPOR', 'COM_DEFICT', 'COM_APUTAC', 'COM_SISTEM', 'COM_RENAL', 'COM_EDEMA', 'COM_SEPTIC', 'COM_CHOQUE', 'DOENCA_TRA']
for coluna in columns_yes_or_no:
    newdatas[coluna] = newdatas[coluna].replace({1:'Sim', 2:'Não', 9:'Ignorado'}) 
newdatas