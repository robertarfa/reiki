import pandas as pd
import re

filepath = "./AvaChakras.xlsx"  # Substitua pelo seu caminho de arquivo
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
    
def sum_points(name, filtered_column, dados):
    if filtered_column is not None:
      try:
          linha_soma = filtered_column.sum(axis=1)
          print("Soma chakra",name,": ", linha_soma[dados["Id"] == 1][0])
          data = {'Chakra': [name], 'Soma': [linha_soma[dados["Id"] == 1][0]]}
          return pd.DataFrame(data)
      except TypeError:
          print("Erro: Algumas colunas não são numéricas. Certifique-se que todas as colunas em base_columns contenham apenas valores numéricos.")

#Exemplo de uso:
base_columns = get_columns(filepath, "Pontos – [BASE]")

dados = df[["Id","Nome Completo:", "E-mail:", "Whatsapp:"]]
chakra_base = df[base_columns]
base_df = sum_points("Base", chakra_base, dados)

