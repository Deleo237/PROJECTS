import openpyxl

def save_variables(variables, col):
    # Write the xlsx file using the openpyxl library
    output = openpyxl.load_workbook('Output Data Structure.xlsx')

    # Specify the sheet you want to work in
    sheet_output = output['Sheet1']

    # Iterate over rows to input the various variables the urls
    for column in range(3, 16):
        # Write data to a specific cell
        sheet_output.cell(row=col, column=column, value=str(variables[column-3]))
    
    # Save the workbook
    output.save("Output Data Structure.xlsx")
    
    print('Saved Successfully')