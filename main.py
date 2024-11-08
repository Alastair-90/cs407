import warnings
import pandas as pd
from verispy import VERIS
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)

data_dir = "C:\\Users\\bain2\\PHPDataset"
veris = VERIS(data_dir)
data = pd.DataFrame(veris.json_to_df(verbose=False))

warnings.resetwarnings()

def plotYearAmount():
    yearCounts = allYears.value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    plt.plot(yearCounts.index, yearCounts.values, marker='o', color='skyblue')
    plt.fill_between(yearCounts.index, yearCounts.values, alpha=0.5, color='skyblue')
    plt.title('Number of Incidents by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Incidents')
    plt.xticks(yearCounts.index, rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotAverageIncidentsPerMonth():
    monthlyCounts = data['timeline.incident.month'].value_counts().sort_index()
    averageMonthlyCounts = monthlyCounts / allYears.nunique()

    plt.figure(figsize=(10, 6))
    plt.plot(averageMonthlyCounts.index, averageMonthlyCounts.values, marker='o', color='skyblue')
    plt.fill_between(averageMonthlyCounts.index, averageMonthlyCounts.values, alpha=0.5, color='skyblue')
    plt.title('Average Number of Incidents for Each Month ')
    plt.xlabel('Month')
    plt.ylabel('Average Number of Incidents')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

    # Set y-axis to start slightly below the minimum average count
    ymin = max(0, averageMonthlyCounts.min() - 0.5)  # Avoid negative values, use 0 if min is very low
    plt.ylim(ymin, averageMonthlyCounts.max() + 1)  # Add some padding above the maximum value

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plotAverageIncidentsPerDaySingle():
    # Count incidents by day of the month across all months and years
    dailyCounts = data['timeline.incident.day'].value_counts().sort_index()

    # Calculate the average by dividing by the number of years (assuming `allYears` has unique years)
    averageDailyCounts = dailyCounts / allYears.nunique()

    plt.figure(figsize=(10, 6))
    plt.plot(averageDailyCounts.index, averageDailyCounts.values, marker='o', color='skyblue')
    plt.fill_between(averageDailyCounts.index, averageDailyCounts.values, alpha=0.5, color='skyblue')
    plt.title('Average Number of Incidents for Each Day of the Month')
    plt.xlabel('Day')
    plt.ylabel('Average Number of Incidents')
    plt.xticks(range(1, 32))  # Days range from 1 to 31

    # Set y-axis to start slightly below the minimum average count
    ymin = max(0, averageDailyCounts.min() - 0.5)  # Avoid negative values, use 0 if min is very low
    plt.ylim(ymin, averageDailyCounts.max() + 1)   # Add some padding above the maximum value

    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotMonthByYear():
    plt.figure(figsize=(10, 6))
    for year in allYears.sort_values().unique():
        monthCounts = data[data['timeline.incident.year'] == year]['timeline.incident.month'].value_counts().sort_index()
        fullMonthCounts = monthCounts.reindex(range(1, 13), fill_value=0) # if no values the add it with 0
        plt.plot(fullMonthCounts.index, fullMonthCounts.values,label=int(year),marker='o')
        plt.fill_between(fullMonthCounts.index, fullMonthCounts.values, alpha=0.3)

    plt.title('Number of Incidents by Month for Each Year')
    plt.xlabel('Month')
    plt.ylabel('Number of Incidents')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotMonthByYear2():
    plt.figure(figsize=(10, 6))
    for year in allYears.sort_values().unique():
        monthCounts = data[data['timeline.incident.year'] == year]['timeline.incident.month'].value_counts().sort_index()
        fullMonthCounts = monthCounts.reindex(range(1, 13), fill_value=0) # if no values the add it with 0
        plt.plot(fullMonthCounts.index, fullMonthCounts.values,label=int(year),linestyle='none', color="red")
        plt.fill_between(fullMonthCounts.index, fullMonthCounts.values, alpha=0.3,color="red")

    plt.title('Number of Incidents by Month for Each Year')
    plt.xlabel('Month')
    plt.ylabel('Number of Incidents')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotMonthByYearContinuous():
    data_dict = {}
    for year in allYears.sort_values().unique():
        monthCounts = data[data['timeline.incident.year'] == year]['timeline.incident.month'].value_counts().sort_index()
        fullMonthCounts = monthCounts.reindex(range(1, 13), fill_value=0)
        data_dict.update({f"{int(year)}-{month:02d}": arr for month, arr in zip(fullMonthCounts.index, fullMonthCounts.values)})

    YearMonth = list(data_dict.keys())
    counts = list(data_dict.values())

    plt.figure(figsize=(40, 6))
    plt.plot(range(len(counts)), counts, color='blue')
    plt.fill_between(range(len(counts)), counts, color='blue', alpha=0.3)
    plt.xticks(ticks=range(0, len(YearMonth)), labels=YearMonth, rotation=90)
    plt.title('Number of Incidents by Month Across All Years')
    plt.xlabel('Time')
    plt.ylabel('Number of Incidents')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plotMonthByYearContinuous2():
    data_dict = {}
    for year in allYears.sort_values().unique():
        monthCounts = data[data['timeline.incident.year'] == year]['timeline.incident.month'].value_counts().sort_index()
        fullMonthCounts = monthCounts.reindex(range(1, 13), fill_value=0)
        data_dict.update({f"{int(year)}-{month:02d}": arr for month, arr in zip(fullMonthCounts.index, fullMonthCounts.values)})

    YearMonth = list(data_dict.keys())
    counts = list(data_dict.values())

    # Continuously count the amount of incidents
    cumulativeCounts = []
    running_total = 0
    for count in counts:
        running_total += count
        cumulativeCounts.append(running_total)

    plt.figure(figsize=(40, 6))
    plt.plot(range(len(cumulativeCounts)), cumulativeCounts, color='blue')
    plt.fill_between(range(len(cumulativeCounts)), cumulativeCounts, color='blue', alpha=0.3)
    plt.xticks(ticks=range(len(YearMonth)), labels=YearMonth, rotation=90)
    plt.title('Cumulative Number of Incidents by Month Across All Years')
    plt.xlabel('Time')
    plt.ylabel('Cumulative Number of Incidents')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotAverageIncidentsPerDayEachMonth():
    frame, sub = plt.subplots(3, 4, figsize=(30, 12), sharey=True)
    frame.suptitle('Average Number of Incidents per Day for Each Month', fontsize=16)
    sub = sub.flatten()

    for month in range(1, 13):
        monthData = data[(data['timeline.incident.month'] == month) & (data['timeline.incident.year'] >= 2005)]
        dayCounts = monthData['timeline.incident.day'].value_counts().sort_index()
        month = month-1
        dayCounts = dayCounts.reindex(range(1, 32), fill_value=0)
        # Get the correct subplot
        ax = sub[month]

        ax.plot(dayCounts.index, dayCounts.values, marker='o', color='red')
        ax.fill_between(dayCounts.index, dayCounts.values, color='red', alpha=0.5)
        ax.set_title(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month])
        ax.set_xlabel('Day')
        ax.set_ylabel('Average Incidents')
        ax.set_xticks(range(1, 32))
        ax.grid(True)

    plt.tight_layout()
    plt.show()


def plotAverageIncidentsPerDay():
    plt.figure(figsize=(15, 8))
    plt.title('Average Number of Incidents per Day for Each Month', fontsize=16)

    for month in range(1, 13):
        monthData = data[(data['timeline.incident.month'] == month) & (data['timeline.incident.year'] >= 2005)]
        dayCounts = monthData['timeline.incident.day'].value_counts().sort_index()

        dayCounts = dayCounts.reindex(range(1, 32), fill_value=0)
        plt.plot(dayCounts.index, dayCounts.values, marker='o', label=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month-1])
        plt.fill_between(dayCounts.index, dayCounts.values, alpha=0.3)

    plt.xlabel('Day of the Month')
    plt.ylabel('Average Incidents')
    plt.xticks(range(1, 32))
    plt.grid(True)
    plt.legend(title="Month")
    plt.tight_layout()
    plt.show()

def plotAverageIncidentsPerDay2():
    plt.figure(figsize=(15, 8))
    plt.title('Average Number of Incidents per Day for Each Month', fontsize=16)

    for month in range(1, 13):
        monthData = data[(data['timeline.incident.month'] == month) & (data['timeline.incident.year'] >= 2005)]
        dayCounts = monthData['timeline.incident.day'].value_counts().sort_index()

        dayCounts = dayCounts.reindex(range(1, 32), fill_value=0)
        plt.plot(dayCounts.index, dayCounts.values, linestyle='none', color='red', label=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month-1])
        plt.fill_between(dayCounts.index, dayCounts.values, alpha=0.3, color='red')

    plt.xlabel('Day of the Month')
    plt.ylabel('Average Incidents')
    plt.xticks(range(1, 32))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotMonthlyIncidentsEachYear():
    uniqueYears = allYears.sort_values(ascending=True).unique()

    rows = (len(uniqueYears) + 3) // 4
    frame, sub = plt.subplots(rows, 4, figsize=(20, rows * 4), sharey=True)
    frame.suptitle('Monthly Incident Counts for Each Year', fontsize=16)
    sub = sub.flatten() # flattens 2d array into 1d

    for i, year in enumerate(uniqueYears):
        monthCount = data[data['timeline.incident.year'] == year]['timeline.incident.month'].value_counts()
        monthCount = monthCount.reindex(range(1, 13), fill_value=0)

        ax = sub[i]
        ax.plot(monthCount.index, monthCount.values, marker='o', color='blue')
        ax.fill_between(monthCount.index, monthCount.values, color='skyblue', alpha=0.4)
        ax.set_title(int(year))
        ax.set_xlabel('Month')
        ax.set_ylabel('Incident Count')
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
        ax.grid(True)

    plt.tight_layout(rect=(0, 0, 1, 0.99))
    plt.show()

holiday_dates =  [
    # January
    (1, 1),   # New Year's Day
    (1, 6),   # Epiphany

    # February
    (2, 14),  # Valentine's Day
    (2, 21),  # Presidents' Day (3rd Monday in February, so varies, approximate)

    # March
    (3, 17),  # St. Patrick's Day
    (3, 8),   # International Women's Day (celebrated worldwide)

    # April
    (4, 1),   # April Fool's Day
    (4, 15),  # Good Friday (varies by year, placeholder)
    (4, 17),  # Easter Sunday (varies by year, placeholder)

    # May
    (5, 1),   # May Day / International Workers' Day
    (5, 8),   # Victory in Europe Day (observed in Europe)
    (5, 25),  # Memorial Day (last Monday in May, approximate)

    # June
    (6, 19),  # Juneteenth (US)
    (6, 24),  # Midsummer’s Day (observed in Scandinavian countries)

    # July
    (7, 1),   # Canada Day
    (7, 4),   # Independence Day (US)
    (7, 14),  # Bastille Day (France)

    # August
    (8, 1),   # Swiss National Day (Switzerland)
    (8, 15),  # Assumption of Mary (celebrated in some European countries)

    # September
    (9, 5),   # Labor Day (1st Monday in September, approximate)
    (9, 21),  # International Day of Peace (observed worldwide)

    # October
    (10, 10), # Indigenous Peoples' Day / Columbus Day (2nd Monday in October, approximate)
    (10, 31), # Halloween

    # November
    (11, 1),  # All Saints' Day
    (11, 11), # Veterans Day (US) / Remembrance Day (UK, Canada)
    (11, 24), # Thanksgiving (4th Thursday in November, approximate)

    # December
    (12, 24), # Christmas Eve
    (12, 25), # Christmas Day
    (12, 26), # Boxing Day (UK, Canada)
    (12, 31), # New Year's Eve
]

def plotIncidentsByYearWithHolidays():
    filtered_data = data[data['timeline.incident.year'] >= 2005]
    yearly_counts = filtered_data.groupby([data['timeline.incident.year'], 'isHoliday']).size().unstack(fill_value=0)

    yearly_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Incidents by Year (Holiday vs. Non-Holiday)")
    plt.xlabel("Year")
    plt.ylabel("Number of Incidents")
    plt.legend(["Non-Holiday", "Holiday"], loc="upper right")
    plt.show()

def plotAttackTypePercentage():
    attackTypes = ['action.Hacking', 'action.Malware', 'action.Social', 'action.Physical', 'action.Error', 'action.Misuse', 'action.Unknown']

    holidayAttacks = data[data['isHoliday']][attackTypes].sum()
    nonHolidayAttacks = data[data['isHoliday'] == False][attackTypes].sum()

    # Should legal the pie charts for action.hacking and so on to hacking
    frame, (pi1, pi2) = plt.subplots(1, 2, figsize=(14, 7))
    pi1.pie(holidayAttacks, labels=holidayAttacks.index, autopct='%1.1f%%')
    pi1.set_title('Attack Types on Holidays')
    pi2.pie(nonHolidayAttacks, labels=nonHolidayAttacks.index, autopct='%1.1f%%')
    pi2.set_title('Attack Types on Non-Holidays')

    plt.tight_layout()
    plt.show()

def HealthcareAverageIncidenceByDayandMonth():
    industryType = [('Healthcare','red'), ('Public', 'lightblue'), ('Educational','green'), ('Finance', 'darkyellow'), ('Information','darkblue'), ('Retail','grey'), ('Professional','purple'), ('Unknown', 'grey'), ('Manufacturing','orange'), ('Other Services', 'grey')]
    for industry, indColor in industryType:
        frame, sub = plt.subplots(3, 4, figsize=(30, 12), sharey=True)
        frame.suptitle('Average Number of Incidents against ' + industry, fontsize=16)
        sub = sub.flatten()

        for month in range(1, 13):
            healthcare_data = data[data['victim.industry.name'] == industry]
            month_data = healthcare_data[
                (healthcare_data['timeline.incident.month'] == month) &
                (healthcare_data['timeline.incident.year'] >= 2005)
            ]

            day_counts = month_data['timeline.incident.day'].value_counts().sort_index()
            day_counts = day_counts.reindex(range(1, 32), fill_value=0)
            ax = sub[month - 1]

            ax.plot(day_counts.index, day_counts.values, marker='o', color=indColor)
            ax.fill_between(day_counts.index, day_counts.values, color=indColor, alpha=0.5)
            ax.set_title(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month - 1])
            ax.set_xlabel('Day')
            ax.set_ylabel('Average Incidents')
            ax.set_xticks(range(1, 32))
            ax.grid(True)

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    allYears = data['timeline.incident.year'].where(data['timeline.incident.year'] >= 2005).dropna()

    #Creates a col that says if date is a holiday
    isHoliday= data.apply(lambda x: (x['timeline.incident.month'], x['timeline.incident.day']) in holiday_dates, axis=1)
    data = pd.concat([data, isHoliday.rename('isHoliday')], axis=1)

    plotYearAmount()
    plotAverageIncidentsPerMonth()
    plotMonthByYear()
    plotAverageIncidentsPerDaySingle()
    plotMonthByYear2()
    plotMonthByYearContinuous()
    plotMonthByYearContinuous2()
    plotAverageIncidentsPerDayEachMonth()
    plotAverageIncidentsPerDay()
    plotAverageIncidentsPerDay2()
    plotMonthlyIncidentsEachYear()

    plotIncidentsByYearWithHolidays()
    plotAttackTypePercentage()

    HealthcareAverageIncidenceByDayandMonth()
