# # 3. Working with CSV
# # Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at
# # Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# # Annual average for each year in the dataset.
import csv

year_list = []
value_list = []

with open('co2-ppm-daily.txt') as co2_ppm_csv:
    csv_reader = csv.reader(co2_ppm_csv, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        # create the list of values for the overall time series
        value_list.append(float(row[1]))
        year, month, day = row[0].split('-')
        if year not in year_list:
            year_list.append(year)
            print(year)

for year_select in year_list:
    yearly_list = []
    with open('co2-ppm-daily.txt') as co2_ppm_csv:
        csv_reader = csv.reader(co2_ppm_csv, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            year, month, day = row[0].split('-')
            if year == year_select:
                yearly_list.append(float(row[1]))
    print(yearly_list)
    print(sum(yearly_list))
    print(len(yearly_list))
    print(str(year_select) + ":" + str(sum(yearly_list)/len(yearly_list)))

# Minimum, maximum and average for the entire dataset.
print(min(value_list))
print(max(value_list))
# average of the entire dataset
print(str(sum(value_list)/len(value_list)))


# Seasonal average if Spring (March, April, May), Summer (June, July, August),
# Autumn (September, October, November) and Winter (December, January, February).
spring = ['03', '04', '05']
spring_value_list = []
summer = ['06', '07', '08']
summer_value_list = []
fall = ['09', '10', '11']
fall_value_list = []
winter = ['12', '01', '02']
winter_value_list = []
with open('co2-ppm-daily.txt') as co2_ppm_csv:
    csv_reader = csv.reader(co2_ppm_csv, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        year, month, day = row[0].split('-')
        # print(month)
        if month in spring:
            spring_value_list.append(float(row[1]))

        if month in summer:
            summer_value_list.append(float(row[1]))

        if month in fall:
            fall_value_list.append(float(row[1]))

        if month in winter:
            winter_value_list.append(float(row[1]))

print(spring_value_list)
print(summer_value_list)
print(fall_value_list)
print(winter_value_list)
print("spring:" + str(sum(spring_value_list)/len(spring_value_list)))
print("summer:" + str(sum(summer_value_list)/len(summer_value_list)))
print("fall:" + str(sum(fall_value_list)/len(fall_value_list)))
print("winter:" + str(sum(winter_value_list)/len(winter_value_list)))


# # Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
anomaly_list = []
with open('co2-ppm-daily.txt') as co2_ppm_csv:
    csv_reader = csv.reader(co2_ppm_csv, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        anomaly_list.append(float(row[1]) - sum(value_list)/len(value_list))

        print("Anomaly:" + str(float(row[1]) - sum(value_list)/len(value_list)))












