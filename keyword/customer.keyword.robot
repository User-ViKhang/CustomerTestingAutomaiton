*** Keywords ***
Create Customer
    [Arguments]    ${customer_file}
    @{data}=    AddCustomer    ${customer_file}

Read File CSV    
    [Arguments]    ${csv_file}
    @{data}=    ReadCSVFile    ${csv_file}