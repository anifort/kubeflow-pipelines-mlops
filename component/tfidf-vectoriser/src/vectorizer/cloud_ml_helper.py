import datetime
from google.cloud import storage
import logging
import codecs

try:
    import cPickle as pickle
except:
    import _pickle as pickle


class CloudMLHelper():


    @staticmethod
    def get_blob(uri: str):
        if not uri.startswith("gs://"):
            raise TypeError("uri is not gs://")

        print(storage.Client().bucket(uri[0]))
        uri = uri.split("gs://")[1].split("/")
        return storage.Client().bucket(uri[0]).blob('{}'.format('/'.join(uri[1:])))


    @staticmethod
    def download_from_gcs(uri: str):

        blob = CloudMLHelper.get_blob(uri)

        destination_file_name = "/tmp/data.csv"
        blob.download_to_filename(destination_file_name)

        logging.info('\t------- Blob data downloaded to {}'
            .format(destination_file_name))

        return destination_file_name




    @staticmethod
    def export_to_gcs(obj: object, uri: str):

        blob = CloudMLHelper.get_blob(uri)

        blob.upload_from_string(pickle.dumps(obj))

        logging.info("\t------- Model exported to : {}".format(uri))

    @staticmethod
    def load_pkl(loc):
        if loc.startswith("gs://"):
            return CloudMLHelper.load_pkl_from_gcs(loc)
        else:
            return CloudMLHelper.load_pkl_from_local(loc)

    @staticmethod
    def load_pkl_from_gcs(uri):

        uri = uri[5:]
        uri_parts = uri.split("/")
        bucket_name = uri_parts[0]
        source_blob_name = "/".join(uri_parts[1:])

        blob = storage.Client().bucket(bucket_name).blob("/".join(uri_parts[1:]))
        mstr = blob.download_as_string()
        return pickle.loads(mstr, encoding='latin1')

    @staticmethod
    def load_pkl_from_local(path):
        with open(path, "rb") as myfile:
            return pickle.loads(myfile.read(), encoding='latin1')
        return None