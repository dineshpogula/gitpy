import sqlite3

# function to be called to save the data to data base
def createNewTableGitPathToDB(tableName):
    try:
        sqliteConnection = sqlite3.connect('GitPath.db')
        cursor = sqliteConnection.cursor()

        print("Successfully Connected to SQLite")

        # ex :-  sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
        #                                 id INTEGER PRIMARY KEY,
        #                                 name TEXT NOT NULL,ggit
        #                                 email text NOT NULL UNIQUE,
        #                                 joining_date datetime,
        #                                 salary REAL NOT NULL);'''
        #
        sqlite_query = '''CREATE TABLE {}  (
                                       path TEXT);'''.format(tableName)

        cursor.execute(sqlite_query)
        sqliteConnection.commit()
        print("Table Created successfully  ", len(cursor.fetchall()))


        cursor.close()
        sqliteConnection.close()

    except sqlite3.Error as error:
        print("Failed to Create data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def saveGitPathToDB(pathTextInput):
    try:
        sqliteConnection = sqlite3.connect('GitPath.db')
        cursor = sqliteConnection.cursor()

        print("Successfully Connected to SQLite")

        sqlite_insert_query = '''INSERT INTO PathDb VALUES (?)'''
        # If you find it easier to read, you can also use a list literal

        cursor.execute(sqlite_insert_query, (pathTextInput,))
        sqliteConnection.commit()

        print("Record inserted successfully  ", len(cursor.fetchall()))
        cursor.close()
        sqliteConnection.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def retriveStoredDbData():
    try:
        sqliteConnection = sqlite3.connect('GitPath.db')
        cursor = sqliteConnection.cursor()

        print("Successfully Connected to SQLite")

        sqlite_query = """SELECT * from PathDb"""

        cursor.execute(sqlite_query)

        for row in cursor.fetchall():
            print("path: ", row[0])
            print("\n")

        print("Stored Data  ", len(cursor.fetchall()))

        cursor.close()
        sqliteConnection.close()

    except sqlite3.Error as error:
        print("Failed to retrive data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def updateGitPath(pathTextInput):
    try:
        sqliteConnection = sqlite3.connect('GitPath.db')
        cursor = sqliteConnection.cursor()

        print("Successfully Connected to SQLite")

        sqlite_update_query = '''UPDATE PathDb set path = (?) WHERE path = 'Dineshfff' '''

        cursor.execute(sqlite_update_query, (pathTextInput,))
        sqliteConnection.commit()
        print("Table Updated successfully  ", len(cursor.fetchall()))


        cursor.close()
        sqliteConnection.close()

    except sqlite3.Error as error:
        print("Failed to Update data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")