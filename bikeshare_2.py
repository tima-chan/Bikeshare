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
    a1 = ["both", "day", "month", "none"]
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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load filtered city data into a dataframe
    data_table = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    data_table['Start Time'] = pd.to_datetime(data_table['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    data_table['month'] = data_table['Start Time'].dt.month
    data_table['day_of_week'] = data_table['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        month = months.index(month)+1
        data_table = data_table[data_table['month'] == month]
    # Filter by day if applicable
    if day != 'all':
        data_table = data_table[data_table['day_of_week'] == day.title()]

    return data_table

def time_stats(data_table):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if data_table['month'].nunique() != 1:
        common_month = data_table['month'].mode()[0]
        print("The most common month is {}".format(common_month), "with count: ", data_table['month'].eq(common_month).sum())

    # display the most common day of week
    if data_table['day_of_week'].nunique() != 1:
        common_day = data_table['day_of_week'].mode()[0]
        print("The most common day of week is {}".format(common_day), "with count: ", data_table['day_of_week'].eq(common_day).sum())

    # display the most common start hour
    data_table['hour'] = data_table['Start Time'].dt.hour
    common_hour = data_table['hour'].mode()[0]
    print("The most common start hour is {}".format(common_hour), "with count: ", data_table['hour'].eq(common_hour).sum())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)

def station_stats(data_table):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = data_table['Start Station'].mode()[0]
    print("The most common start station is {}".format(common_start_station), "with count: ", data_table['Start Station'].eq(common_start_station).sum())

    # display most commonly used end station
    common_end_station = data_table['End Station'].mode()[0]
    print("The most common end station is {}".format(common_end_station), "with count: ", data_table['End Station'].eq(common_end_station).sum())

    # display most frequent combination of start station and end station trip
    data_table['Trip'] = "From " + data_table['Start Station'] + " To " + data_table['End Station']
    common_trip = data_table['Trip'].mode()[0]
    print("The most common trip is {}".format(common_trip), "with count: ", data_table['Trip'].eq(common_trip).sum())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)


def trip_duration_stats(data_table):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = data_table['Trip Duration'].sum()
    print("The total travel time is ",total_duration, " seconds.")

    # display mean travel time
    avg_duration = data_table['Trip Duration'].mean()
    print("The average travel time is ",avg_duration, " seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)


def user_stats(data_table):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = data_table['User Type'].value_counts()
    print("\nUser Type: Count:\n", user_type_count)

    # Display counts of gender
    if "Gender" in (data_table.columns):
        gender_count = data_table['Gender'].value_counts()
        print("\n\nGender count:\n", gender_count)

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in (data_table.columns):
        earliest_year = data_table['Birth Year'].min()
        recent_year = data_table['Birth Year'].max()
        common_year = int(data_table['Birth Year'].mode()[0])
        print("\n\nThe earliest birth year is ", earliest_year, "\nThe most recent birth year is ", recent_year, "\nThe most common birth year ", common_year, "with count: ", data_table['Birth Year'].eq(common_year).sum(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(data_table):

    # Get user response to whether display raw data or not
    q2 = input("\nWould you like to display the first 5 rows of raw data? Enter yes or no.\n").lower()
    a2 = ["yes", "no"]
    while q2 not in a2:
        print("Invalid input.\nEnter yes or no.\n")
        q2 = input("\nWould you like to display the first 5 rows of raw data? Enter yes or no.\n").lower()
    # Display requested raw data
    count_raw_data = 0
    if q2 == "yes":
        count_raw_data += 5
        print(data_table.head(count_raw_data+1))
        # Display more requests if any
        q3 = input("Display another 5 rows of raw data? Enter yes or no.\n").lower()
        while q3 == "yes":
            count_raw_data += 5
            print(data_table.head(count_raw_data+1))
            q3 = input("\nDisplay another 5 rows of raw data? Enter yes or no.\n").lower()
        while q3 not in a2:
            print("\nInvalid input.\nEnter yes or no.\n")
            q3 = input("\nDisplay another 5 rows of raw data? Enter yes or no.\n").lower()
            if q3 == "no":
                break



def main():
    while True:
        city, month, day = get_filters()
        data_table = load_data(city, month, day)

        time_stats(data_table)
        station_stats(data_table)
        trip_duration_stats(data_table)
        user_stats(data_table)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
