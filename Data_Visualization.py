
# importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def LinePlot(xaxis):
    """
    Drawing a line plot to show the change in total number of
    cancer deaths in the selected countries for the selected years

    Args: 
        xaxis: the range or list of years

    """
    for c in country:
        """ The total number of cancer deaths in a certain year in a 
        selected set of nations, for example, is displayed against 2000 and 
        similarly in each rotation """
        year_total = list(cancer_df[cancer_df['Country'] == c]['Total'])

        # plot the line
        plt.figure(1, figsize=(12, 6))
        plt.plot(xaxis, year_total, label=c, marker='o')

        # set x-axis and y-axis limits
        plt.xlim([2000, 2019])
        plt.ylim([18000, 36000])

        # set the ticks on both axes
        plt.xticks(year)
        plt.yticks(np.arange(20000, 36000, 2000))

        # set the title and axes labels
        plt.title('Cancer attributed Deaths of 5 Countries (2000-2019)'+'\n',
                  fontsize=15, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Total Cancer Deaths', fontsize=12)

    plt.legend(loc='best', bbox_to_anchor=(1, 0.4))  # set the legends
    plt.savefig('CancerVsCountry.png')  # save the figure
    plt.show()  # show the plot


def StackedBarPlot(xaxis, yaxis1, yaxis2):
    """ Construct a stacked bar plot represent

    Args:
        xaxis (Series): the set of countries to be compared
        yaxis1 (Series): number of deaths by breast cancer
        yaxis2 (Series): number of deaths by Tracheal, bronchus,
                    and lung cancer
    """
    plt.figure(2, figsize=(10, 6))
    plt.bar(xaxis, yaxis1, label='Breast Cancer')
    plt.bar(xaxis, yaxis2,
            bottom=yaxis1, label='Tracheal, bronchus and lung Cancer')
    plt.title('Comparison of Breast and Tracheal, bronchus, and lung Cancer'+'\n'
              + 'Caused Deaths of 5 Countries in 2019', fontweight='bold')
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Proportion of Cancer Deaths', fontsize=12)

    # Determine the percentages of each cancer type in each country
    total_cases = yaxis1 + yaxis2
    prop_breast_cancer = list(np.round(yaxis1 / total_cases * 100, 1))
    prop_tracheal_etc = list(np.round(yaxis2 / total_cases * 100, 1))

    # Determine the y values of the text labels
    y_values_breast = yaxis1 / 2
    y_values_tracheal = yaxis1 + yaxis2 / 2
    # Add the text labels to the plot
    for i in range(len(xaxis)):
        plt.text(x=i - 0.3, y=y_values_breast.to_list()[i],
                 s=f'{prop_breast_cancer[i]}%',
                 fontsize=12, fontweight="bold")
        plt.text(x=i - 0.3, y=y_values_tracheal.to_list()[i],
                 s=f'{prop_tracheal_etc[i]}%',
                 fontsize=12, fontweight="bold")
    plt.legend(loc=(0.2, 0.8))
    plt.savefig('Breast_cancer_Vs_Lung_cancer.png')
    plt.show()


def PieChart(grp_values, grp_types):
    """ Contruct a pie chart showing the worldwide distribution of cancer caused
        deaths and its types

    Args:
        grp_values (list): list of global death count in each type of cancer, 
                where the ones lower that the given threshold is added to a single value
        grp_types (list): list of cancer types, 
                where the ones below the threshold value is grouped as 'Others'
    """
    plt.figure(3, figsize=(12, 6))
    plt.pie(grp_values, labels=grp_types, autopct='%1.1f%%', pctdistance=0.8)
    plt.title(
        'Global Distribution of Cancer-Caused Deaths and Cancer Types 2019' +
        '\n', fontweight='bold')
    plt.axis('equal')
    plt.legend(loc=(0.8, 0.01))
    plt.savefig('Global_Distribution_of_Cancer-Caused_Deaths')
    plt.show()


# Reading the csv file
cancer = pd.read_csv(r"Dataset\total-cancer-deaths-by-type.csv")

# Renamed the column names for easy access
cancer.columns = ['Country', 'Code', 'Year', 'Liver', 'Kidney',
                  'Lip and Oral', 'Tracheal, bronchus, and lung',
                  'Larynx', 'Gallbladder and biliary tract',
                  'Malignant skin melanoma', 'Leukemia',
                  'Hodgkin lymphoma', 'Multiple myeloma',
                  'Other neoplasms', 'Breast', 'Prostate',
                  'Thyroid', 'Stomach', 'Bladder', 'Uterine',
                  'Ovarian', 'Cervical', 'Brain and central nervous system',
                  'Non-Hodgkin lymphoma', 'Pancreatic cancer',
                  'Esophageal cancer', 'Testicular', 'Nasopharynx',
                  'Other pharynx', 'Colon and rectum',
                  'Non-melanoma skin', 'Mesothelioma']

# Creating a new Dataframe with cancer record from 2000 to 2019
cancer2000_19 = cancer[(cancer['Year'] >= 2000) & (cancer['Year'] <= 2019)]

# Selecting 5 Countries randomly and forming a list
country = ['Sweden', 'Chile', 'Hungary', 'Belgium', 'Greece']

# Filtering the dataframe into these 5 countries records
cancer_df = cancer2000_19[cancer2000_19['Country'].isin(country)]

# Reseting the index for the filtered dataframe cancer_df
cancer_df = cancer_df.reset_index()

'''Creating a new column 'Total' which adds up the values
    of all cancer types of these 5 countries.
This is done for drawing the line plot of the total cancer deaths of
    these 5 countries in the given years '''
selected_columns = cancer_df.columns[cancer_df.columns.get_loc('Liver'):]
cancer_df['Total'] = cancer_df[selected_columns].sum(axis=1)

# list of selected years ie., 2000 to 2019
year = np.arange(2000, 2020)

# Filtering the dataframe cancer_df for the year 2019 for bar plot
cancer19 = cancer_df[cancer_df['Year'] == 2019]

''' Filter the above dataframe to create a dataframe of breast cancer and
     tracheal,bronchus and lung cancer'''
cancer_bl = cancer19[['Country', 'Breast', 'Tracheal, bronchus, and lung']]

# adding columns showing proportion of breast cancer and lung cancer of each country
cancer_bl['b_prop'] = cancer_bl['Breast'] / \
    (cancer_bl['Breast']+cancer_bl['Tracheal, bronchus, and lung'])
cancer_bl['l_prop'] = cancer_bl['Tracheal, bronchus, and lung']/(
    cancer_bl['Breast']+cancer_bl['Tracheal, bronchus, and lung'])

'''Creating a new Dataframe with data of selected countries and all
    cancer type deaths of a single year(2019) for the pie chart '''
cancer_19 = cancer[cancer['Year'] == 2019]

# List of cancer types
cancer_types = cancer_19.columns[3:]

''' Creating a new row 'Grand Total' which gives the type wise total
    deaths in the year 2019 '''
cancer_19.loc['Grand Total'] = cancer_19[cancer_types].sum(axis=0)

# list of total deaths caused by each cancer type
values = list(cancer_19.loc['Grand Total'][3:])

''' setting a threshold for creating a pie 'others' so that the cancer
    types causing deaths less than 1400000 comes under this pie '''
threshold = 1400000

grp_values = []  # creating an empty list for grouped values
grp_types = []   # creating an empty list for grouped types

low_values = 0  # setting a variable low_value as 0

''' starting a for loop to loop through the list of cancer types
    and its values to compare it with the threshold set '''
for i in range(len(cancer_types)):
    ''' to check the condition of death count and threshold
        if less then added with low_values '''
    if values[i] < threshold:
        low_values += values[i]
    else:
        # else added to the list of grouped values and types
        grp_values.append(values[i])
        grp_types.append(cancer_types[i])

# newly created set of low values appended to the list as 'Others'
grp_values.append(low_values)
grp_types.append('Others')

# calling line plot function
LinePlot(year)

# calling stacked bar plot function
StackedBarPlot(cancer19['Country'], cancer_bl['b_prop'],
               cancer_bl['l_prop'])

# calling pie plot function
PieChart(grp_values, grp_types)
