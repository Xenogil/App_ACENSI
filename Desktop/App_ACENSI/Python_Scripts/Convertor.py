import os
import pandas as pd

class CSVDateConverter:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def modify_date_format(self, file_path, output_path):
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y').dt.strftime('%Y-%d-%m %H:%M:%S')
        df.to_csv(output_path, index=False)

    def process_files(self):
        # Créer le dossier de sortie s'il n'existe pas
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Parcourir tous les fichiers CSV dans le dossier d'entrée
        for filename in os.listdir(self.input_folder):
            if filename.endswith('.csv'):
                input_file = os.path.join(self.input_folder, filename)
                output_file = os.path.join(self.output_folder, filename)
                self.modify_date_format(input_file, output_file)

        print("Tous les fichiers ont été traités avec succès.")
