import pypyodbc as odbc
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SqlDataVerifier:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def data_exists(self, symbol, date):
        self.cursor.execute("SELECT *  FROM UNDERLYING WHERE SYMBOL = ? AND MARKETID = ?", (symbol,1))
        underlyingId = 0
        #tester si le cursor est non vide
        symbolExist = False
        symbolAndDateExist= False
        data= self.cursor.fetchall()
        if len(data)!=0:
            underlyingId = data[0][0]
            symbolExist = True
            self.cursor.execute("SELECT *  FROM MARKETDATA JOIN UNDERLYINGMARKETDATA ON MARKETDATA.MARKETDATAID = UNDERLYINGMARKETDATA.MARKETDATAID JOIN UNDERLYING ON UNDERLYINGMARKETDATA.UNDERLYINGID = UNDERLYING.UNDERLYINGID WHERE UNDERLYING.SYMBOL = ? AND MARKETDATA.DATE = ?;", (symbol, date))
            results = self.cursor.fetchall()
            if len(results)!=0:
                symbolAndDateExist=True

        #logging.info(f"Vérification des données pour Symbol={symbol}, Date={date} : {'Données trouvées' if results else 'Aucune donnée trouvée'}")  # Commentaire pour éviter la redondance
        return (symbolExist, symbolAndDateExist,underlyingId)
