import pandas as pd
import numpy as np
import statistics as st
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Backend não-interativo
import matplotlib.pyplot as plt

import io
import base64


sns.set_palette('Accent')
sns.set_style('darkgrid')


def obter_dataframe():
    df = pd.read_csv('students/management/commands/data/students_data_classified.csv',
                     encoding='latin1')
    df = df[['genero', 'idade', 'altura', 'peso', 'imc', 'classificacao']]

    df.idade = df.idade // 12
    df.altura = round(df.altura / 100, 2)
    df.peso = df.peso / 1000

    return df


def grafico_barras(df):
    # Configuração do gráfico
    plt.figure(figsize=(12, 8))
    ordem_classificacao = ['Muito Abaixo do Peso', 'Abaixo do Peso', 'Peso Adequado', 'Sobrepeso', 'Obesidade']

    # Gráfico de barras
    ax = sns.countplot(data=df, y='classificacao', order=ordem_classificacao,
                       saturation=0.8, edgecolor='black', linewidth=0.5)

    plt.title('Distribuição dos Alunos por Classificação de IMC',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Número de Alunos', fontsize=12, fontweight='semibold')
    plt.ylabel('Classificação de IMC', fontsize=12, fontweight='semibold')

    # Adiciona os valores nas barras
    for p in ax.patches:
        width = p.get_width()
        plt.text(width + 0.5, p.get_y() + p.get_height() / 2.,
                 f'{int(width)}',
                 ha='left', va='center', fontsize=11, fontweight='bold')

    # Remove bordas desnecessárias
    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    # Salva a imagem em base64 para HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')
    imagem_html = f'<img src="data:image/png;base64,{graphic}" class="img-fluid">'
    plt.close()
    # Gera o relatório em string
    distribuicao = df['classificacao'].value_counts(normalize=True).sort_index()

    texto_classificacao = ""
    for classificacao, percentual in distribuicao.items():
        texto_classificacao += f"\n  • {classificacao}: {percentual:.1%}"

    relatorio = f'''RESUMO ESTATÍSTICO:

    Total de alunos: {len(df)}                
    Distribuição percentual:{texto_classificacao}
                '''

    return imagem_html, relatorio
