# Document Search Engine

## Description
This project implements a hash table-based document search engine to enable quick retrieval of documents by their unique IDs in **constant time**. The hash table uses **chaining** to handle collisions and supports two hashing algorithms:
1. **Sum-Based Hashing**: Sums the ASCII values of the characters in the document ID.
2. **Product-Based Hashing**: Multiplies the ASCII values of the characters in the document ID.

The implementation includes methods for adding, searching, and deleting documents.

---

## Features
- **Fast Retrieval**: Search for documents by ID in O(1) time on average.
- **Collision Handling**: Uses chaining to handle hash collisions.
- **Two Hashing Methods**:
  - Sum-based hashing for index calculation.
  - Product-based hashing for index calculation.
- **Customizable Hash Table Size**.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/DocumentSearchEngine.git

## Code Explanation

### 1. **Hash Table Design**

The hash table is implemented as a list of lists. Each index in the list represents a bucket, and each bucket stores key-value pairs (document ID and content). Collisions are handled by appending multiple entries to the same bucket.
