import collections
from statistics import mean

average_of = collections.defaultdict(float)
num_companies = int(input("Number of companies: "))
for _ in range(num_companies):
    company = input("Company name: ")
    profits = (
        float(input("  Q1 = ")),
        float(input("  Q2 = ")),
        float(input("  Q3 = ")),
        float(input("  Q4 = "))
    )
    average_of[company] = mean(profits)

#print(average_of)

total_average = mean(average_of.values())

#print(total_average)

print("More than average:")
for company, average in average_of.items():
    if average > total_average:
        print(company)

print("Less than average:")
for company, average in average_of.items():
    if average < total_average:
        print(company)
