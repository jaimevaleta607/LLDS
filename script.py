import subprocess
import json
import csv

# Paths to email and token files
email_file_path = '/{File_path}/emails.txt'
token_file_path = '/{File_path}/token.txt'
output_file_path = '/{File_path}/results.csv'
# example '/Users/jaimevaleta/Downloads/token.txt'

# Read token and environment variables from file
with open(token_file_path, 'r') as file:
    lines = file.readlines()
    token = lines[0].strip()  # SUBMARINE_DOCKER_AUTH_TOKEN
    environment = lines[1].strip()  #SUBMARINE_DOCKER_ENVIRONMENT

# Read emails from file
with open(email_file_path, 'r') as file:
    emails = file.read().splitlines()

# Prepare CSV file to save results
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Email', 'Date Joined', 'Last Login'])

    # Run the command for each email and extract the desired information
    for email in emails:
        result = subprocess.run(['submarine', 'account', 'lookup', email, '--token', token, '--env', environment], capture_output=True, text=True)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            account_info = data.get('account', {})
            full_name = account_info.get('full_name', 'N/A')
            date_joined = account_info.get('date_joined', 'N/A')
            last_login = account_info.get('last_login', 'N/A')
            email_info = data.get('emails', [{}])[0]
            email_address = email_info.get('email', 'N/A')

            # Write row to CSV file
            writer.writerow([full_name, email_address, date_joined, last_login])
        else:
            print(f"Error executing command for {email}: {result.stderr}")

# CSV file is ready at the specified path
print(f"Results saved in: {output_file_path}")
