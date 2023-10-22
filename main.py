import json
import csv

# Initialize an empty list to store order data
order_list = []

# Define the CSV file name
csv_filename = 'orders.csv'

# Open the JSON file for reading
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)
    results = json_data.get('results', [])

    for order_data in results:
        # Extract relevant information and create a dictionary for the order
        order_info = {
            'Order ID': order_data.get('id', ''),
            'Total Amount': order_data.get('total_amount', ''),
            'Contact ID': order_data.get('contact_id', ''),
            'Status': order_data.get('status', ''),
            # Add more fields as needed

            # Extract Billing Contact Details from billing_contact > billing_address
            'Name': order_data['company']['contact']['details'].get('first_name', '') + ' ' + order_data['company']['contact']['details'].get('last_name', ''),
            'Phone': order_data['company']['contact']['details'].get('phone', ''),
            'Email': order_data['company']['contact']['details'].get('email', ''),
            # Add more fields as needed
        }

        # Append the order information to the list
        order_list.append(order_info)

# Writing the data to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Order ID', 'Amount', 'Contact', 'Status',
                  'Billing Contact Name', 'Phone', ' Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data rows
    for order_info in order_list:
        writer.writerow(order_info)

print(f'CSV file "{csv_filename}" has been created with the order details including billing contact information.')
