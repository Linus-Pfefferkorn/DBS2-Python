import pyodbc

def getConn ():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=141.56.2.45;"
                          "Database=iw21s84623;"
                          "uid=s84623;pwd=s84623")
    return cnxn
