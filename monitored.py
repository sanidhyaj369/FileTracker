# Importing neccessary modules
import os , time
from datetime import datetime

to_be_monitored_path = os.path.join(os.getcwd(),'to_be_monitored')  # joining the current working directory with the subdirectory

global_keep_safe = []


def check_files(file_name, output_file_name):
    if file_name not in global_keep_safe:
        file1 = open(output_file_name, "a")
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        file1.write(f"{file_name} - {formatted_time} \n")
        file1.close()
        global_keep_safe.append(file_name)

def start_checking(to_be_monitored_path):
    for file in os.listdir(to_be_monitored_path):
        check_files(file,'logs_file.txt')

while True:     # infinite loop for continuously monitoring the directory.
    start_checking(to_be_monitored_path=to_be_monitored_path)
    time.sleep(1)



    