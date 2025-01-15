import pandas as pd
from docutils.parsers.rst.directives import percentage


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = race_count_calc(df)

    # What is the average age of men?
    average_age_men = avg_man_age_calc(df)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = percent_ppl_with_bachelors(df)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # percentage with salary >50K
    higher_education_rich = percent_high_edu_rich(df)
    lower_education_rich = percent_lower_edu_rich(df)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = round(df['hours-per-week'].min(), 1)


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = percent_min_hours_rich(df, min_work_hours)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = highest_percent_rich_country(df)[0]
    highest_earning_country_percentage = highest_percent_rich_country(df)[1]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = most_popular_occupation_india_rich(df)

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


def race_count_calc(df):
    race_df = df.loc[:,'race']
    return race_df.value_counts()

def avg_man_age_calc(df):
    men_df = df[df['sex'] == "Male"]
    avg_age_man = men_df.age.mean()
    return round(avg_age_man, 1)

def percent_ppl_with_bachelors(df):
    bachelors_df = df[df['education'] == "Bachelors"]
    len_bachelors = len(bachelors_df)
    len_df = len(df)
    percent = len_bachelors / len_df * 100
    return round(percent, 1)

def percent_high_edu_rich(df):
    higher_education = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    len_higher_education = len(higher_education)
    len_high_earn = len(higher_education[higher_education['salary'] == ">50K"])
    percent = len_high_earn / len_higher_education * 100
    return round(percent, 1)

def percent_lower_edu_rich(df):
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    len_lower_education = len(lower_education)
    lower_edu_high_earn = len(lower_education[lower_education['salary'] == ">50K"])

    lower_percent = (lower_edu_high_earn / len_lower_education) * 100
    return round(lower_percent, 1)

def percent_min_hours_rich(df, min_work_hours):
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    total_min_hours_workers = len(num_min_workers)
    high_earners_min_hours = len(num_min_workers[num_min_workers['salary'] == '>50K'])
    percentage_high_earners = (high_earners_min_hours / total_min_hours_workers) * 100
    return round(percentage_high_earners, 1)

# return name of country first than percent (name, percent)
def highest_percent_rich_country(df):
    high_earners = df[df['salary'] == '>50K']
    country_counts = df['native-country'].value_counts()
    high_earner_counts = high_earners['native-country'].value_counts()
    percentage_high_earners_country = high_earner_counts / country_counts * 100
    return percentage_high_earners_country.idxmax(), round(percentage_high_earners_country.max(), 1)

def most_popular_occupation_india_rich(df):
    india_df = df[df['native-country'] == 'India']
    high_earn_india = india_df[india_df['salary'] == '>50K']
    occupation = high_earn_india['occupation'].value_counts().idxmax()
    return occupation