from typing import List
import csv
from datetime import timedelta


# TODO: automate the current workflow 
# (move file from shortcuts to desktop, create loan file, cut from log-focus to loan-file, append monthly hours to loan file, delete focus-log, move loan file )

# CONSTANTS NEEDED
# file-name, directory, target-name
DIR = '/users/deniz/desktop/'
FILE_NAME = 'focus-time-log.csv'
LOAN_FILE_NAME = 'arbeitszeit_juni_deniz_grollmusz.csv'

# VARIABLES NEEDED
work_hours_list: List = []
hours_list = []
minutes_list = []
work_hours_tot = timedelta(hours=0, minutes=0)
loan_file = None
start_time = None
end_time = None


# LOAD CSV FILE
with open(DIR+FILE_NAME, "r") as f:
    loan_file = csv.reader(f, delimiter=",")

    # LOOP THROUGH ALL LINES
    for line in loan_file:

        if line[2].upper().strip() == 'START':
            hours, minutes = line[1].split(':')
            start_time = timedelta(hours=int(hours), minutes=int(minutes))

        elif line[2].upper().strip() == 'ENDE':
            hours, minutes = line[1].split(':')
            end_time = timedelta(hours=int(hours), minutes=int(minutes))

            work_hours_list.append(end_time - start_time)

            start_time, end_time = None, None


# CALCULATE MONTHLY HOUR BY ADDING ALL TIMEDELTAS FROM THE LIST
for timedelta_ in work_hours_list:
    work_hours_tot += timedelta_


print(
    divmod(
        divmod(work_hours_tot.total_seconds(), 60)[0],
        60
    )
)