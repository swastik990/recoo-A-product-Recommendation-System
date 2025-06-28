# recommender/views.py

from django.http import JsonResponse
from django.shortcuts import redirect, render
from recommender.recommender_engine import load_product_data, build_similarity_matrix, get_recommendations

try:
    df = load_product_data()
    cosine_sim, df = build_similarity_matrix(df)
except Exception as e:
    print("INITIALIZATION ERROR:", e)
    df = None
    cosine_sim = None

def recommend_products(request, product_id):
    try:
        if df is None or cosine_sim is None:
            raise ValueError("Recommendation engine failed to initialize.")
        
        product_id = int(product_id)
        recommendations = get_recommendations(product_id, cosine_sim, df)
        return JsonResponse({"recommended_products": recommendations}, safe=False)

    except Exception as e:
        print("ERROR in recommend_products view:", e)
        return JsonResponse({"error": str(e)}, status=400)
    
def reco(request):
    return render(request, 'reco.html')