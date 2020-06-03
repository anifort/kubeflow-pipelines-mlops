import unittest

from ..Vectorizer import Tokeniser, Vectorizer

class TestVectorizer(unittest.TestCase):

    tok = None;


    def setUp(self):
        self.tok = Tokeniser()
        return

    def tearDown(self):
        return

    def test_tokenise_size(self):
        """
        Test that it can sum a list of integers
        """

        result = Tokeniser.tokenise("this is a nice sentence")
        self.assertEqual(len(result), 5)

    def test_tokenise_size_not_equal(self):
        """
        Test that it can sum a list of integers
        """
        result = self.tok.tokenise("this is a nice sentence")
        self.assertNotEqual(len(result), 3)




    def test_tokenise_size_not_equal_no_sw(self):
        """python -m unittest discover -s tests
        Test that it can sum a list of integers
        """
        result = self.tok.tokenise_no_stopwords("this is a nice sentence")
        self.assertNotEqual(len(result), 3)



    def test_vectoriser(self):
        with self.assertRaises(Exception) as context:
            Vectorizer("file.xml", "gs://a_url/out.pkl")
        self.assertTrue('Data file input should be in CSV', context.exception)