from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# calculate cosine similarities to evaluate how accurate RAG model responds
def cosine_similarity_phrases(phrase1, phrase2):
    
    # vectorize phrases
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([phrase1, phrase2])
    
    # Compute the cosine similarity between the two vectors
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return cosine_sim[0][0]

# function to prompt the RAG model 
# used to evalute model responses for gender bias
def generate_responses(word_list, prompt):
    
    for word in word_list:
        # Construct the query by combining the prompt with the current word
        q = f"{prompt} {word}"
        
        # Query the retriever to fetch relevant context for the word
        d = retriever.query(q)
        
        # Use the RAG model to generate a response with the retrieved context
        generation = rag_chain.invoke({"context": d, "question": q})
        
        # Print the generated response for the current word
        print(f"Response for '{word}':\n{generation}\n")

