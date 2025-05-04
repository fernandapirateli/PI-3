def calcular_energia(carboidratos, proteinas, lipidios):
    return (carboidratos * 4) + (proteinas * 4) + (lipidios * 9)


DRIS_NUTRICIONAIS = {
    # Lactentes
    '0-6_meses': {
        'lipidios_totais_g': 31,
        'carboidratos_g': 60,
        'proteinas_g': 9.1,
        'fibras_g': 0,
        'energia_kcal': calcular_energia(60, 9.1, 31)
    },
    '6-12_meses': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 95,
        'proteinas_g': 11.0,
        'fibras_g': 0,
        'energia_kcal': calcular_energia(95, 11.0, 30)
    },

    # Crianças
    '1-3_anos': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 130,
        'proteinas_g': 13,
        'fibras_g': 19,
        'energia_kcal': calcular_energia(130, 13, 30)
    },
    '4-8_anos': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 130,
        'proteinas_g': 19,
        'fibras_g': 25,
        'energia_kcal': calcular_energia(130, 19, 35)
    },

    # Homens
    '9-13_anos_masc': {
        'lipidios_totais_g': 40,
        'carboidratos_g': 130,
        'proteinas_g': 34,
        'fibras_g': 31,
        'energia_kcal': calcular_energia(130, 34, 40)
    },
    '14-18_anos_masc': {
        'lipidios_totais_g': 40,
        'carboidratos_g': 130,
        'proteinas_g': 52,
        'fibras_g': 38,
        'energia_kcal': calcular_energia(130, 52, 40)
    },
    '19-30_anos_masc': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 130,
        'proteinas_g': 56,
        'fibras_g': 38,
        'energia_kcal': calcular_energia(130, 56, 35)
    },
    '31-50_anos_masc': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 130,
        'proteinas_g': 56,
        'fibras_g': 38,
        'energia_kcal': calcular_energia(130, 56, 35)
    },
    '51-70_anos_masc': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 130,
        'proteinas_g': 56,
        'fibras_g': 30,
        'energia_kcal': calcular_energia(130, 56, 30)
    },
    '70+_anos_masc': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 130,
        'proteinas_g': 56,
        'fibras_g': 30,
        'energia_kcal': calcular_energia(130, 56, 30)
    },

    # Mulheres
    '9-13_anos_fem': {
        'lipidios_totais_g': 40,
        'carboidratos_g': 130,
        'proteinas_g': 34,
        'fibras_g': 26,
        'energia_kcal': calcular_energia(130, 34, 40)
    },
    '14-18_anos_fem': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 130,
        'proteinas_g': 46,
        'fibras_g': 26,
        'energia_kcal': calcular_energia(130, 46, 35)
    },
    '19-30_anos_fem': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 130,
        'proteinas_g': 46,
        'fibras_g': 25,
        'energia_kcal': calcular_energia(130, 46, 30)
    },
    '31-50_anos_fem': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 130,
        'proteinas_g': 46,
        'fibras_g': 25,
        'energia_kcal': calcular_energia(130, 46, 30)
    },
    '51-70_anos_fem': {
        'lipidios_totais_g': 25,
        'carboidratos_g': 130,
        'proteinas_g': 46,
        'fibras_g': 21,
        'energia_kcal': calcular_energia(130, 46, 25)
    },
    '70+_anos_fem': {
        'lipidios_totais_g': 25,
        'carboidratos_g': 130,
        'proteinas_g': 46,
        'fibras_g': 21,
        'energia_kcal': calcular_energia(130, 46, 25)
    },

    # Gravidez
    '14-18_anos_gravidez': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 175,
        'proteinas_g': 71,
        'fibras_g': 28,
        'energia_kcal': calcular_energia(175, 71, 30)
    },
    '19-30_anos_gravidez': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 175,
        'proteinas_g': 71,
        'fibras_g': 28,
        'energia_kcal': calcular_energia(175, 71, 30)
    },
    '31-50_anos_gravidez': {
        'lipidios_totais_g': 30,
        'carboidratos_g': 175,
        'proteinas_g': 71,
        'fibras_g': 28,
        'energia_kcal': calcular_energia(175, 71, 30)
    },

    # Lactação
    '14-18_anos_lactacao': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 210,
        'proteinas_g': 71,
        'fibras_g': 29,
        'energia_kcal': calcular_energia(210, 71, 35)
    },
    '19-30_anos_lactacao': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 210,
        'proteinas_g': 71,
        'fibras_g': 29,
        'energia_kcal': calcular_energia(210, 71, 35)
    },
    '31-50_anos_lactacao': {
        'lipidios_totais_g': 35,
        'carboidratos_g': 210,
        'proteinas_g': 71,
        'fibras_g': 29,
        'energia_kcal': calcular_energia(210, 71, 35)
    }
}

OBSERVACAO = {
    '0-6_meses': (
        "A alimentação nesta fase é exclusivamente por leite materno ou fórmula, "
        "oferecida sob livre demanda. A divisão percentual dos macronutrientes por refeição "
        "não se aplica da mesma forma que para crianças maiores."
    ),
    '6-12_meses': (
        "Nesta faixa etária, a introdução alimentar ocorre gradualmente com manutenção do leite materno. "
        "As refeições ainda são adaptativas, mas o ideal é que cada uma contribua com cerca de 10% a 20% "
        "das necessidades nutricionais diárias, respeitando o apetite do bebê."
    ),
    '1-3_anos': (
        "Considerando de 5 a 6 refeições ao dia (café, lanche, almoço, lanche, jantar e ceia opcional), "
        "espera-se que cada refeição represente aproximadamente entre 15% a 25% das necessidades nutricionais "
        "diárias para esta faixa etária."
    ),
    '4-8_anos': (
        "Para crianças entre 4 e 8 anos, com padrão alimentar distribuído em 5 a 6 refeições diárias, "
        "é adequado que cada refeição contribua com cerca de 15% a 25% das necessidades nutricionais diárias."
    ),
    '9-13_anos_masc': (
        "Nessa fase de crescimento acelerado, meninos geralmente apresentam maior gasto energético. "
        "Para atender adequadamente às suas necessidades nutricionais, cada refeição — em um plano com 5 a 6 ao dia — "
        "deve representar de 15% a 25% da ingestão diária recomendada de nutrientes."
    ),
    '9-13_anos_fem': (
        "Durante a pré-adolescência, meninas apresentam ritmo de crescimento elevado, mas com exigências calóricas "
        "ligeiramente menores que os meninos. Refeições equilibradas (5 a 6 por dia) devem prover de 15% a 25% das "
        "necessidades diárias de energia e nutrientes."
    ),
    '14-18_anos_masc': (
        "A adolescência masculina exige maior aporte calórico e proteico, devido ao pico de crescimento e aumento da "
        "massa muscular. "
        "Com 5 a 6 refeições ao dia, recomenda-se que cada uma cubra de 15% a 25% das necessidades nutricionais dessa "
        "faixa etária."
    ),
    '14-18_anos_fem': (
        "Durante a adolescência, meninas requerem atenção especial ao ferro e cálcio, fundamentais para o "
        "desenvolvimento. "
        "Em uma rotina alimentar com 5 a 6 refeições, cada uma deve fornecer cerca de 15% a 25% das demandas "
        "diárias de nutrientes."
    ),
    '19-30_anos_masc': (
        "Na fase adulta jovem, os hábitos alimentares tendem a variar. Comumente realizam-se de 3 a 4 refeições ao dia."
        "Cada refeição idealmente deve contribuir com 20% a 33% das necessidades nutricionais diárias para essa "
        "faixa etária."
    ),
    '19-30_anos_fem': (
        "Adultas jovens geralmente apresentam menor gasto energético comparado aos homens, "
        "o que reflete em escolhas por refeições menos calóricas. Considerando de 3 a 4 refeições ao dia, "
        "cada uma deve suprir de 20% a 33% das necessidades nutricionais."
    ),
    '31-50_anos_masc': (
        "Na vida adulta, a prática de 3 a 4 refeições ao dia é comum, especialmente por conta da rotina agitada. "
        "Cada refeição deve fornecer de 20% a 33% das necessidades nutricionais, com atenção ao controle de gorduras "
        "e ao equilíbrio energético."
    ),
    '31-50_anos_fem': (
        "Mulheres adultas tendem a apresentar um metabolismo mais lento, o que demanda maior atenção ao valor "
        "calórico das refeições. "
        "Com 3 a 4 refeições diárias, cada uma deve prover cerca de 20% a 33% das necessidades nutricionais "
        "dessa fase da vida."
    ),
    '51-70_anos_masc': (
        "Com o avanço da idade, a ingestão de cálcio, fibras e proteínas passa a ser crucial. "
        "Homens nessa faixa etária podem manter de 3 a 4 refeições ao dia, sendo ideal que cada uma cubra de 20% a 33% "
        "das necessidades diárias."
    ),
    '51-70_anos_fem': (
        "Para mulheres acima dos 50 anos, recomenda-se especial atenção ao consumo de cálcio, vitamina D e fibras. "
        "Com 3 a 4 refeições diárias, cada uma deve fornecer de 20% a 33% das necessidades nutricionais totais."
    ),
    '70+_anos_masc': (
        "Na terceira idade, a alimentação deve ser rica em nutrientes essenciais, com foco em cálcio, "
        "proteínas e fibras. "
        "Considerando refeições mais leves e frequentes, cada uma das 3 a 5 refeições diárias pode "
        "representar de 20% a 30% da ingestão total recomendada."
    ),
    '70+_anos_fem': (
        "Para mulheres idosas, manter uma alimentação leve, nutritiva e com foco em cálcio e vitamina D é essencial. "
        "Com 3 a 5 refeições ao dia, cada uma deve atender de 20% a 30% das necessidades nutricionais, "
        "respeitando a tolerância individual."
    )
}
