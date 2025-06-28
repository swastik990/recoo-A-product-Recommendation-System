# recommender/recommender_engine

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from recommender.models import Products

# Load data from the database
def load_product_data():
    products = Products.objects.all().values(
        'Product_id', 'product_name', 'category', 'description', 'price', 'rating', 'image_url'
    )
    df = pd.DataFrame(products)
    df['text'] = df['description'] + " " + df['category']  # Combine description + category
    return df

# Build similarity matrix
def build_similarity_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['text'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim, df

# Get similar products
def get_recommendations(product_id, cosine_sim, df, top_n=5):
    indices = pd.Series(df.index, index=df['Product_id'])
    
    if product_id not in indices:
        return []

    idx = indices[product_id]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    product_indices = [i[0] for i in sim_scores]
    return df.iloc[product_indices].to_dict(orient='records')
