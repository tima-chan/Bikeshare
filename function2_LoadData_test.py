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
