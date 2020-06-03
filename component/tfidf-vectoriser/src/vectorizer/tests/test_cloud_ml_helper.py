import unittest, mock
from google.cloud import storage
from ..cloud_ml_helper import CloudMLHelper
'''
class TestCloudMLHelper(unittest.TestCase):

    def setUp(self):
        storage.Client = mock.Mock(return_value = storage.Client())
        storage.Client().bucket = mock.Mock(return_value="st")
        return

    def tearDown(self):
        return

    def test_get_blob(self):
        storage.Client().bucket.assert_called_once()
        storage.Client().bucket.assert_called_once_with("gs://skubeflow_pipelines_sentiment")
        blob = CloudMLHelper.get_blob('gs://kubeflow_pipelines_sentiment/data/test.csv');
        print(type(blob))
'''