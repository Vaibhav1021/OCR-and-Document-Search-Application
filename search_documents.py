# search_documents.py

def search_documents(documents, query):
    """
    Search for a keyword within a list of documents.

    Parameters:
    - documents: List of document strings.
    - query: The keyword to search for.

    Returns:
    - results: List of documents containing the keyword.
    """
    results = []
    for doc in documents:
        if query.lower() in doc.lower():
            results.append(doc)
    return results

if __name__ == "__main__":
    documents = ["Document 1 content", "Document 2 content", "Some other content"]
    query = "Document"
    results = search_documents(documents, query)
    print(results)
