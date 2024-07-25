*** Settings ***
Variables       ../data/variables.yaml
Library         ../libraries/CustomerLib.py    ${customer_json_file}
Resource        ../keyword/customer.keyword.robot
*** Test Cases ***
Create Customer From CSV 
    [Documentation]    Create customers from CSV file and save to JSON file
    Create Customer    ../data/test_data.csv

Read CSV file        
    [Documentation]    Read file CSV
    Read File CSV    ../data/test_data.csv