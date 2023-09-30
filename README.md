# Just some random scripts

This repo is just my landfill of scripts I'm writing as useful tools, or just for fun.

## Listing

_(might not be fully up to date with the files)_

**operations on files**

- [ico_pdf_polyglot_file.py](#ico_pdf_polyglot_file.py)

**binary**

- [binary_trainer.py](#binary_trainer.py)
- [clear_bit.py](#clear_bit.py)
- [gen_bin_mask.py](#gen_bin_mask.py)
- [set_val_in_bin.py](#set_val_in_bin.py)

**web**

- [addAccessibleTagsAreaForNirvanaHqApp.js](#addAccessibleTagsAreaForNirvanaHqApp.js)

**misc**

- [git-fill-1-day-gaps.py](#git-fill-1-day-gaps.py)
- [macro_calculator.py](#macro_calculator.py)

## ico_pdf_polyglot_file.py

🚧 WIP 🚧

This script takes an ico file and a pdf file and creates a polyglot</br>
file that is both a valid ico and a valid pdf file.</br>
Inspired with [PagedOut!#1 article by @tickelton](https://pagedout.institute/download/PagedOut_001_beta1.pdf#page=13)

```bash
TODO...
```

## binary_trainer.py

This script gonna help you to train your binary encoding skills</br>
in 0000 - 1111 range (0 - 15 in decimal). It's nice to be able</br>
to convert small binary values to decimal and vice versa in your head.</br>

```bash
$ python binary_trainer.py
```

## clear_bit.py

This script clears a bit at given position in a binary number.

```bash
$ python clear_bit.py 1011 2

Your number with cleared bit:
1001
```

## gen_bin_mask.py

This script generates a binary mask with given number of bits,</br>
shifted by given number of positions.

```bash
$ python gen_bin_mask.py 5 3

Your mask:
1111100
```

## set_val_in_bin.py

```bash
$ python set_val_in_bin.py 100101 4 1

Your updated value is:
101101

```

## addAccessibleTagsAreaForNirvanaHqApp.js

Javascript snippet that adds an accessible "Current Sprint" tag filter </br>
for the [NirvanaHQ](https://nirvanahq.com/) app.</br>
Use with any browser extension that allows you to inject custom JS.</br>

## git-fill-1-day-gaps.py

🚧 WIP 🚧

Another script to fill a github activity log.</br>
This one fills 1 day gaps (Including Mondays and Fridays gaps).</br>
Like one wise saide once: </br>
"Don't judge annyone by thier github activity log.</br>
It's not a good measure of productivity."</br>

```bash
TODO...
```

## macro_calculator.py

This script takes protein, fat and carbs values in grams</br>
and calculates what's their energy ratio. </br>

Why this weird way of calling it? </br>
Probably it meant to have more functions. </br>
But it doesn't. </br>

```bash
$ python macro_calculator.py energy-ratio 100 50 200

Energy ratio:
-----------------
- protein   24 %
- fat       27 %
- carbs     48 %
```
