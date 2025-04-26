from django.db import models


def nutri_field(verbose_name):
    return models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=verbose_name
    )


class IBGEFood(models.Model):
    codigo = models.CharField(max_length=8)
    descricao_do_alimento = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80)
    codigo_de_preparacao = models.CharField(max_length=3, blank=True, null=True)
    descricao_da_preparacao = models.CharField(max_length=80)

    # Macronutrientes e energia
    energia_kcal = nutri_field('Energia (kcal)')
    proteina_g = nutri_field('Proteínas (g)')
    lipidios_totais_g = nutri_field('Lipídios totais (g)')
    carboidrato_g = nutri_field('Carboidratos (g)')
    fibra_alimentar_total_g = nutri_field('Fibras alimentares (g)')

    # Lipídios e colesterol
    colesterol_mg = nutri_field('Colesterol (mg)')
    ag_saturados_g = nutri_field('Ácidos graxos saturados (g)')
    ag_monoinsaturados_g = nutri_field('Ácidos graxos monoinsaturados (g)')
    ag_poliinsaturados_g = nutri_field('Ácidos graxos poliinsaturados (g)')
    acido_linoleico_g = nutri_field('Ácido linoleico (g)')
    acido_linolenico_g = nutri_field('Ácido linolênico (g)')
    ag_trans_g = nutri_field('Ácidos graxos trans (g)')

    # Açúcares
    acucar_total_g = nutri_field('Açúcares totais (g)')
    acucar_adicionado_g = nutri_field('Açúcares adicionados (g)')

    # Minerais
    calcio_mg = nutri_field('Cálcio (mg)')
    magnesio_mg = nutri_field('Magnésio (mg)')
    manganes_mg = nutri_field('Manganês (mg)')
    fosforo_mg = nutri_field('Fósforo (mg)')
    ferro_mg = nutri_field('Ferro (mg)')
    sodio_mg = nutri_field('Sódio (mg)')
    sodio_adicionado_mg = nutri_field('Sódio adicionado (mg)')
    potassio_mg = nutri_field('Potássio (mg)')
    cobre_mg = nutri_field('Cobre (mg)')
    zinco_mg = nutri_field('Zinco (mg)')
    selenio_mcg = nutri_field('Selênio (µg)')

    # Vitaminas
    retinol_mcg = nutri_field('Retinol (µg)')
    vitamina_a_rae_mcg = nutri_field('Vitamina A (RAE µg)')
    tiamina_mg = nutri_field('Tiamina (B1) (mg)')
    riboflavina_mg = nutri_field('Riboflavina (B2) (mg)')
    niacina_mg = nutri_field('Niacina (B3) (mg)')
    niacina_ne_mg = nutri_field('Equivalentes de niacina (mg)')
    piridoxina_mg = nutri_field('Piridoxina (B6) (mg)')
    cobalamina_mcg = nutri_field('Cobalamina (B12) (µg)')
    folato_dfe_mcg = nutri_field('Folato (DFE µg)')
    vitamina_d_mcg = nutri_field('Vitamina D (µg)')
    vitamina_e_mg = nutri_field('Vitamina E (mg)')
    vitamina_c_mg = nutri_field('Vitamina C (mg)')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alimento IBGE"
        verbose_name_plural = "Alimentos IBGE"
        ordering = ['descricao_do_alimento']

    def __str__(self):
        return f"{self.descricao_do_alimento} ({self.codigo})"
