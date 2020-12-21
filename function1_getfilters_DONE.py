"""
    This script is a project that displays some descriptive statistics for
    a sample of the bikeshare system US provider Motivate data. It's the first
    Udacity professional track project.

    Student: Fatimah Ehab Farouk Mohammed
    """
import pandas as pd
import numpy as np
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["sunday", "saturday", "monday", "tuesday", "wednesday", "thursday", "friday", "all"]
a1 = ["both", "day", "month", "none"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york, washington).
    city = input("Pick a city you want to analyze: Chicago, New York or Washington\n").lower()
    while city not in CITY_DATA.keys():
        print("Invalid input.\nMake sure you type only 1 city of the 3 mentioned above.")
        city = input("Pick a city you want to analyze: Chicago, New York or Washington\n").lower()

    #get user input for data filter (day, month, both, none)
    q1 = input("Would you like to filter the data by day, month, both or none?\n").lower()
    while q1 not in a1:
        print("Invalid input.")
        q1 = input("Would you like to filter the data by day, month, both or none?\n").lower()
    if q1 == "both":
        month = input("Which month? January, February, March, April, May or June?\n").lower()
        while month not in months:
            print("Invalid input.\nMake sure you type only 1 month of the 6 mentioned above.")
            month = input("Which month? January, February, March, April, May or June?\n").lower()
        day = input("Which day?\n").lower()
        while day not in days:
            print("Invalid input.\nMake sure you type a weekday.")
            day = input("Which day?\n").lower()
    elif q1 == "day":
        month = "all"
        day = input("Which day?\n").lower()
        while day not in days:
            print("Invalid input.\nMake sure you type a weekday.")
            day = input("Which day?").lower()
    elif q1 == "month":
        day = "all"
        month = input("Which month? January, February, March, April, May or June?\n").lower()
        while month not in months:
            print("Invalid input.\nMake sure you type only 1 month of the 6 mentioned above.")
            month = input("Which month? January, February, March, April, May or June?\n").lower()
    elif q1 == "none":
        month = "all"
        day = "all"

    print('_'*40)
    return city, month, day

print(get_filters())
