*** Settings ***
Variables       ../data/variables.yaml
Library         ../libraries/CustomerLib.py    ${customer_json_file}
Library         OperatingSystem
Library         Collections
Library         String

*** Test Cases ***
Create Customer From CSV 
    [Documentation]    Create customers from CSV file and save to JSON file
    [Tags]    Create
    AddCustomer    ../data/test_data.csv

Read CSV file    
    [Documentation]    Read file CSV
    @{data}=    ReadCSVFile    ../data/test_data.csv
    Log    ${data}    
*** Keywords ***
Customer Should Be Saved
    [Arguments]    ${customer}
    ${exist_customer}=    GetCustomer    ${customer['email']}
    Should Not Be Empty    ${exist_customer}
    Should Be Equal   ${customer}    ${exist_customer}
        
