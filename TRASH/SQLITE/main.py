import sqlite3
from sqlite3 import OperationalError

connection = sqlite3.connect("tracker.db")
cursor = connection.cursor()

def create_table():
    try:
        cursor.execute(
            "CREATE TABLE links(channel_id TEXT,posted_links TEXT,error_links TEXT,all_links TEXT,query_link TEXT)")
        connection.commit()

    except OperationalError:
        pass


def insert_data(channel_id, posted_links, error_links, all_links, query_link):
    cursor.execute("INSERT INTO links VALUES(?,?,?,?,?)", (channel_id, posted_links, error_links, all_links, query_link))
    connection.commit()
    cursor.execute("select * from links")
    print(cursor.fetchall())











create_table()

channel_id = "-12222"
posted_links = "a, cd, cd, cd, cd, cd, cd, cd, cd, cd"
error_links = "a, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd"
all_links = "a, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd, cd "
query_link = "link.com"

insert_data(channel_id, posted_links, error_links, all_links, query_link)
connection.close()

# cursor.execute("""
# INSERT TABLE links(-12505,posted_links,error_links,all_links,query_link)
# """)


# when making things persistent use this: now persistence should be manual by passing force_id
# self.object_data = {
# "channel_id": "",
# "all_links": [],
# "posted_links": [],
# "error_links": [],
# }

#
# connection.commit()
# connection.cursor().fetchall()
# connection.cursor().fetchmany()
# connection.cursor().fetchone()
# connection.close()
