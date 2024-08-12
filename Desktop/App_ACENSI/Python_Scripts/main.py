from zipExtractor import ZipExtractor
from CSVReader import CsvReader
from Convertor import CSVDateConverter
import database_handler as dh
import logging
import pypyodbc as odbc

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='C:\\Users\\gillian.nahum\\Desktop\\Logfile.log', encoding='utf-8', level=logging.DEBUG)

if __name__ == "__main__":
    zip_path = 'C:\\Users\\gillian.nahum\\Downloads\\AMEX_2023.zip'
    unzip_path = 'C:\\Users\\gillian.nahum\\Downloads\\unFINAL'
    input_folder = unzip_path
    Converted_folder = 'C:\\Users\\gillian.nahum\\Downloads\\FINAL'
    
    
    
    conn='DRIVER={SQL SERVER}; SERVER=FR-LTP-0577\SQLEXPRESS; DATABASE=MarkIXDB; Trust_Connected=yes'
    with odbc.connect(conn) as conn_str:
        # Vérification de la connexion
        if conn_str:
            logging.info("Connexion à la base de données réussie.")
        else:
            logging.error("Échec de la connexion à la base de données.")

        zip_extractor = ZipExtractor(zip_path, unzip_path)
        zip_extractor.unzip_file()

        date_converter = CSVDateConverter(input_folder, Converted_folder)
        date_converter.process_files()

        csv_reader = CsvReader(Converted_folder, conn)
        csv_reader.read_csv_files()
