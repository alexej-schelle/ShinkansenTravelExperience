################################################################################################################################################
#                                                                                                                                              #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE for Analytics of TravelData.csv developed with partial technical support of W3Schools.com and GPT-Language-Model 3.5 #

# Analyse von Sitzklasse und Sitzkomfort

import os
import sys

import numpy as np
import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('TravelData.csv')
dfs = pd.read_csv('SurveyData.csv')

# Code for printing to a file
result_inner = pd.merge(df, dfs, on='ID', how='inner')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 1.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for one minute delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 2.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for two minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 5.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for five minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 10.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for ten minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 15.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for fiveteen minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 25.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 25 minute delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 50.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 50.0 minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 120.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 120 minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 240.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 240 minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['DepartureDelay_in_Mins'] > 360.0].copy()
number_of_delays = reduced_df['DepartureDelay_in_Mins'].count()
total_number = result_inner['DepartureDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 360 minutes delay ')

print(' ')
print(' ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 1.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for one minute delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 2.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for two minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 5.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for five minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 10.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for ten minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 15.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for fiveteen minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 25.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 25 minute delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 50.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 50.0 minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 120.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 120 minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 240.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 240 minutes delay ')

# Unterscheidung als Numerische und Logische VariablenTypen
reduced_df = result_inner[result_inner['ArrivalDelay_in_Mins'] > 360.0].copy()
number_of_delays = reduced_df['ArrivalDelay_in_Mins'].count()
total_number = result_inner['ArrivalDelay_in_Mins'].count()
print(number_of_delays/total_number*100.0, ' for 360 minutes delay ')

print(' ')
print(' ')
