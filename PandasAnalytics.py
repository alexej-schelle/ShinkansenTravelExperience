################################################################################################################################################
#                                                                                                                                              #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE for Analytics of SurveyData.csv with support of W3Schools.com and GPT-Language-Model 3.5 #

import os
import sys

import pandas as pd
import numpy as np

from functools import reduce

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('SurveyData.csv')

# Code for printing to a file
sample = open('ResultData.txt', 'w')

# Display the first few rows of the DataFrame
print(df.head())
print(df.count())

print(' ')

# Calculate Number of Elements for Logic Variable "Seat_comfort"
reduced_df = df['Seat_comfort'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Seat_comfort in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Seat_Class"
reduced_df = df['Seat_Class'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Seat_Class in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Arrival_time_convenient"
reduced_df = df['Arrival_time_convenient'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Arrival_time_convenient in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Catering'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Catering in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Platform_location'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Platform_location in the columns:", class_counts, file = sample)
print(class_counts)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Onboardwifi_service'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Onboardwifi_service in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Onboard_entertainment'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Onboard_entertainment in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Online_support'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Online_support in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Onlinebooking_Ease'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Onlinebooking_Ease in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Onboard_service'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Onboard_service in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Leg_room'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Leg_room in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Baggage_handling'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Baggage_handling in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Checkin_service'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Checkin_service in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Cleanliness'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Cleanliness in the columns:", class_counts, file = sample)

print(' ')

# Calculate Number of Elements for Logic Variable "Catering"
reduced_df = df['Online_boarding'].copy()

class_counts = reduced_df.value_counts()
print("Number of elements per class Online_boarding in the columns:", class_counts, file = sample)

print(' ')
print('Calculating mean Seat_comfort...')
print(' ')

reduced_df_Seat_comfort = []
reduced_df_Seat_Class = []
reduced_df_Arrival_time_convenient = []
reduced_df_Catering = []
reduced_df_Platform_location = []
reduced_df_Onboardwifi_service = []
reduced_df_Onboard_entertainment = []
reduced_df_Online_support = []
reduced_df_Onlinebooking_Ease = []
reduced_df_Onboard_service = []
reduced_df_Leg_room = []
reduced_df_Baggage_handling = []
reduced_df_Checkin_service = []
reduced_df_Cleanliness = []
reduced_df_Online_boarding = []

# Quantitative Model for Converted Logic Variable Seat_Comfort

reduced_df = df[['ID', 'Seat_comfort']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Seat_comfort'

mean_value = reduced_df['Seat_comfort'].mean()
std_value = reduced_df['Seat_comfort'].std()

print("Mean value for numeric Seat_Comfort: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Seat_comfort = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Seat_Class

reduced_df = df[['ID', 'Seat_Class']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'Green Car': 5.0, 'Ordinary': 6.0})

# Calculate Mean Values for Numeric Variable 'Seat_Class'

mean_value = reduced_df['Seat_Class'].mean()
std_value = reduced_df['Seat_Class'].std()

print("Mean value for numeric Seat_Class: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Seat_Class = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Catering

reduced_df = df[['ID', 'Catering']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Catering'

mean_value = reduced_df['Catering'].mean()
std_value = reduced_df['Catering'].std()

print("Mean value for numeric Catering: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Catering = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Platform_location

reduced_df = df[['ID', 'Platform_location']].copy()
reduced_df = reduced_df.replace({'manageable': 1.0, 'Convinient': 2.0, 'need improvement': 3.0, 'Inconvinient': 4.0, 'very convinient': 5.0, 'very inconvinient': 6.0})

# Calculate Mean Values for Numeric Variable 'Platform_location'

mean_value = reduced_df['Platform_location'].mean()
std_value = reduced_df['Platform_location'].std()

print("Mean value for numeric Platform_location: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Platform_location = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Onboardwifi_service

reduced_df = df[['ID', 'Onboardwifi_service']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Onboardwifi_service'

mean_value = reduced_df['Onboardwifi_service'].mean()
std_value = reduced_df['Onboardwifi_service'].std()

print("Mean value for numeric Onboardwifi_service: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Onboardwifi_service = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Onboardwifi_service

reduced_df = df[['ID', 'Onboard_entertainment']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Onboard_entertainment'

mean_value = reduced_df['Onboard_entertainment'].mean()
std_value = reduced_df['Onboard_entertainment'].std()

print("Mean value for numeric Onboard_entertainment: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Onboard_entertainment = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Online_support

reduced_df = df[['ID', 'Online_support']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Online_support'

mean_value = reduced_df['Online_support'].mean()
std_value = reduced_df['Online_support'].std()

print("Mean value for numeric Online_support: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Online_support = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Online_support

reduced_df = df[['ID', 'Onlinebooking_Ease']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Online_support'

mean_value = reduced_df['Onlinebooking_Ease'].mean()
std_value = reduced_df['Onlinebooking_Ease'].std()

print("Mean value for numeric Onlinebooking_Ease: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Onlinebooking_Ease = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Online_support

reduced_df = df[['ID', 'Onboard_service']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Online_support'

mean_value = reduced_df['Onboard_service'].mean()
std_value = reduced_df['Onboard_service'].std()

print("Mean value for numeric Onboard_service: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Onboard_service = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Online_support

reduced_df = df[['ID', 'Leg_room']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Online_support'

mean_value = reduced_df['Leg_room'].mean()
std_value = reduced_df['Leg_room'].std()

print("Mean value for numeric Onboard_service: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Leg_room = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Baggage_handling

reduced_df = df[['ID', 'Baggage_handling']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0})

# Calculate Mean Values for Numeric Variable 'Baggage_handling'

mean_value = reduced_df['Baggage_handling'].mean()
std_value = reduced_df['Baggage_handling'].std()

print("Mean value for numeric Baggage_handling: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Baggage_handling = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Checkin_service

reduced_df = df[['ID', 'Checkin_service']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Cleanliness'

mean_value = reduced_df['Checkin_service'].mean()
std_value = reduced_df['Checkin_service'].std()

print("Mean value for numeric Cleanliness: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Checkin_service = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Cleanliness

reduced_df = df[['ID', 'Cleanliness']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Checkin_service'

mean_value = reduced_df['Cleanliness'].mean()
std_value = reduced_df['Cleanliness'].std()

print("Mean value for numeric Cleanliness: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Cleanliness = pd.DataFrame(reduced_df)

# Quantitative Model for Converted Logic Variable Cleanliness

reduced_df = df[['ID', 'Online_boarding']].copy()
reduced_df = reduced_df.replace({'excellent': 1.0, 'good': 2.0, 'acceptable': 3.0, 'need improvement': 4.0, 'poor': 5.0, 'extremely poor': 6.0})

# Calculate Mean Values for Numeric Variable 'Checkin_service'

mean_value = reduced_df['Online_boarding'].mean()
std_value = reduced_df['Online_boarding'].std()

print("Mean value for numeric Online_boarding: ", mean_value, ' +/- ', std_value, file = sample)
print(' ')

reduced_df_Online_boarding = pd.DataFrame(reduced_df)

# Form numeric matrix from columns
corr_matrix = pd.merge(reduced_df_Cleanliness, reduced_df_Onboard_service, on='ID', how='inner')

print(corr_matrix)

# Calculate covariance matrix
cov_matrix = corr_matrix.cov()

# Calculate Pearson correlation matrix
pearson_correlation_matrix = corr_matrix.corr(method='pearson')

# Calculate Spearman correlation matrix
spearman_correlation_matrix = corr_matrix.corr(method='spearman')

# Slicing and output the Dataframe into the file 'ResultData.txt'  
print(cov_matrix.iloc[0:12, 0:12], file = sample)
print(pearson_correlation_matrix.iloc[0:12, 0:12], file = sample)
print(spearman_correlation_matrix.iloc[0:12, 0:12], file = sample)

print(pearson_correlation_matrix)

sample.close()

# reduced_df_Seat_comfort = []
# reduced_df_Seat_Class = []
# reduced_df_Arrival_time_convenient = []
# reduced_df_Catering = []
# reduced_df_Platform_location = []
# reduced_df_Onboardwifi_service = []
# reduced_df_Onboard_entertainment = []
# reduced_df_Online_support = []
# reduced_df_Onlinebooking_Ease = []
# reduced_df_Onboard_service = []
# reduced_df_Leg_room = []
# reduced_df_Baggage_handling = []
# reduced_df_Checkin_service = []
# reduced_df_Cleanliness = []
# reduced_df_Online_boarding = []