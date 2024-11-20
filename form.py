import pandas as pd
# import re

filepath = "../AvaChakras.xlsx"  # Substitua pelo seu caminho de arquivo
df = pd.read_excel(filepath)

def get_columns(filepath, column):
    """
    Retorna uma lista de colunas contendo column em seu nome.

    Args:
        filepath: Caminho para o arquivo XLS ou XLSX.

    Returns:
        Uma lista de strings com os nomes das colunas. Retorna None se houver erro.
    """
    try:
        base_cols = [col for col in df.columns if column in col]
        return base_cols
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {filepath}")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None
    
def append_sum_to_dataframe(name,filtered_column, dados, id, sum_df):
    """Appends a chakra sum to an existing DataFrame."""
    if filtered_column is not None:
      try:
        linha_soma = filtered_column.sum(axis=1)
        sum_value = linha_soma[dados["Id"] == id][0]
        new_row = pd.DataFrame({'Chakra': [name], 'Soma': sum_value})
        return pd.concat([sum_df, new_row], ignore_index=True)
      except TypeError:
          print("Erro: Algumas colunas não são numéricas. Certifique-se que todas as colunas em base_columns contenham apenas valores numéricos.")

def list_chakras(columns):
        chakras = []
        for column in columns:
            # chakra = column.split("[")[-1].split("]")[0]
            chakra = column.split("]")[0] + "]"
            chakras.append(chakra)

        chakras_unique = list(set(chakras))  # Convert the set back to a list to maintain original data type
        return chakras_unique #The order may change.
#Exemplo de uso:
columns = get_columns(filepath, "Pontos – [")

list_chakras = list_chakras(columns)

laringeo_columns = get_columns(filepath, list_chakras[0])
sexual_columns = get_columns(filepath, list_chakras[1])
solar_columns = get_columns(filepath, list_chakras[2])
cardio_columns = get_columns(filepath, list_chakras[3])
base_columns = get_columns(filepath, list_chakras[4])
coro_columns = get_columns(filepath, list_chakras[5])
frontal_columns = get_columns(filepath, list_chakras[6])

dados = df[["Id","Nome Completo:", "E-mail:", "Whatsapp:"]]

chakras_df = pd.DataFrame(columns=['Chakra', 'Soma'])

id = 1
print("Dados:", dados[dados["Id"] == id])
chakras_df = append_sum_to_dataframe(list_chakras[0], df[laringeo_columns], dados, id,chakras_df)
chakras_df = append_sum_to_dataframe(list_chakras[1], df[sexual_columns], dados, id,chakras_df)
chakras_df = append_sum_to_dataframe(list_chakras[2], df[solar_columns], dados, id,chakras_df)
chakras_df = append_sum_to_dataframe(list_chakras[3], df[cardio_columns], dados, id,chakras_df)
chakras_df = append_sum_to_dataframe(list_chakras[4], df[base_columns], dados, id,chakras_df)
chakras_df = append_sum_to_dataframe(list_chakras[5], df[coro_columns], dados, id,chakras_df)
chakras_df = append_sum_to_dataframe(list_chakras[6], df[frontal_columns], dados, id,chakras_df)

sorted_df = chakras_df.sort_values(by='Soma', ascending=False)
