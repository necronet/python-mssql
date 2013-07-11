import pyodbc
import config
from sqlalchemy import create_engine
import os
import sys

if os.name == 'posix':
    connectionString = "DRIVER={FreeTDS};Server=%s;Database=%s;UID=%s;PWD=%s;TDS_Version=8.0;Port=1433;" % (config.SERVER, config.DB, config.USER, config.PASS)
elif os.name == 'nt':
    print 'NT not yet supported'
    sys.exit()
print "Connecting: %s" % (connectionString)

con = pyodbc.connect(connectionString)

cursor = con.cursor()

cursor.execute("select 2+2 as [Result]")

for row in cursor:
    print row.Result
