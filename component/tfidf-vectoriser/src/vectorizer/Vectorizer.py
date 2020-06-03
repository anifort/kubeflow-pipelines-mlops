from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import pandas as pd
import _pickle as pickle
import logging

from .cloud_ml_helper import CloudMLHelper

class Tokeniser():

    def __init__(self):
        return

    def tokenise_no_stopwords(self, text_block: str):
        return text_block.split()

    @staticmethod
    def tokenise(text_block: str):
        return text_block.split()



class Vectorizer:

    def __init__(self, csv_data_path: str, uri: str):

        if (not csv_data_path.endswith(".csv")):
            raise TypeError('Data file input should be in CSV')

        if csv_data_path.startswith("gs://"):
            CloudMLHelper.download_from_gcs(csv_data_path)
        else:
            with open(csv_data_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    print(row['Text'])

        data = pd.read_csv(csv_data_path)
        # Preview the first 5 lines of the loaded data

        
        vect = TfidfVectorizer()
        vect.fit(data['Text'])

        logging.info("Feature names of vectorised text : {}", vect.get_feature_names())

        CloudMLHelper.export_to_gcs(vect, uri)
        pickle.dumps(vect)



