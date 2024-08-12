import pypyodbc as odbc
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SQLInserter:
    def __init__(self, conn):  
        self.conn = conn
        self.cursor = conn.cursor()

    def insert_data(self, verifier, reader):
        for row in reader:
            symbol = row['Symbol']
            date = row['Date']

            resultVerifier = verifier.data_exists(symbol, date)
            if resultVerifier[0]==True and resultVerifier[1]==False:
                try:
                    self.cursor.execute("USE MarkIXDB")
                    insert_query = """
                        INSERT INTO MARKETDATA ([DATE], [ISCUTOFF], [PARAMETERSETPERSONALID]) 
                        VALUES (?,? ,?)
                    """
                    insert_query2 = """ INSERT INTO UNDERLYINGMARKETDATA ([MARKETDATAID],[UNDERLYINGID]) VALUES (?,?)"""
                    insert_query3 = """
                        INSERT INTO SPOTMARKETDATA ([MARKETDATAID], [SPOTVALUE]) 
                        VALUES (?, ?)
                    """
                    self.cursor.execute(insert_query,(row['Date'],0,1))
                    self.cursor.execute("SELECT @@IDENTITY")
                    marketdata_id = self.cursor.fetchall()[0][0]
                    underlyingid=resultVerifier[2]
                    self.cursor.execute(insert_query2,(marketdata_id,underlyingid))
                    self.cursor.execute(insert_query3, (marketdata_id, row['Close']))
                    self.conn.commit()  
                    logging.info(f"Inserted row for Symbol: {symbol} Date: {date}")
                except odbc.Error as e:
                    logging.error(f"Erreur SQL lors de l'insertion des données : {e}")
                    # Optionnel : gérer l'erreur plus spécifiquement (rollback, etc.)
            # else:  # Pas besoin de log ici, c'est fait dans data_exists
                # logging.info(f"Symbol {row['Symbol']} de date {row['Date']} déjà présente dans la table. Insertion sautée.")
