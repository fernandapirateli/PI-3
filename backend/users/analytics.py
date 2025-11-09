import pandas as pd
import numpy as np
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


def salvar_imagem(plt):
    # Salva a imagem em base64 para HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')
    imagem_html = f'<img src="data:image/png;base64,{graphic}" class="img-fluid">'
    plt.close()
    return imagem_html


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

    imagem_html = salvar_imagem(plt)

    # Gera o relatório em string
    distribuicao = df['classificacao'].value_counts(normalize=True).sort_index()

    texto_classificacao = ""
    for classificacao, percentual in distribuicao.items():
        texto_classificacao += f"\n     • {classificacao}: {percentual:.1%}"

    relatorio = f'''RESUMO ESTATÍSTICO:

    Total de alunos: {len(df)}
    Distribuição percentual:    {texto_classificacao}
                '''

    return imagem_html, relatorio


def grafico_imc_idade(df):
    # Gráfico 2: IMC Médio por Idade
    plt.figure(figsize=(14, 8))

    # Calcula IMC médio por idade
    imc_por_idade = df.groupby('idade')['imc'].agg(['mean', 'std', 'count']).reset_index()

    # Gráfico de linha com área de desvio padrão
    plt.fill_between(imc_por_idade['idade'],
                     imc_por_idade['mean'] - imc_por_idade['std'],
                     imc_por_idade['mean'] + imc_por_idade['std'],
                     alpha=0.2, color='skyblue', label='Desvio Padrão')

    # Linha principal do IMC médio
    sns.lineplot(data=df, x='idade', y='imc',
                 estimator='mean', errorbar='sd',
                 linewidth=3, marker='o', markersize=8,
                 color='#2E86AB', label='IMC Médio')

    plt.axhline(y=16, color='red', linestyle='--', alpha=0.7, label='Abaixo do Peso')
    plt.axhline(y=20, color='green', linestyle='--', alpha=0.7, label='Sobrepeso')
    plt.axhline(y=25, color='orange', linestyle='--', alpha=0.7, label='Obesidade')

    plt.title('Evolução do IMC Médio por Idade',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Idade (anos)', fontsize=12, fontweight='semibold')
    plt.ylabel('IMC Médio', fontsize=12, fontweight='semibold')

    # Adiciona valores de contagem acima dos pontos
    for i, row in imc_por_idade.iterrows():
        plt.annotate(f"n={row['count']}",
                     (row['idade'], row['mean'] + 0.1),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center', fontsize=9, alpha=0.8)

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    sns.despine()
    plt.tight_layout()

    imagem_html = salvar_imagem(plt)

    idade_maior_imc = imc_por_idade.loc[imc_por_idade['mean'].idxmax()]
    idade_menor_imc = imc_por_idade.loc[imc_por_idade['mean'].idxmin()]

    # Gera o relatório em string
    relatorio = f'''TENDÊNCIAS POR IDADE::

        • Idade com maior IMC médio: {idade_maior_imc['idade']} anos (IMC: {idade_maior_imc['mean']:.1f})
        • Idade com menor IMC médio: {idade_menor_imc['idade']} anos (IMC: {idade_menor_imc['mean']:.1f})
                    '''

    return imagem_html, relatorio


def grafico_dispersao(df):
    # Gráfico 3: Relação Peso x Altura
    plt.figure(figsize=(14, 10))

    # Scatterplot com hue por classificação
    scatter = sns.scatterplot(data=df, x='altura', y='peso',
                              hue='classificacao', palette='viridis',
                              s=100, alpha=0.7, edgecolor='white', linewidth=0.5)

    # Adiciona linha de tendência
    sns.regplot(data=df, x='altura', y='peso',
                scatter=False, ci=None,
                line_kws={'color': 'red', 'linestyle': '--', 'alpha': 0.7},
                label='Tendência Linear')

    # Personalização
    plt.title('Relação entre Peso e Altura dos Alunos',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Altura (metros)', fontsize=12, fontweight='semibold')
    plt.ylabel('Peso (kg)', fontsize=12, fontweight='semibold')

    # Linhas de referência para IMC (opcional)
    # Criar curvas de IMC constante
    alturas = np.linspace(df['altura'].min(), df['altura'].max(), 50)
    for imc_val in [16, 20, 25]:
        pesos = imc_val * (alturas ** 2)
        plt.plot(alturas, pesos, 'gray', linestyle=':', alpha=0.5,
                 label=f'IMC = {imc_val}' if imc_val == 20 else "")

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
               title='Classificação', title_fontsize=10)

    plt.grid(True, alpha=0.3)
    sns.despine()

    plt.tight_layout()
    imagem_html = salvar_imagem(plt)

    # Estatísticas de correlação
    correlacao = df['altura'].corr(df['peso'])
    df['imc_esperado'] = df['peso'] / (df['altura'] ** 2)
    outliers = df[(df['imc_esperado'] < 12) | (df['imc_esperado'] > 32)]
    interpretacao = 'Forte' if abs(correlacao) > 0.7 else 'Moderada' if abs(correlacao) > 0.5 else 'Fraca'
    # Gera o relatório em string
    relatorio = f'''
    CORRELAÇÃO PESO x ALTURA:
    
        • Coeficiente de correlação: {correlacao:.3f}
        • Interpretação: {interpretacao} relação positiva
        • Casos que fogem do padrão esperado: {len(outliers)} aluno(s)
        '''

    return imagem_html, relatorio


def grafico_colunas(df):
    # Gráfico 4: Distribuição por Gênero
    plt.figure(figsize=(14, 8))

    # Gráfico de barras agrupadas
    ax = sns.countplot(data=df, x='classificacao', hue='genero',
                       order=['Muito Abaixo do Peso', 'Abaixo do Peso', 'Peso Adequado', 'Sobrepeso', 'Obesidade'],
                       palette=['#3498db', '#e74c3c'], saturation=0.8,
                       edgecolor='black', linewidth=0.5)

    plt.title('Distribuição da Classificação de IMC por Gênero',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Classificação de IMC', fontsize=12, fontweight='semibold')
    plt.ylabel('Número de Alunos', fontsize=12, fontweight='semibold')

    # Adiciona os valores nas barras
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.text(p.get_x() + p.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom',
                    fontsize=10, fontweight='bold')

    plt.legend(title='Gênero', title_fontsize=11,
               labels=['Meninos', 'Meninas'],
               bbox_to_anchor=(1.05, 1), loc='upper left')

    # Remove bordas
    sns.despine(left=True, bottom=True)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    imagem_html = salvar_imagem(plt)

    total_por_genero = df['genero'].value_counts()
    tabela_contingencia = pd.crosstab(df['classificacao'], df['genero'], normalize='index') * 100
    diferencas = []
    relatorio = ''

    # Estatísticas por gênero
    texto_distribuicao_genero = "DISTRIBUIÇÃO POR GÊNERO:"
    texto_distribuicao_genero += "\n\nTotal por gênero:"
    for genero, total in total_por_genero.items():
        texto_distribuicao_genero += f"\n  • {genero}: {total} alunos ({total/len(df)*100:.1f}%)"
    relatorio += texto_distribuicao_genero

    # Proporções por classificação e gênero
    texto_proporcoes = "\n\nPROPORÇÕES POR CLASSIFICAÇÃO:"

    for classificacao in tabela_contingencia.index:
        meninos = tabela_contingencia.loc[classificacao].iloc[0]
        meninas = tabela_contingencia.loc[classificacao].iloc[1]
        texto_proporcoes += f"\n  • {classificacao}: {meninos:.1f}% meninos vs {meninas:.1f}% meninas"

    relatorio += texto_proporcoes
    # Destaque de diferenças significativas
    for classificacao in tabela_contingencia.index:
        diff = abs(tabela_contingencia.loc[classificacao].iloc[0] - tabela_contingencia.loc[classificacao].iloc[1])
        if diff > 15:  # Diferença maior que 15%
            diferencas.append(classificacao)

    if diferencas:
        texto_diferencas = f"\nDIFERENÇAS SIGNIFICATIVAS:"
        for classificacao in diferencas:
            texto_diferencas += f"\n  • {classificacao} apresenta distribuição desigual entre gêneros"
        relatorio += texto_diferencas

    return imagem_html, relatorio
