import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentSearchEngine:
    def __init__(self, size=10, hash_type="sum"):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_type = hash_type  # "sum" or "product"

    def hash_function(self, key):
        if self.hash_type == "sum":
            return sum(ord(char) for char in key) % self.size
        elif self.hash_type == "product":
            hash_value = 1
            for char in key:
                hash_value *= ord(char)
            return hash_value % self.size
        else:
            raise ValueError("Invalid hash type. Use 'sum' or 'product'.")

    def add_document(self, doc_id, content):
        index = self.hash_function(doc_id)
        for item in self.table[index]:
            if item[0] == doc_id:
                logging.warning(f"Document ID '{doc_id}' already exists.")
                return False  # Document ID already exists
        self.table[index].append((doc_id, content))
        logging.info(f"Document '{doc_id}' added successfully at index {index}.")
        return True

    def search_document(self, doc_id):
        index = self.hash_function(doc_id)
        for item in self.table[index]:
            if item[0] == doc_id:
                logging.info(f"Document '{doc_id}' found at index {index}.")
                return item[1]
        logging.warning(f"Document '{doc_id}' not found.")
        return None  # Document not found

    def delete_document(self, doc_id):
        index = self.hash_function(doc_id)
        for item in self.table[index]:
            if item[0] == doc_id:
                self.table[index].remove(item)
                logging.info(f"Document '{doc_id}' deleted from index {index}.")
                return True
        logging.warning(f"Document '{doc_id}' not found for deletion.")
        return False  # Document not found

    def display_table(self):
        logging.info("Hash Table:")
        for i, bucket in enumerate(self.table):
            logging.info(f"Index {i}: {bucket}")

def main():
    # Create a document search engine with sum-based hashing
    logging.info("Initializing Document Search Engine with 'sum' hash type...")
    engine = DocumentSearchEngine(size=5, hash_type="sum")

    # Add documents
    engine.add_document("Doc1", "Content of Document 1")
    engine.add_document("Doc2", "Content of Document 2")
    engine.add_document("Doc3", "Content of Document 3")

    # Display the table
    engine.display_table()

    # Search for documents
    logging.info(f"Searching for 'Doc1': {engine.search_document('Doc1')}")
    logging.info(f"Searching for 'Doc4': {engine.search_document('Doc4')}")

    # Delete a document
    engine.delete_document("Doc1")
    engine.display_table()

    # Add more documents to trigger collision handling
    engine.add_document("DocA", "Content of Document A")
    engine.add_document("DocB", "Content of Document B")
    engine.display_table()

if __name__ == "__main__":
    main()
