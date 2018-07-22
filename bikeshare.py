import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '\\data\\chicago.csv',
              'new york city': '\\data\\new_york_city.csv',
              'washington': '\\data\\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').strip().lower()
        if city in CITY_DATA.keys():
            break 
        else:
            print('Invalid Input')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? January, February, March, April, May, June or all?\n').strip().lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break 
        else:
            print('Invalid Input')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n').strip().lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']:
            break 
        else:
            print('Invalid Input')

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['total_trip'] = df['Start Station'] + " to " + df['End Station']
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_index = df['month'].value_counts().idxmax()
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month is {}'.format(months[month_index-1]))

    # display the most common day of week
    print('The most common day of the week is {}'.format(df['day_of_week'].value_counts().idxmax()))

    # display the most common start hour
    print('The most common start hour is {}'.format(df['Start Time'].dt.hour.value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common Start Station is {}'.format(df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print('The most common End Station is {}'.format(df['Start Station'].value_counts().idxmax()))

    # display most frequent combination of start station and end station trip
    print('The most common Trip is {}'.format(df['total_trip'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_sum = int(df['Trip Duration'].sum())
    total_minutes = int(total_sum/60)
    total_seconds = int(total_sum%60)

    print('Total travel time is {} minutes {} seconds'.format(total_minutes,total_seconds))

    # display mean travel time
    total_mean = int(df['Trip Duration'].mean())
    mean_minutes = int(total_mean/60)
    mean_seconds = int(total_mean%60)
    print('Mean travel time is {} minutes {} seconds'.format(mean_minutes,mean_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of user types \n{}\n'.format(df['User Type'].value_counts().to_string()))


    # Display counts of gender
    if 'Gender' in df.columns:
        print('Count of genders \n{}\n'.format(df['Gender'].value_counts().to_string()))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Birth year is {}'.format(df['Birth Year'].min().astype(int)))
        print('Most Recent Birth year is {}'.format(df['Birth Year'].max().astype(int)))
        print('Most Common Birth year is {}'.format(df['Birth Year'].mode()[0].astype(int)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display raw data on bikeshare users"""

    while True:
        try:
            row = input('\n How many rows of data would you like to print? Please enter an integer\n')
            row = int(row)
            print(df.iloc[:row])
            break
        except:
             print("\n Error with input, please try again")

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes to restart, enter any other value to end.\n')
        if restart.strip().lower() != 'yes':
            break


if __name__ == "__main__":
	main()
