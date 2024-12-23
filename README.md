# Projeto de Análise de Dados dos Chakras

Este projeto tem como objetivo analisar dados de chakras a partir de um arquivo Excel e gerar relatórios em formato PDF e Word. Ele utiliza bibliotecas como `pandas`, `fpdf` e `python-docx` para manipulação de dados e geração de documentos.

## Estrutura do Projeto

```
├── .gitignore
├── .python-version
├── documentos/ │
                ├── pipeline_dados/
                │ │ ├── data_processed/
                │ │ ├── data_raw/
                │ │ │ └── AvaChakras.xlsx
                │ │ ├── scripts/
                │ │ │ ├── extracao_form_1224.py
                │ │ │ └── processamento_dados.py
├── forms/  |
            │ └── init.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests/  |
            | └── init.py
```

## Dependências

As dependências do projeto estão listadas no arquivo [pyproject.toml](pyproject.toml). As principais bibliotecas utilizadas são:

- `pandas`
- `openpyxl`
- `tabulate`
- `fpdf`
- `python-docx`

## Instalação

Para instalar as dependências do projeto, utilize o Poetry:

```sh
poetry install
```

## Uso

Extração e Processamento de Dados
O script principal para extração e processamento de dados é o extracao_form_1224.py. Ele lê os dados do arquivo Excel AvaChakras.xlsx, realiza a análise e gera relatórios.

## Executando o Script

Para executar o script, utilize o seguinte comando:

```
python documentos/pipeline_dados/scripts/extracao_form_1224.py
```

## Funções Principais

- validate_id(): Valida o ID das colunas.
- filter_by_id(new_id): Filtra os dados pelo ID fornecido.
- dados_resumidos(id): Retorna um dicionário com dados resumidos para um ID específico.
- pontuacao_chakras(id_filtered): Calcula a pontuação dos chakras.
- chakra_menor_pontuacao(tabela_ordenada): Retorna os chakras com menor pontuação.
- add_heading(document, text, level=1): Adiciona um cabeçalho ao documento Word.
- add_paragraph(document, text): Adiciona um parágrafo ao documento Word.
- add_table(document, dataframe): Adiciona uma tabela ao documento Word.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
