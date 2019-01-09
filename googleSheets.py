import gspread
from oauth2client.service_account import ServiceAccountCredentials

class dataBase:

    def __init__(self,file_name,json_name):
        '''Constructor for dataBase Class
        PRAMETERS: file_name -> str, json_name -> str
        '''

        self.file_name = file_name #This is the name of a google sheet that you created
        self.json_name = json_name #The name of the json file which downloads when you give google access to your drive

    def createSpreadSheet(self):
        '''Creates a connection to a google spreadsheet'''

        scope = ['https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(str(self.json_name),scope)
        client = gspread.authorize(creds)

        sheet = client.open(str(self.file_name)).sheet1
        return sheet

    def getSpreadSheetData(self):
        '''Returns all values in the spreadsheet in JSON format'''

        sheet = dataBase(self.file_name,self.json_name).createSpreadSheet()
        data = sheet.get_all_records()
        return data

    def updateSpreadSheet(self,row,column,newEntry):
        '''Updates the (row,column) entry of the spreadsheet to new Entry
        PARAMETERS: row -> int, column -> int, newEntry -> str'''

        sheet = dataBase(self.file_name, self.json_name).createSpreadSheet()
        sheet.update_cell(row,column,newEntry)

        return("Database updated successfully.")

    def getRow(self):
        '''Returns the number of rows in the spreadsheet
        PRECONDITION: Must be less then 1000 rows in spreadsheet'''

        count = 0
        sheet = dataBase(self.file_name, self.json_name).createSpreadSheet()

        for number in range(1000):
            if sheet.cell(number + 1,1).value != '':
                count += 1
            else:
                break

        return count

    def getColumn(self):
        '''Returns the number of columns in the spreadsheet
        PRECONDITION: Must be less then 1000 rows in spreadsheet'''

        count = 0
        sheet = dataBase(self.file_name, self.json_name).createSpreadSheet()

        for number in range(1000):
            if sheet.cell(1,number+1).value != '':
                count += 1
            else:
                break

        return count

    def getValue(self,row,column):
        '''Returns the value of cell corresponding to row and column
        PARAMETERS: row -> int, column -> int'''

        sheet = dataBase(self.file_name, self.json_name).createSpreadSheet()
        value = sheet.cell(row,column)

        return value

    def findValue(self,search_value):
        '''Returns the index as a list in the form [row,column] for cell where search_value is. If the search_value
        isn't in the spreadsheet return None
        PARAMETER: search_value -> str'''

        sheet = dataBase(self.file_name, self.json_name).createSpreadSheet()

        try:
            counter = 0
            index = str(sheet.find(search_value))[7:]
            row_number  = ''
            column_number = ''

            for i in range(len(index)):
                if index[i] != 'C':
                    row_number += index[i]
                    counter += 1
                else:
                    break

            index = index[counter +1:]
            for i in range(len(index)):
                if index[i] != ' ':
                    column_number += index[i]
                else:
                    break

            return [int(row_number),int(column_number)]

        except:
            return None








