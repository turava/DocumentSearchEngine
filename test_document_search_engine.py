import unittest
from document_search_engine import DocumentSearchEngine

class TestDocumentSearchEngine(unittest.TestCase):

    def setUp(self):
        self.engine_sum = DocumentSearchEngine(size=5, hash_type="sum")
        self.engine_product = DocumentSearchEngine(size=5, hash_type="product")

    def test_add_and_search_document_sum(self):
        self.assertTrue(self.engine_sum.add_document("Doc1", "Content of Document 1"))
        self.assertEqual(self.engine_sum.search_document("Doc1"), "Content of Document 1")
        self.assertFalse(self.engine_sum.add_document("Doc1", "Another Content"))

    def test_add_and_search_document_product(self):
        self.assertTrue(self.engine_product.add_document("Doc2", "Content of Document 2"))
        self.assertEqual(self.engine_product.search_document("Doc2"), "Content of Document 2")
        self.assertFalse(self.engine_product.add_document("Doc2", "Another Content"))

    def test_delete_document_sum(self):
        self.engine_sum.add_document("Doc1", "Content of Document 1")
        self.assertTrue(self.engine_sum.delete_document("Doc1"))
        self.assertIsNone(self.engine_sum.search_document("Doc1"))

    def test_delete_document_product(self):
        self.engine_product.add_document("Doc2", "Content of Document 2")
        self.assertTrue(self.engine_product.delete_document("Doc2"))
        self.assertIsNone(self.engine_product.search_document("Doc2"))

    def test_collision_handling_sum(self):
        # Add two documents with colliding indices
        self.engine_sum.add_document("DocA", "Content A")
        self.engine_sum.add_document("DocB", "Content B")
        self.assertEqual(self.engine_sum.search_document("DocA"), "Content A")
        self.assertEqual(self.engine_sum.search_document("DocB"), "Content B")

    def test_collision_handling_product(self):
        # Add two documents with colliding indices
        self.engine_product.add_document("DocC", "Content C")
        self.engine_product.add_document("DocD", "Content D")
        self.assertEqual(self.engine_product.search_document("DocC"), "Content C")
        self.assertEqual(self.engine_product.search_document("DocD"), "Content D")


if __name__ == "__main__":
    unittest.main()
