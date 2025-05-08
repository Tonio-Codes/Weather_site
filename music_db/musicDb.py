import sqlite3
import pandas as pd

#convert csv file to sqlite3 db
def create_database(path:str):
    connection = sqlite3.connect('music_data_db')
    df = pd.read_csv(path)
    df.columns.str.strip()
    df.to_sql('music_data', connection, if_exists="replace")
    return connection

def fetch_music_list(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT""")

def main():
    path = 'music_db/high_popularity_spotify_data.csv'
    conn = create_database(path)
    cursor = conn.cursor() 
    cursor.execute("""SELECT * 
                   FROM music_data_db""")
    print(cursor.fetchone())
    cursor.close()
    
main()
