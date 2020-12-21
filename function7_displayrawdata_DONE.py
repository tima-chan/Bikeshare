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
