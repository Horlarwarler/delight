import copy
import sqlite3

mapper = {int:'INTEGER', str:"TEXT", float:'REAL'}


class Product:
    def __init__(self, productName, supplier, quantity, cost, price):
        self.name = productName
        self.supplier = supplier
        self.quantity = quantity
        self.cost = cost
        self.price = price

    def getAttributes(self):
        return tuple(vars(self).values())

    def identifier(self):
        return 'productid'

class TransactionOrder:    
    def __init__(self, billnumber, clientname, clientaddress, phonenumber, date, productname, quantity, totalamount):
        self.billnumber  = billnumber
        self.clientname = clientname
        self.clientaddress = clientaddress
        self.phonenumber = phonenumber
        self.date = date
        self.productname = productname
        self.quantity = quantity
        self.amount = totalamount
    
    def getAttributes(self):
        return tuple(vars(self).values())

    def identifier(self):
        return 'billnumber'

    @staticmethod
    def generateBillNumber():
        return f"BILL-"



class Report:
    def __init__(self, customer, type, date, productName, quantity, amount, month):
        self.customer = customer
        self.type = type        
        self.date = date
        self.productname = productName
        self.quantity = quantity
        self.amount = amount
        self.month = month

        

class Database:
    def __init__(self, dbfile, modelInstance, primaryKey=None, autoincreament = True):
        self.__dbfile = dbfile
        self.__model = modelInstance
        self.__tablename = type(modelInstance).__name__.lower()

        self.__tabledata = None
        self.__primaryKey = primaryKey
        self.__autoincreament = autoincreament

        self.createTable()

    def executeSQLcommand(self, sqlcommand, executeArgs = tuple(), commit = False, fetchresult=False):
        db = sqlite3.connect(self.__dbfile)
        cursor = db.cursor()
        cursor.execute(sqlcommand, executeArgs)

        if fetchresult:
            result = cursor.fetchall()
        else:
            result = None
        
        if commit:
            db.commit()
        db.close()
        return result
        
    def createTable(self):
        attributes = copy.deepcopy(vars(self.__model))

        sqlcommand = f'''CREATE TABLE IF NOT EXISTS {self.__tablename}('''

        if self.__primaryKey or self.__autoincreament:
            value = attributes.get(self.__primaryKey)

            self.__primaryKey = self.__primaryKey if self.__primaryKey else 'id'

            datatype = 'INTEGER' if  not value else  mapper[type(attributes.get(self.__primaryKey))]

            sqlcommand = f'''{sqlcommand}
                {self.__primaryKey} {datatype} PRIMARY KEY {(lambda x: 'AUTOINCREMENT' if x == 'INTEGER' else 'NOT NULL')(datatype)},'''
            attributes.pop(self.__primaryKey, None)
        
        for name, data in attributes.items():
            datatype = mapper[type(data)]

            sqlcommand = f'''{sqlcommand}
                {name} {datatype} NOT NULL,'''
               
        sqlcommand = sqlcommand.rstrip(',')  + ');'

        self.executeSQLcommand(sqlcommand, commit=True)
    
    def readAllrows(self):
        '''Read all rows from the table'''
        if self.__tabledata != None:
            return self.__tabledata
        
        sqlcommand = f'''
        SELECT * FROM {self.__tablename};
        '''
        self.__tabledata = self.executeSQLcommand(sqlcommand, fetchresult=True)
        return self.__tabledata

    def readColumn(self, columns:tuple):
        '''Select completely a paticular column or columns from the table

        ### Arguments
        columns: list of columns to be selected
        '''
        sqlcommand = f'''SELECT {", ".join(columns)} FROM {self.__tablename};'''
        return self.executeSQLcommand(sqlcommand, fetchresult=True)

    def readSpecificRow(self, columns:tuple, values:tuple, conjunction='AND'):
        '''Read specific rows from the table based on some column values

        ### Arguments
        column: list of columns to filter by
        values: value of columns to filter by
        conjunction: Logical Operators (AND, OR)
        '''

        sqlcommand = f'''
        SELECT * FROM {self.__tablename} WHERE {(' %s '%(conjunction)).join(['%s = ?'%(i) for i in columns])};
        '''        
        return self.executeSQLcommand(sqlcommand, values, fetchresult=True)

    def readSpecificColumn(self, selectionColumn:tuple, columns:tuple, values:tuple, conjuction='AND'):
        '''Read specific columns of some rows from the table based on some column values
        
        ### Arguments
        selectionColumn: list of columns to be selected
        column: list of columns to filter by
        values: value of columns to filter by
        conjunction: Logical Operators (AND, OR)
        '''

        sqlcommand = f'''
        SELECT {", ".join(selectionColumn)} FROM {self.__tablename} WHERE {(' %s '%(conjuction)).join(['%s = ?'%(i) for i in columns])};
        '''        
        return self.executeSQLcommand(sqlcommand, values, fetchresult=True)

    def deleteRow(self, data, usePrimaryKey = True):
        '''Delete a row from the table selected using the primary key or another column

        ### Argumnets
        data: a tuple of column name and its value OR a single value if usePrimaryKey=True

        usePrimaryKey: To use primary key to select a row otherwise uses the column and value supplied in the data variable
        '''
        if usePrimaryKey:
            column = self.__primaryKey
            value = data
        else:
            column, value = data
        sqlcommand = f'''
        DELETE FROM {self.__tablename} WHERE {column} = ?;
        '''        
        self.executeSQLcommand(sqlcommand, (value, ), commit=True)
        self.__tabledata = None
    
    def deleteAll(self):
        '''Delete all entries of the table'''

        sqlcommand = f'''
        DELETE FROM {self.__tablename};'''

        self.executeSQLcommand(sqlcommand, commit=True)
        self.__tabledata = None

    def addRow(self, modelInstance):
        """Add a new entry to the table
        
        Takes an instance of the model class as argument 
        """
        data = []
        sqlcommand = f'INSERT INTO {self.__tablename}('
        for name, value in vars(modelInstance).items():
            sqlcommand += name + ', '
            data.append(value)
        sqlcommand = sqlcommand.rstrip(', ') + ')'
        sqlcommand = f'''{sqlcommand} VALUES({', '.join(list('?' * len(data)))})
        '''
        self.__tabledata = None

        self.executeSQLcommand(sqlcommand, data, commit=True)

    def updateRow(self, selectcolumn, value, columns, values):
        sqlcommand = f'''
        UPDATE product SET {', '.join(['%s = ?'%(i) for i in columns])} WHERE {selectcolumn} = ?
        '''
        values = [*values, value]
        self.executeSQLcommand(sqlcommand, values, commit=True)
        self.__tabledata = None
    
    @property
    def totalRow(self):
        return len(self.readAllrows())



productInstance = Product('Product', 'Delight', 1, 1.0, 1.0)
orderInstance = TransactionOrder('BILL1234', 'ClientName', 'ClientAddress', '+2345678990', '18-03-2022', 'Ford', 1, 1.0)
reportInstance = Report('customerName', 'Sales', '19-03-2022', 'ProductName', 1, 1.0, 'Month')


dbfile = 'AppData.db'
PRODUCT = Database(dbfile, productInstance, productInstance.identifier())
ORDER = Database(dbfile, orderInstance)
REPORT = Database(dbfile, reportInstance)

#print(PRODUCT.readSpecificColumn(('name', 'price', 'quantity'), ('name', 'quantity'), ('Rodeo', 3071), conjuction='OR'))

