#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon July 31 22:32:00 PDT 2018
# FILENAME: pyodbc_mssqldbtest.py
# =============================================================================
"""The Module Has Been Build for Interaction with MSSQL DBs To Test the con."""
# =============================================================================
# Thanks to this post for headers https://stackoverflow.com/q/12704305/1896134
# Answer to an SO question: https://stackoverflow.com/q/42433408/1896134
# =============================================================================

import pyodbc


def runningwithqueries(query):
    """The Module Has Been Build to {Open, Run & Close} query connection."""
    print("\nRunning Query: " + str(query) + "\nResult :\n")
    crsr = cnxn.execute(query)
    columns = [column[0] for column in crsr.description]
    print(columns)
    for row in crsr.fetchall():
        print(row)
    crsr.close()

# =============================================================================
# SET VARIABLES NEEDED FOR SERVER CONNECTION
# =============================================================================
server = 'yourusername'
username = 'yourusername'
password = 'yourforgottencomplicatedpassword'
database = 'yourdatabase'

connStr = (r'DRIVER={ODBC Driver 17 for SQL Server};' +
           r"Integrated Security=True;" +
           r'SERVER=' + server +
           r';UID=' + username +
           r';PWD=' + password +
           r';DSN=MSSQL-PYTHON' +
           r';DATABASE=' + database + ';'
           )

print("Your Connection String:\n" + str(connStr) + "\n\n")

# =============================================================================
# CONNECT TO THE DB
# =============================================================================
cnxn = pyodbc.connect(connStr, autocommit=True)

# =============================================================================
# SET QUERIES TO VARIABLES
# =============================================================================
SQLQUERY1 = ("SELECT @@VERSION;")
SQLQUERY2 = ("SELECT * FROM sys.schemas;")
SQLQUERY3 = ("SELECT * FROM INFORMATION_SCHEMA.TABLES;")
SQLQUERY4 = ("SELECT * FROM INFORMATION_SCHEMA.COLUMNS;")
SQLQUERY5 = ("SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;")
SQLQUERY6 = ("EXEC sp_databases;")
SQLQUERY7 = ("EXEC sp_who2 'active';")

# =============================================================================
# RUN QUERIES
# YOU CAN RUN AS MANY QUERIES AS LONG AS THE CONNECTION IS OPEN TO THE DB
# =============================================================================
runningwithqueries(SQLQUERY1)
runningwithqueries(SQLQUERY2)
runningwithqueries(SQLQUERY3)
runningwithqueries(SQLQUERY4)
runningwithqueries(SQLQUERY5)
runningwithqueries(SQLQUERY6)
runningwithqueries(SQLQUERY7)

# =============================================================================
# CLOSE THE CONNECTION TO THE DB
# =============================================================================
cnxn.close()
