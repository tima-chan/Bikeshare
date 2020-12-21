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
    print('_'*40)
