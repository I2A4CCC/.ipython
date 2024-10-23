# creating  a while loop

import os
import re
from collections import defaultdict

# Step 1: Load documents from a directory
def load_documents(directory):
    documents = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                documents[filename] = file.read()
    return documents

# Step 2: Tokenize the content of documents
def tokenize(text):
    # Remove punctuation and make all text lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Step 3: Build an inverted index (word -> list of document names)
def build_inverted_index(documents):
    index = defaultdict(list)
    for doc_name, content in documents.items():
        words = tokenize(content)
        for word in words:
            index[word].append(doc_name)
    return index

# Step 4: Search query and return matching documents
def search(query, index):
    words = tokenize(query)
    if not words:
        return []
    
    # Initialize result set with the documents of the first word
    result = set(index[words[0]])
    
    # Perform intersection for each subsequent word in the query
    for word in words[1:]:
        result.intersection_update(index[word])
        
    return result

# Step 5: Rank results based on the frequency of search terms in documents
def rank_results(query, docs, results):
    words = tokenize(query)
    scores = {}
    for doc in results:
        content = docs[doc]
        # Count occurrences of each search word in the document
        score = sum(content.count(word) for word in words)
        scores[doc] = score
    # Sort documents by score in descending order
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# Step 6: Main function to run the search engine
def main():
    directory = input("Enter the directory path containing text files: ")
    
    # Load and index documents
    documents = load_documents(directory)
    inverted_index = build_inverted_index(documents)
    
    while True:
        query = input("Enter your search query (or type 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            break
        
        # Search and rank results
        results = search(query, inverted_index)
        if results:
            ranked_results = rank_results(query, documents, results)
            print("\nSearch Results:")
            for doc, score in ranked_results:
                print(f"{doc} (Relevance Score: {score})")
        else:
            print("No matching documents found.\n")

# Run the search engine
if __name__ == "__main__":
    main()

