#!/usr/bin/env python3

import csv
import re
import operator

count_error = {}
count_user = {}

with open('syslog.log', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            error = re.search(r"ERROR ([\w ]*) ", line).group(1)
            count_error[error] = count_error.get(error, 0) + 1
            user = re.search(r"\(([\w.]*)\)", line).group(1)
            count_user[user] = count_user.get(user, [0, 0])
            count_user[user][1] += 1
        elif 'INFO' in line:
            user = re.search(r"\(([\w.]*)\)", line).group(1)
            count_user[user] = count_user.get(user, [0, 0])
            count_user[user][0] += 1
        
# sort by value
sorted_error = sorted(count_error.items(), key=operator.itemgetter(1), reverse=True)
# sort by key / username
sorted_user = sorted(count_user.items(), key=operator.itemgetter(0))

# insert column names
sorted_error.insert(0, ("Error", "Count"))
sorted_user.insert(0, ("Username", "INFO", "ERROR"))

# write to csv file
with open("error_message.csv", "w") as error_file:
    for item in sorted_error:
        error_file.write("{},{}\n".format(item[0], item[1]))

with open("user_statistics.csv", "w") as user_file:
    for item in sorted_user:
        # the first item is column name "Username", so we need to handle it differently
        if item[0] == "Username":
            user_file.write("{},{},{}\n".format(item[0], item[1], item[2]))
        else:
            user_file.write("{},{},{}\n".format(item[0], item[1][0], item[1][1]))

