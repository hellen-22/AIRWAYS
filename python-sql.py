from mysql.connector import connect, Error

try:
    conn = connect(
        host='localhost', 
        database='db_airways', 
        user='root', 
        )
    if conn.is_connected():
        print('Connected to MySQL database')
        cursor = conn.cursor()
        """perform crud operations"""
        # FUNCTION TO INSERT RECORDS
        def insert_record(table_name, column_name, column_value):
            query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, column_name, column_value)
            cursor.execute(query)
            conn.commit()
            print('Record inserted successfully')

        # FUNCTION TO DISPLAY RECORDS
        def get_records(table_name):
            query = "SELECT * FROM {}".format(table_name)
            cursor.execute(query)
            records = cursor.fetchall()
            print(records)

        # FUNCTION TO UPDATE RECORDS
        def update_record(table_name, column_name, column_value, column_name_to_update, column_value_to_update):
            query = "UPDATE {} SET {} = {} WHERE {} = {}".format(table_name, column_name, column_value, column_name_to_update, column_value_to_update)
            cursor.execute(query)
            conn.commit()
            print('Record updated successfully')

        # FUNCTION TO DELETE RECORDS
        def delete_record(table_name, column_name, column_value):
            query = "DELETE FROM {} WHERE {} = {}".format(table_name, column_name, column_value)
            cursor.execute(query)
            conn.commit()
            print('Record deleted successfully')

        add_record = input('Do you want to add a record? (y/n): ')
        if add_record == 'y':
            table_name = input('Enter table name: ')
            column_name = input('Enter All column names: ')
            column_value = input('Enter All values to add: ')
            insert_record(table_name, column_name, column_value)
        if add_record == 'n':
            show_records = input('Do you want to show records? (y/n): ')
            if show_records == 'y':
                table_name = input('Enter table name: ')
                get_records(table_name)
            if show_records == 'n':
                update_record_id = input('Do you want to update a record? (y/n): ')
                if update_record_id == 'y':
                    table_name = input('Enter table name: ')
                    column_name = input('Enter All Column Names: ')
                    column_value = input('Enter values to update ')
                    column_name_to_update = input('Enter ID column name update: ')
                    column_value_to_update = input('Enter ID to update: ')
                    update_record(table_name, column_name, column_value, column_name_to_update, column_value_to_update)
                if update_record_id == 'n':
                    delete_record_id = input('Do you want to delete a record? (y/n): ')
                    if delete_record_id == 'y':
                        table_name = input('Enter table name: ')
                        column_name = input('Enter All Column names: ')
                        column_value = input('Enter ID to be deleted: ')
                        delete_record(table_name, column_name, column_value)
                    if delete_record_id == 'n':
                        print('Thank you for using this application')

        # QUERY TO RETURN A LIST OF PASSENGER IN A SPECIFIC FLIGHT
        query = "SELECT * FROM flight WHERE flight_number = 1"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        cursor.close()
        

    else:
        print('Connection failed')

except Error as e:
    print(e)
