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
    print('-'*40)
