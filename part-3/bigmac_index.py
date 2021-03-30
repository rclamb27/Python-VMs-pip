#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-10-22
#rclamb27@csu.fullerton.edu
"""Takes an argument and loops through files to create plots"""
import csv
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
#has a pylitn error for this but like literally the code wont run if I take this out?

def main():
    """main function"""
    if len(sys.argv) < 2:
        print("Needs an filename as an argument.")
        sys.exit(1)
    if sys.argv[1] != "Minnimum_Wage.csv":
        print("Needs Minnimum_Wage.csv to be the file inputed to loop through the other cvs files")
        sys.exit(1)

    #List initialization and variable initialization

    first = 0
    country = []
    min_wage = []
    with open(sys.argv[1]) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if first != 0:
                country.append(row[0])
                min_wage.append(float(row[1]))
            else:
                first += 1

    list = {"CAN" : [], "USA" : [], "NZL" : [], "MEX" : [], "JPN" : [], "DEU" : [], "CHN" : []}

    for country_label in country:
        dates = []
        local_price = []
        dollar_ex = []
        dollar_price = []
        dollar_ppp = []
        dollar_valuation = []
        dollar_adj_valuation = []
        zero = []
        first = 0
        file = "ECONOMIST-BIGMAC_{}.csv".format(country_label)
        with open(file) as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if first != 0:
                    dates.append(row[0])
                    local_price.append(float(row[1]))
                    dollar_ex.append(float(row[2]))
                    dollar_price.append(float(row[3]))
                    dollar_ppp.append(float(row[4]))
                    dollar_valuation.append(float(row[5]))
                    if row[6] != '':
                        dollar_adj_valuation.append(float(row[6]))
                    else:
                        dollar_adj_valuation.append(float("0"))

                    zero.append(0)
                else:
                    first += 1
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
        list[country_label] = [dates, local_price, dollar_ex, dollar_price,
                               dollar_ppp, dollar_valuation, dollar_adj_valuation]

    #############################################################
    fig, axis = plt.subplots(figsize=(10, 10), constrained_layout=True)
    axis.set(title="Big Mac Index Valuation")
    #Canada
    axis.plot(list["CAN"][0], list["CAN"][6], color='blue', label='dollar adj valuation for CAN')
    axis.plot(list["CAN"][0], list["CAN"][5], dashes=[4, 3], color='blue',
              label='dollar valuation for CAN')
    #China
    axis.plot(list["CHN"][0], list["CHN"][6], color='yellow', label='dollar adj valuation for CHN')
    axis.plot(list["CHN"][0], list["CHN"][5], dashes=[4, 3], color='yellow',
              label='dollar valuation for CHN')
    #DEU
    axis.plot(list["DEU"][0], list["DEU"][6], color='orange', label='dollar adj valuation for DEU')
    axis.plot(list["DEU"][0], list["DEU"][5], dashes=[4, 3], color='orange',
              label='dollar valuation for DEU')
    #JPN
    axis.plot(list["JPN"][0], list["JPN"][6], color='red', label='dollar adj valuation for JPN')
    axis.plot(list["JPN"][0], list["JPN"][5], dashes=[4, 3], color='red',
              label='dollar valuation for JPN')
    #MEX
    axis.plot(list["MEX"][0], list["MEX"][6], color='green', label='dollar adj valuation for MEX')
    axis.plot(list["MEX"][0], list["MEX"][5], dashes=[4, 3], color='green',
              label='dollar valuation for MEX')
    #NZL
    axis.plot(list["NZL"][0], list["NZL"][6], color='purple', label='dollar adj valuation for NZL')
    axis.plot(list["NZL"][0], list["NZL"][5], dashes=[4, 3], color='purple',
              label='dollar valuation for NZL')
    #USA
    axis.plot(list["USA"][0], zero, color='black', label='US Data')
    #OTHER Plot STUFF
    axis.legend()
    axis.set(xlabel='Dates', ylabel='Percentages')
    plt.margins(0)
    print('Writing plot to big_mac_index_valuation.pdf')
    fig.savefig("big_mac_index_valuation.pdf")
    plt.close()
    #############################################################
    fig, axis = plt.subplots(figsize=(10, 10), constrained_layout=True)
    axis.set(title="Big Mac Scatter")
    #USA dollar
    axis.plot(zero, list["USA"][0], dashes=[4, 3], color='black', label='US Dollar')
    #Canada
    axis.scatter(list["CAN"][6], list["CAN"][0], color='blue', label='CAN dollar_adj_valuation')
    #China
    axis.scatter(list["CHN"][6], list["CHN"][0], color='yellow', label='CHN dollar_adj_valuation')
    #DEU
    axis.scatter(list["DEU"][6], list["DEU"][0], color='orange', label='DEU dollar_adj_valuation')
    #JPN
    axis.scatter(list["JPN"][6], list["JPN"][0], color='red', label='JPN dollar_adj_valuation')
    #MEX
    axis.scatter(list["MEX"][6], list["MEX"][0], color='green', label='MEX dollar_adj_valuation')
    #NZL
    axis.scatter(list["NZL"][6], list["NZL"][0], color='purple', label='NZL dollar_adj_valuation')
    #OTHER Plot STUFF
    #axis.get_yaxis().set_visible(False) Unclear if there
    #is supposed to be a y-axis or not? says label only horizontal in README
    axis.legend()
    axis.set(xlabel='Percentages')
    plt.margins(0)
    print('Writing plot to big_mac_index_scatter.pdf')
    fig.savefig("big_mac_index_scatter.pdf")
    plt.close()
    #############################################################
    dollaryear = []
    for country_name in country:
        index = 0
        count = 0
        for date in list[country_name][0]:
            if date.year == 2017:
                count += 1
            elif date.year != 2017 and count >= 1:
                dollaryear.append(list[country_name][3][index])
                count = 0
            index += 1

    perhour = []
    index2 = 0
    for i in dollaryear:
        number = i *4
        perhour.append(number // min_wage[index2])
        index2 += 1
    #############################################################
    fig, axis = plt.subplots(figsize=(10, 10), constrained_layout=True)
    axis.set(title="4 Big Mac Hours to be able to Purchase in 2017")
    axis.bar(country, perhour, color='green')

    axis.set(xlabel='Countrys Name', ylabel='Number of Hours Worked')
    plt.margins(0)
    print('Writing plot to hours_worked_to_feed_a_family.pdf')
    fig.savefig("hours_worked_to_feed_a_family.pdf")
    plt.close()
    #############################################################


if __name__ == "__main__":
    main()
