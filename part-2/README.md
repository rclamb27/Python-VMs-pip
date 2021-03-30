# CPSC 223p
##  Plotting JSON Data

This exercise is meant to be a trivial plot of time series data from an input JSON file.

Use the data contained in `USMISERY-INDEX.json` to plot three lines in three different styles using the matplotlib library.

Name the program `usmiseryplot.py`. The program takes one argument, an input file and outputs a PDF file with the name `us_misery_plot.pdf`.

The plot has two axes. The horizontal axis are dates. The vertical axis are floating point values.

Include a `requirements.txt` file which specifies what the software requirements are to recreate your virtual environment.

## US Misery Index
The misery index for the United States of America is an economic indicator. Originally created by the economist [Arthur Okun](https://en.wikipedia.org/wiki/Arthur_Melvin_Okun). The misery index is calculated as the addition of the unemployment rate and the inflation rate.

The data file `USMISERY-INDEX.json` contains a monthly record of the U.S. unemployment rate, inflation rate, and the misery index. The data is stored as a [JSON](https://en.wikipedia.org/wiki/JSON) formatted file which can be easily read with Python's standard library module [json](https://docs.python.org/3/library/json.html).

An example of opening and loading a JSON data file is the following Python code snippet:
```
import json
f = 'some_data_file.json'
with open(f, 'r') as fp:
    d = json.load(fp)
```

## Example Output
The plot shall be written to a file named `us_misery_plot.pdf`.
```
$ ./usmiseryplot.py USMISERY-INDEX.json
Writing plot to us_misery_plot.pdf
$
```

