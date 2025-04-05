from django.db import models


class IBGEFood(models.Model):
    codigo = models.CharField(max_length=8)
    descricao_do_alimento = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80)
    codigo_de_preparacao = models.CharField(max_length=3)
    descricao_da_preparacao = models.CharField(max_length=80)

    # Macronutrientes e energia
    energia_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    proteina_g = models.DecimalField(max_digits=10, decimal_places=2)
    lipidios_totais_g = models.DecimalField(max_digits=10, decimal_places=2)
    carboidrato_g = models.DecimalField(max_digits=10, decimal_places=2)
    fibra_alimentar_total_g = models.DecimalField(max_digits=10, decimal_places=2)

    # Lipídios e colesterol
    colesterol_mg = models.DecimalField(max_digits=10, decimal_places=2)
    ag_saturados_g = models.DecimalField(max_digits=10, decimal_places=2)
    ag_monoinsaturados_g = models.DecimalField(max_digits=10, decimal_places=2)
    ag_poliinsaturados_g = models.DecimalField(max_digits=10, decimal_places=2)
    acido_linoleico_g = models.DecimalField(max_digits=10, decimal_places=2)
    acido_linolenico_g = models.DecimalField(max_digits=10, decimal_places=2)
    ag_trans_g = models.DecimalField(max_digits=10, decimal_places=2)

    # Açúcares
    acucar_total_g = models.DecimalField(max_digits=10, decimal_places=2)
    acucar_adicionado_g = models.DecimalField(max_digits=10, decimal_places=2)

    # Minerais
    calcio_mg = models.DecimalField(max_digits=10, decimal_places=2)
    magnesio_mg = models.DecimalField(max_digits=10, decimal_places=2)
    manganes_mg = models.DecimalField(max_digits=10, decimal_places=2)
    fosforo_mg = models.DecimalField(max_digits=10, decimal_places=2)
    ferro_mg = models.DecimalField(max_digits=10, decimal_places=2)
    sodio_mg = models.DecimalField(max_digits=10, decimal_places=2)
    sodio_adicionado_mg = models.DecimalField(max_digits=10, decimal_places=2)
    potassio_mg = models.DecimalField(max_digits=10, decimal_places=2)
    cobre_mg = models.DecimalField(max_digits=10, decimal_places=2)
    zinco_mg = models.DecimalField(max_digits=10, decimal_places=2)
    selenio_mcg = models.DecimalField(max_digits=10, decimal_places=2)

    # Vitaminas
    retinol_mcg = models.DecimalField(max_digits=10, decimal_places=2)
    vitamina_a_rae_mcg = models.DecimalField(max_digits=10, decimal_places=2)
    tiamina_mg = models.DecimalField(max_digits=10, decimal_places=2)
    riboflavina_mg = models.DecimalField(max_digits=10, decimal_places=2)
    niacina_mg = models.DecimalField(max_digits=10, decimal_places=2)
    niacina_ne_mg = models.DecimalField(max_digits=10, decimal_places=2)
    piridoxina_mg = models.DecimalField(max_digits=10, decimal_places=2)
    cobalamina_mcg = models.DecimalField(max_digits=10, decimal_places=2)
    folato_dfe_mcg = models.DecimalField(max_digits=10, decimal_places=2)
    vitamina_d_mcg = models.DecimalField(max_digits=10, decimal_places=2)
    vitamina_e_mg = models.DecimalField(max_digits=10, decimal_places=2)
    vitamina_c_mg = models.DecimalField(max_digits=10, decimal_places=2)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alimento IBGE"
        verbose_name_plural = "Alimentos IBGE"
        ordering = ['descricao_do_alimento']

    def __str__(self):
        return f"{self.descricao_do_alimento} ({self.codigo})"
