# This is a mini python project that seeks to explore temperature trends 
# of different cities. The project is based of a weather dataset 
# 'weather_data.csv' found in this directory.

# Importing neccessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import re
import os

# Read in dataset into pandas.DataFrame df
df = pd.read_csv('weather_data.csv')


def display_array(array):
    ''' This function displays arrays in a neatly formatted way on the 
        terminal. It prints 10 array items at a time.

    Args: 
        array (np.ndarray): The array to be displayed on the terminal
    '''
    print()
    if len(array) == 0: print('You have no data to view!\n')

    count = 0
    index = 0
    while index < len(array):
        print(array[index])

        count += 1
        index += 1
        if count == 10:
            user_input = input('\nClick "Enter" for more or Enter "q" to terminate: ')
            print()

            if user_input.lower() == 'q':
                break
            else:
                count = 0
                continue

    time.sleep(2)


def display_temperature_trend(city):
    ''' This function uses matplotlib.pyplot.errorbar() function to display
        temperature trend for a particular city as a line chart.

    Args: 
        city (str): The name of the city
    '''
    df_city = df.query('city == @city')
    if df_city.shape[0] == 0:
        print('\nYou have no data for {}.\n'.format(city))
        time.sleep(1)
        return
    
    # Create bin egdes that will be used to create intervals 
    bin_size = 10 
    bin_edges = np.arange(df_city['year'].min(), df_city['year'].max()+bin_size, bin_size)

    # This are the mid points of the bins
    bin_mids = bin_edges[:-1] + int(bin_size/2)

    # Create intervals that will be used to group data
    bin_intervals = pd.cut(df_city['year'], bin_edges)

    # Find mean avg_temp for each bin_interval
    bin_interval_means = df_city.groupby(bin_intervals)['avg_temp'].mean()

    # Plot line chart 
    plt.errorbar(bin_mids, bin_interval_means)
    plt.title('Temperature trend for {}'.format(city))
    plt.xlabel('Year')
    plt.ylabel('Average Temperature')
    plt.show()


def country_handler():
    ''' This function handles all country commands '''

    print('\n\n  Enter "0" (zero) to view all countries in dataset.')
    print('  Enter text to search for countries begining with text.\n  E.g, "N", "Ni", "Nig" all searchs for countries that begin with "N", "Ni", "Nig" respectively.')
    
    user_input = input('\nOption: ')

    countries = np.array([])
    if user_input == "0":
        countries = np.sort(df['country'].unique())
    else:
        countries = np.sort(df[df['country'].str.match('^'+user_input, 
                        case=False, flags=re.IGNORECASE)]['country'].unique())

    display_array(countries)

def city_handler():
    ''' This function handles all city commands '''

    print('\n\n  Enter "0" (zero) to view all cities in dataset.')
    print('  Enter "1" to view all cities of a particular country.')
    print('  Enter "2" to search for particular city with text.')
    print('  Enter "3" to view city temperature trend.')

    user_input = input('\nOption: ')
    
    if user_input == '0':
        cities = np.sort(df['city'].unique())
        display_array(cities)
    elif user_input == '1':
        country = input('Please enter country name: ')
        cities = np.sort(df.query('country == @country')['city'].unique())
        display_array(cities)
    elif user_input == '2':
        search_text = input('Please enter search text: ')
        cities = np.sort(df[df['city'].str.match('^'+search_text, 
                        case=False, flags=re.IGNORECASE)]['city'].unique())
        display_array(cities)
    elif user_input == '3':
        city = input('Please enter city name: ')
        display_temperature_trend(city)
    else:
        print('\nOops! You have made an incorrect entry.')


# Welcome message
print('\nHello human!\n\nThis is cybertron your city temperature dataset guide.\nI will be here to help you explore temperature trend of your favorite city.\n')
time.sleep(3)

# While loop that keeps the program running in the terminal until a specific 
# terminating key is entered
while True:
    print('\nWhat would you like to do?')
    print('  Enter "1" to view 10 randon sample of dataset.')
    print('  Enter "2" to view countries available in dataset.')
    print('  Enter "3" to view cities available in dataset.')
    print('  Enter "4" to view dataset year range.')
    print('  Enter "5" to clear screen.')
    print('  Enter "6" or "Q" to terminate program.')

    print('\nEnter option below and click "Enter" on you keyboard to execute.')

    user_input = input('\nOption: ')

    if user_input == '1':
        print('\n')
        print(df.sample(10))
        print('\n')
        time.sleep(2.5)
    elif user_input == '2':
        country_handler()
    elif user_input == '3':
        city_handler()
    elif user_input == '4':
        print('\nYour dataset spanned for {} years.\nMin year = {}\nMax year = {}'
            .format(df['year'].max() - df['year'].min(), df['year'].min(), df['year'].max()))
        time.sleep(2.5)
    elif user_input == '5':
        os.system('cls')
    elif user_input == '6' or user_input.lower() == 'q':
        break
    else:
        print('\nOops! You have made an incorrect entry, try again.')
        time.sleep(1.5)
