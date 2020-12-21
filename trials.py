
import pandas as pd
import numpy as np
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["sunday", "saturday", "monday", "tuesday", "wednesday", "thursday", "friday", "all"]
a1 = ["both", "day", "month", "none"]

# city, month, day = get_filters()
# data_table = load_data(city, month, day)
# print(data_table)


def display_raw_data(data_table):

    # Get user response to whether display raw data or not
    q2 = input("\nWould you like to display the first 5 rows of raw data?\n").lower()
    a2 = ["yes", "no"]
    while q2 not in a2:
        print("Invalid input.")
        q2 = input("\nWould you like to display the first 5 rows of raw data?\n").lower()
    # Display requested raw data
    count_raw_data = 0
    if q2 == "yes":
        count_raw_data += 5
        print(data_table.head(count_raw_data+1))
        # Display more requests if any
        q3 = input("Display another 5 rows of raw data?\n").lower()
        while q3 == "yes":
            count_raw_data += 5
            print(data_table.head(count_raw_data+1))
            q3 = input("\nDisplay another 5 rows of raw data?\n").lower()
        while q3 not in a2:
            print("\nInvalid input.")
            q3 = input("\nDisplay another 5 rows of raw data?\n").lower()
            if q3 == "no":
                break
