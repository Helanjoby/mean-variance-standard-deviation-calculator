import pandas as pd

def calculate_demographic_data(print_data=True):
    # Column names
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ]

    # Read CSV and add column names
    df = pd.read_csv("adult.data.csv", names=column_names)

    # Strip leading/trailing spaces from all string columns
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage with advanced education (>50K)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    if not num_min_workers.empty:
        rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)
    else:
        rich_percentage = 0

    # 7. Country with highest percentage earning >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    country_percentages = country_salary / country_total * 100

    if not country_percentages.empty:
        highest_earning_country = country_percentages.idxmax()
        highest_earning_country_percentage = round(country_percentages.max(), 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = 0

    # 8. Most popular occupation for >50K earners in India
    india_rich = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    if not india_rich.empty:
        top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
    else:
        top_IN_occupation = None

    # Print results if requested
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education earning >50K:", higher_education_rich)
        print("Percentage without higher education earning >50K:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich in country:", highest_earning_country_percentage)
        print("Top occupations in India for rich:", top_IN_occupation)

    # Return values for testing
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }