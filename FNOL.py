import datetime

# Program to create editable fields

# Create a dictionary to store the fields
fields = {}

# Get the current time and date
now = datetime.datetime.now()

# Store the current time and date as the timestamp
fields['Timestamp'] = now.strftime("%Y-%m-%d %H:%M:%S")

# Prompt the user to enter a value for each field
fields['Call Received By'] = input("Enter Call Received By: ")
fields['Date of Call'] = now.strftime("%Y-%m-%d")
fields['Time of Call'] = now.strftime("%H:%M:%S")
fields['Customer First Name'] = input("Enter Customer First Name: ")
fields['Customer Last Name'] = input("Enter Customer Last Name: ")
fields['Customer Phone Number'] = input("Enter Customer Phone Number: ")
fields['Customer Email Address'] = input("Enter Customer Email Address: ")
fields['Loss Address'] = input("Enter Loss Address (Number and Street Name): ")
fields['City'] = input("Enter City: ")
fields['State'] = input("Enter State: ")
fields['Zip Code'] = input("Enter Zip Code: ")
fields['Services Scheduled For'] = input("Enter Services Scheduled For: ")
fields['Type of Loss'] = input("Enter Type of Loss: ")
fields['Date of Loss'] = input("Enter Date of Loss: ")
fields['Structure Type'] = input("Enter Structure Type: ")
fields['Room(s) Affected'] = input("Enter Room(s) Affected: ")
fields['Is there Standing Water?'] = input("Is there Standing Water? (Yes/No): ")
fields['Were Contents Affected?'] = input("Were Contents Affected? (Yes/No): ")
fields['Is electric available'] = input("Is electric available? (Yes/No): ")
fields['Type(s) of Flooring Affected'] = input("Enter Type(s) of Flooring Affected: ")
fields['Cause of Loss'] = input("Enter Cause of Loss: ")
fields['Insurance Company'] = input("Enter Insurance Company: ")
fields['Insurance Agent Name (If Known)'] = input("Enter Insurance Agent Name (If Known): ")
fields['Claim Number (If Applicable)'] = input("Enter Claim Number (If Applicable): ")
fields['Deductible Amount (If Known)'] = input("Enter Deductible Amount (If Known): ")
fields['Referred To:'] = input("Enter Referred To: ")
fields['Notes'] = input("Enter Notes: ")




# Display the fields
print("\nFields:")
for key, value in fields.items():
  print(key + ": " + value)
  import csv

