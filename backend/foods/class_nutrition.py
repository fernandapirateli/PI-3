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
