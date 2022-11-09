import re

filehandle = open("regex_sum_1654171.txt", "rt")
cummulative_sum = 0
count = 0

for line in filehandle:
    line = line.rstrip()

    values_list = re.findall('[0-9]+', line)
    if len(values_list) > 0:

        for num in values_list:
            num = int(num)
            count = count + 1
            cummulative_sum = cummulative_sum + num

print(cummulative_sum, count)
