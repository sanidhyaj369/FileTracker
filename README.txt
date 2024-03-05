This Python script is created to keep track of any changes that occur in a directory called "to_be_monitored." Whenever a new file is added to the directory, the script records the filename with the current timestamp in a file named "logs_file.txt". The following are the steps involved in the script:

1. Importing Modules:
The script uses three modules:
- os: This module provides a way to interact with the operating system portably, and it is used for directory operations.
- time: This module provides various time-related functions and is used for pausing the program.
- datetime: This module supplies classes for managing dates and times. It is used for getting the current timestamp.

2. Global Variables:
The following global variables are used:
- to_be_monitored_path: This variable stores the path of the directory to be monitored. It is obtained by joining the current working directory (os.getcwd()) with the subdirectory "to_be_monitored."
- global_keep_safe: This list tracks files that have been processed to prevent duplicate logging.

3. Check_Files Function:
The "check_files" function takes two arguments:
- file_name: The name of the file to be checked.
- output_file_name: The name of the log file.
The function verifies that the file_name is not already in the "global_keep_safe" list to avoid duplicating logs. If it is not already processed, the function opens the log file in append mode, retrieves the current timestamp, writes the filename and the timestamp to the log file, and then closes the file. Finally, the function adds the file_name to the "global_keep_safe" list.

4. Start_Checking Function:
The "start_checking" function takes "to_be_monitored_path" as an argument. The function iterates over each file in the directory specified by "to_be_monitored_path" and calls the "check_files" function for each file, passing the file name and the name of the log file as arguments.

5. Main Loop:
The script has an infinite loop that continuously monitors the directory. In each iteration, it calls the "start_checking" function with the "to_be_monitored_path" directory. After processing all files in the directory, the script pauses for one second before starting the next iteration. This pause is to avoid excessive CPU usage.