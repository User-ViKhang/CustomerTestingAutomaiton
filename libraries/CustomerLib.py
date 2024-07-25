import json
import csv

class CustomerLib:
    
    def __init__(self, json_file):
        self.json_file = json_file
        
    def AddCustomer(self, customer):  # add a customer
        dict_customer = self.ReadCSVFile(customer)
        self.WriteToJson(dict_customer, self.json_file)
        with open(customer, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            return data
        
    def GetCustomer(self, email):  # get customer by email
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                for record in data:
                    if record['email'] == email:
                        return record
        except FileNotFoundError:   
            return None
        return None
    def ReadCSVFile(self, csv_file):
        try:
          with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            return data
        except:
          return None    
    def WriteToJson(self, dict_data, json_file_path):
        try:
        # Read the existing JSON data from the file
            with open(json_file_path, 'r') as jsonfile:
                existing_data = json.load(jsonfile)
            
            # Append the new data to the existing data
            existing_data.extend(dict_data)
            
            # Write the updated data back to the file
            with open(json_file_path, 'w') as jsonfile:
                json.dump(existing_data, jsonfile, indent=4)
    
        except FileNotFoundError:
            # If the file doesn't exist, create a new one and write the data
            with open(json_file_path, 'w') as jsonfile:
                json.dump(dict_data, jsonfile, indent=4)
            
