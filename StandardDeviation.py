import csv
import math

with open("data_1.csv",newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    records = len(data)
    sum = 0
    for x in data:
        sum += int(x)
    mean = sum/records
    return mean

squared_list = []
for num in data:
    answer = int(num)-mean(data)
    answer = answer**2
    squared_list.append(answer)

result = 0
for i in squared_list:
    result += i

std_deviation = math.sqrt(result/(len(data)-1))
print(std_deviation)    