# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt


def read(file_name):
    data = pd.read_csv(file_name)
    #data_transpose = data.transpose()
    return data


def data_filter(df_name):
    df_filtered = df_name[df_name["Country Name"].isin(data)]
    return df_filtered


def line_plot(df_name,title) :
    for i in range (len(year)):    
        plt.plot(df_name["Country Name"], df_name[year[i]], label = year[i])

    plt.xticks(rotation = 90)
    plt.title(title)
    plt.legend()
    plt.savefig("line.png", bbox_inches="tight", dpi = 300)
    plt.show()
    
df_liq = read("CO2_emissions_from_liquid_fuel_consumption.csv")
df_solid = read("CO2 emissions from solid fuel consumption.csv")
df_power_cons = read("Electric power consumption.csv")
df_urban_population = read("Urban Population.csv")


year = ["2007","2008","2009","2010"]
data = ["Belgium","United Kingdom","France","India",
        "Brazil","Costa Rica","Bangladesh","Zimbabwe","Zambia"]

df_to_be_plotted1 = data_filter(df_solid)
df_to_be_plotted2 = data_filter(df_urban_population)
df_to_be_plotted3 = data_filter(df_liq )


line_plot(df_to_be_plotted2,"Urban Population")
line_plot(df_to_be_plotted1,"CO2 emissions from solid fuel consumption")
line_plot(df_to_be_plotted3,"CO2 emissions from liquid fuel consumption") 




