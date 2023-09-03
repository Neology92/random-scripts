import click

KCAL_PER_GRAM_PROTEIN = 4
KCAL_PER_GRAM_CARBS = 4
KCAL_PER_GRAM_FAT = 9


@click.group()
def cli():
    pass


@cli.command()
@click.option('-p', default=0, help='weight of protein in grams')
@click.option('-f', default=0, help='weight of fat in grams')
@click.option('-c', default=0, help='weight of carbs in grams')
def energy_ratio(p, f, c):
    protein_kcal = p * KCAL_PER_GRAM_PROTEIN
    carbs_kcal = c * KCAL_PER_GRAM_CARBS
    fat_kcal = f * KCAL_PER_GRAM_FAT

    kcal_sum = protein_kcal + carbs_kcal + fat_kcal
    protein_percent = calc_percent(protein_kcal, kcal_sum)
    carbs_percent = calc_percent(carbs_kcal, kcal_sum)
    fat_percent = calc_percent(fat_kcal, kcal_sum)

    kcal_ratio = [
        ("protein", protein_percent),
        ("carbs", carbs_percent),
        ("fat", fat_percent)
    ]
    kcal_ratio_rounded = map(lambda r: (r[0], round(r[1])), kcal_ratio)
    print_macro_ratio(kcal_ratio_rounded)


def calc_percent(nominator, denominator):
    return nominator / denominator * 100


def print_macro_ratio(elems):
    for (kind, percent) in elems:
        print("- Energy ratio: {k:.<7}{p:.>10} %".format(k=kind, p=percent))


if __name__ == "__main__":
    cli()
