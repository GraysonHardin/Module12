"""
Program: csv_imports.py
Author: Grayson Hardin
Last date modified: 11/15/2020

Inherits data from the Iowa Census and can either print all of its content or filter selected data to the console.
"""
import csv
import locale
from csv_assignment.county_demos import CountyDemos


def display_population_and_household_for_county(county_name, county):
    return f'Population: {county[county_name].population}, Number of households: {county[county_name].number_of_households}'


def total_population_calculator(county):
    locale.setlocale(locale.LC_ALL, 'en_US')
    pop_sum = 0
    for key in county:
        pop_sum += int(county[key].population.replace(',', ''))
    return f'The total Iowa population is: {locale.format_string("%d", pop_sum, grouping=True)}'


with open('iowa_2010_census_population_income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    county = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = CountyDemos(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    del county['Iowa State']
    del county['United States']

    print(display_population_and_household_for_county('Dallas', county))
    print(total_population_calculator(county))
