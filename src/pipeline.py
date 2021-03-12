import mysql.connector
import xml.etree.ElementTree as et
import csv


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user=auth_dict["username"],
                                             password=auth_dict["password"],
                                             host=auth_dict["host"],
                                             port=auth_dict["port"],
                                             database=auth_dict["dbname"])
    except Exception as error:
        print("Error while connecting to database for online sales", error)
    return connection


def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()

    data = csv.reader(open(file_path_csv, "rt"), delimiter=",")
    for row in data:
        sql_statement = "INSERT INTO online_sales.ticket_sale (ticket_id, trans_date, event_id, event_name, " \
                        "event_date, event_type, event_city, event_addr, customer_id, price, num_tickets) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        cursor.execute(sql_statement, values)

    connection.commit()
    cursor.close()
    return


def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = "SELECT * " \
                    "FROM online_sales.ticket_sale " \
                    "ORDER BY num_tickets DESC " \
                    "LIMIT 3"

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records


def print_records(records):
    print(f"Here are the top 3 most popular tickets in the past month: ")
    for x in records:
        print(f"- {x[3]}")


if __name__ == "__main__":
    tree = et.parse('db_auth.xml')
    root = tree.getroot()
    auth_dict = root[0].attrib
    path_dict = root[1].attrib

    db_connection = get_db_connection()
    load_third_party(db_connection, path_dict["path"])
    ticket_data = query_popular_tickets(db_connection)
    print_records(ticket_data)



