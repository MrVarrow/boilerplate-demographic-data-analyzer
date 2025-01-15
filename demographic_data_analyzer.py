import pandas as pd
from docutils.parsers.rst.directives import percentage


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    print(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df.loc[:,'race']
    race = race.value_counts()
    print(race)
    race_count = race

    # What is the average age of men?
    men_df = df[df['sex'] == "Male"]
    avg_age_man = men_df.age.mean()
    avg_age_man = round(avg_age_man, 1)
    average_age_men = avg_age_man


    # What is the percentage of people who have a Bachelor's degree?
    bl_df = df[df['education'] == "Bachelors"]
    len_bl = len(bl_df)
    len_df = len(df)
    percent = len_bl / len_df * 100
    rounded_percent = round(percent, 1)
    percentage_bachelors = rounded_percent

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    len_high = len(higher_education)
    print(len_high)
    len_high_earn = len(higher_education[higher_education['salary'] == ">50K"])
    perc = len_high_earn / len_high * 100
    rounded_perc = round(perc, 1)
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    len_lower_edu = len(lower_education)
    lower_high_earn = len(lower_education[lower_education['salary'] == ">50K"])

    lower_percent = lower_high_earn / len_lower_edu * 100
    rounded_lower_percent = round(lower_percent, 1)

    # percentage with salary >50K
    higher_education_rich = rounded_perc
    lower_education_rich = rounded_lower_percent

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = round(df['hours-per-week'].min(), 1)


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    total_min_hours_workers = len(num_min_workers)
    high_earners_min_hours = len(num_min_workers[num_min_workers['salary'] == '>50K'])
    percentage_high_earners = (high_earners_min_hours / total_min_hours_workers) * 100


    rich_percentage = round(percentage_high_earners, 1)

    # What country has the highest percentage of people that earn >50K?
    high_earners = df[df['salary'] == '>50K']
    country_counts = df['native-country'].value_counts()
    high_earner_counts = high_earners['native-country'].value_counts()
    percentage_high_earners_country = high_earner_counts / country_counts * 100

    highest_earning_country = percentage_high_earners_country.idxmax()
    highest_earning_country_percentage = round(percentage_high_earners_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df['native-country'] == 'India']
    high_earn_india = india_df[india_df['salary'] == '>50K']
    occupation_count = high_earn_india['occupation'].value_counts().idxmax()
    top_IN_occupation = occupation_count

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
