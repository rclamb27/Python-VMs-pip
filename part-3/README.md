# CPSC 223p
##  Plotting CSV Data
This exercise is meant to be a trivial plot of time series data from several CSV files.

Use the data contained in the `ECONOMIST-BIGMAC_*.csv` files to plot a number of different plots using the matplotlib library. Details of the plots are given at the end of this assignment.

Name the program `bigmac_index.py`. The program takes at least one argument, an input file and outputs a PDF file with the name `us_misery_plot.pdf`.

The plot has two axes. The horizontal axis are dates. The vertical axis are floating point values.

Include a `requirements.txt` file which specifies what the software requirements are to recreate your virtual environment.

## The Big Mac Index
The [Big Mac Index](https://en.wikipedia.org/wiki/Big_Mac_Index) is an informal measure of [purchasing power parity](https://en.wikipedia.org/wiki/Purchasing_power_parity) (PPP) between two currencies. Originally published by [The Economist newspaper](https://en.wikipedia.org/wiki/The_Economist) to "make exchange-rate theory a bit more digestible".

PPP produces an [inflation](https://en.wikipedia.org/wiki/Inflation) rate that is equal to the price of the basket of goods, in this case a Big Mac, at one location divided by the price of the basket of goods at a different location. On the other hand, there exists currency markets which are used to establish exchange rates between one currency and another and market-based indices that are used to determine the inflation rate. The PPP inflation and currency exchange rate may differ from the market exchange rate

The PPP inflation and exchange rate may differ from the market exchange rate due to poverty, tariffs, and other transaction costs.

Each Big Mac Index file has a three letter code which represents which country the data is for.

The USA data table has the price for a Big Mac in the U.S.A. Let's call the price given in that table as `us_price`. The data in the file has the following headings for each column:
* `date` - The date (year-month-day) that the data was collected
* `local_price` - The price of a Big Mac in that country in local currency.
* `dollar_ex` - The exchange rate, how much US$1 will buy of local currency
* `dollar_price` - The price of a Big Mac in that country in US dollars `(local_price / dollar_ex)`
* `dollar_ppp` - The implied purchasing power parity or in other words the implied exchange rate between the two currencies `local_price / us_price`
* `dollar_valuation` - The percent the local currency is over (+) or under (-) valued according when compared to a currency market exchange rate `((dollar_price / us_price ) / us_price) * 100` or `((dollar_ppp - dollar_ex) / dollar_ex) * 100`
* `dollar_adj_valuation` - The percent the local currency is over (+) or under (-) valued adjusted for GDP per person `(dollar_valuation + gdp_adjustement)`; `gdp_adjustment` is not given but can be derived from `dollar_valuation` and `dollar_adj_valuation`, `gdp_adjustment = dollar_valuation - dollar_adj_valuation`
* `euro_adj_valuation` - ignore this column
* `sterling_adj_valuation` - ignore this column
* `yen_adj_valuation` - ignore this column
* `yuan_adj_valuation` - ignore this column

## Minimum Wage
The [minimum wage](https://en.wikipedia.org/wiki/Minimum_wage) is the lowest amount of money that a worker can legally be paid. For example, the US Federal minimum wage is $7.25 with some [exceptions](https://www.dol.gov/agencies/whd/minimum-wage/faq) and [exemptions](https://webapps.dol.gov/elaws/whd/flsa/screen75.asp).

Although it is difficult to standardize [minimum wages in different countries](https://en.wikipedia.org/wiki/List_of_minimum_wages_by_country) and different labor markets, a second database, `Minnimum_Wage.csv`, is given with an approximation of minimum wages for the countries where the Big Mac Index data has been provided. The data in this file is the 3 letter country code (identical to the Big Mac Index) and the approximate minimum wage in 2017 adjusted US dollar. 

## Instructions
First create a plot where the horizontal axis are the years from 2000 to 2020 and the vertical axis is percent change expressed as a percentage. There is no need to plot the US data, instead plot a visible dashed line at the 0% line. For each country other than the US:

* Plot the `dollar_adj_valuation` as a solid line in unique and clearly distinguishable color.

* Plot the `dollar_valuation` in a stippled, dashed, or dotted-and-dashed line in the identical color used for `dollar_adj_valuation`.

* Create a legend for the plot

Output this plot as `big_mac_index_valuation.pdf`.

Next create a scatter plot using the GDP adjusted values, `dollar_adj_valuation`. In the plot label the horizontal axis as percentages. Mark the 0% line with a dashed black vertical line and label is 'US Dollar'. Plot uniquely colored points for each country other than the US. Create a legend for the plot.

Output this plot as `big_mac_index_scatter.pdf`.

Next create a series of plots that describes how many hours a worker must work to purchase 4 Big Macs in the year 2017 using the minimum wage data and the Big Mac Index data. To accomplish this, you must calculate some values before plotting.

For each country (including the US), collect the `dollar_price` for the Big Mac for the year 2017. If there is more than one data available, select the latest value. (For example data was collected in January and July of 2005, use July of 2005.) Next, calculate how many whole hours (no fractions or decimals) a worker must work to purchase 4 Big Macs.

With this data, make a bar char with the vertical axis the number of hours worked, the horizontal axis labels each bar with the country's name and each bar is labeled with number of hours worked and total earned.

Output this plot as `hours_worked_to_feed_a_family.pdf`.



