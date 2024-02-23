# LLDS
Last login Day Script


This script is designed to scrape email addresses from a specified list of users. To execute the script, follow these steps:

Prerequisites:

Ensure you have Python installed on your computer. You can download it here. https://www.python.org/downloads/

Necessary Files:

token.txt
emails.txt
script.py

Execution Steps:

1. Open **script.py** in your preferred code editor.

2. Modifi **token.txt** and **emails.txt**

3. In emails.txt, list the email addresses you want to consult. You can obtain this information by exporting user data from the Docker admin panel. Refer to the documentation here.

4. In token.txt, include **SUBMARINE_DOCKER_AUTH_TOKEN** and **SUBMARINE_DOCKER_ENVIRONMENT**. You can obtain these by executing submarine auth login. Use the file as a reference.

5. Navigate to the directory containing the script using the terminal.

6. Once ready, execute the following command to run the script: **cd '' && '/usr/local/bin/python3' 'script.py'**.

6. Upon successful execution, look for a file called **results.csv** in the path specified on line 8 of your script.
