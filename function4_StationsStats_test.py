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
