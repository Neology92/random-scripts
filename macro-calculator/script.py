KCAL_PER_GRAM_PROTEIN = 4
KCAL_PER_GRAM_CARBS = 4
KCAL_PER_GRAM_FAT = 9

protein = 0
carbs = 0
fat = 0

def count_energy_proportions(p, c, f):
    protein_kcal = p * KCAL_PER_GRAM_PROTEIN
    carbs_kcal = c * KCAL_PER_GRAM_CARBS
    fat_kcal = f * KCAL_PER_GRAM_FAT

    kcal_sum = protein_kcal + carbs_kcal + fat_kcal
    protein_percent = calc_percent(protein_kcal, kcal_sum)
    carbs_percent = calc_percent(carbs_kcal, kcal_sum)
    fat_percent = calc_percent(fat_kcal, kcal_sum)

    proportions = (protein_percent, carbs_percent, fat_percent)
    return proportions


def calc_percent(nominator, denominator):
    return nominator / denominator


if __name__ == "__main__":
    print(count_energy_proportions(7,6,5))


