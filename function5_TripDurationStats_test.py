
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = data_table['Trip Duration'].sum()
    print("The total travel time is ",total_duration)

    # display mean travel time
    avg_duration = data_table['Trip Duration'].mean()
    print("The average travel time is ",avg_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
