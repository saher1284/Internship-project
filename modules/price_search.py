import requests

# -------------------------
# Placeholder Search APIs
# -------------------------

import requests

def usd_to_inr(usd_amount):
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        data = requests.get(url).json()
        rate = data["rates"]["INR"]
        return round(usd_amount * rate, 2)
    except:
        # If API fails, use fallback conversion (1 USD = ₹83)
        return round(usd_amount * 83, 2)

def search_amazon(query):
    """
    Replace with Amazon Product Advertising API.
    """
    return {
        "store": "Amazon",
        "price": 49.99,
        "url": "https://amazon.com/example"
    }

def search_ebay(query):
    """
    Replace with official eBay Browse API.
    """
    return {
        "store": "eBay",
        "price": 44.75,
        "url": "https://ebay.com/example"
    }

def search_walmart(query):
    """
    Replace with Walmart Product Search API.
    """
    return {
        "store": "Walmart",
        "price": 46.20,
        "url": "https://walmart.com/example"
    }

# -------------------------
# Compare All Stores
# -------------------------

def compare_prices(product_name):
    results = [
        search_amazon(product_name),
        search_ebay(product_name),
        search_walmart(product_name)
    ]

    for r in results:
        r["price_inr"] = usd_to_inr(r["price"])
    
    sorted_results = sorted(results, key=lambda x: x["price"])
    return sorted_results
