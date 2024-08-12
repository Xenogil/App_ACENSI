import csv
import glob
import os
import logging
import pypyodbc as odbc

from SQLDataVerifier import SqlDataVerifier
from SQLInserter import SQLInserter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CsvReader:
    def __init__(self, csv_path, conn_str):
        self.csv_path = csv_path
        self.conn_str = conn_str

    def read_csv_files(self):
        csv_files = sorted(glob.glob(os.path.join(self.csv_path, "*.csv")))
        
        with odbc.connect(self.conn_str) as conn:
            verifier = SqlDataVerifier(conn)
            inserter = SQLInserter(conn)
            
            for csv_file in csv_files:
                logging.info(f"Lecture du fichier {csv_file} en cours...")

                with open(csv_file, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)

                    inserter.insert_data(verifier, reader) 
                    conn.commit() 

                logging.info(f"Lecture du fichier {csv_file} terminée.")
