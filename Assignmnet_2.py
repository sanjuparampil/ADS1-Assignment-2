# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt


def read(file_name):
    """This function is used to read the file and return the 2 dataframes"""
    data = pd.read_csv(file_name)
    #data_transpose = data.transpose()
    return data


def data_filter(df_name):
    """This function is used to filter the data from the dataframe"""
    df_filtered = df_name[df_name["Country Name"].isin(data)]
    return df_filtered


def line_plot(df_name,title) :
    """This function is used to plot line graph"""
    for i in range (len(year)):    
        plt.plot(df_name["Country Name"], df_name[year[i]], label = year[i])
    
    plt.xticks(rotation = 90)
    plt.title(title)
    plt.legend()
    plt.savefig("line.png", bbox_inches="tight", dpi = 300)
    plt.show()
    
def barplot(df_name,title):
    """This function is used to plot bar graph"""
    raw_data = data_filter(df_name)
    pwr_consumption_fltrd = raw_data.set_index("Country Name")
    df = pd.DataFrame({'2000': pwr_consumption_fltrd["2000"],
                       '2005': pwr_consumption_fltrd["2005"],
                       '2010': pwr_consumption_fltrd["2010"],
                       '2014': pwr_consumption_fltrd["2014"]},index=pwr_consumption_fltrd.index)
    df.plot.bar()
    plt.title(title) 
    return df

#calling read function giving filename as parameter
df_liq = read("CO2_emissions_from_liquid_fuel_consumption.csv")

#calling read function giving filename as parameter
df_solid = read("CO2 emissions from solid fuel consumption.csv")

#calling read function  giving filename as parameter
df_power_cons = read("Electric power consumption.csv")

#calling read function  giving filename as parameter
df_urban_population = read("Urban Population.csv")


year = ["2000","2005","2010","2014"]
data = ["Belgium","United Kingdom","France","India",
        "Brazil","Costa Rica","Bangladesh","Zimbabwe","Zambia"]

df_to_be_plotted1 = data_filter(df_solid)
df_to_be_plotted2 = data_filter(df_urban_population)
df_to_be_plotted3 = data_filter(df_liq )


line_plot(df_to_be_plotted2,"Urban Population")
line_plot(df_to_be_plotted1,"CO2 emissions from solid fuel consumption")
line_plot(df_to_be_plotted3,"CO2 emissions from liquid fuel consumption") 

barplot(df_power_cons,"power consumption")



