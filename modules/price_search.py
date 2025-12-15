from serpapi import GoogleSearch

SERPAPI_KEY = "b8fde7942fb59416addb4364ad0d7e93a464cee692013278df55005dae23f6dc"

# -----------------------------
# Convert USD → INR
# -----------------------------
def usd_to_inr(usd):
    """
    Converts USD to INR.
    Handles both strings like "$49.99" and floats like 49.99
    """
    if isinstance(usd, str):
        usd = usd.replace("$", "").replace(",", "")
    return round(float(usd) * 83, 2)  # Conversion rate: 1 USD = ₹83

# -----------------------------
# Search Google Shopping via SerpAPI
# -----------------------------
def search_serpapi(product):
    params = {
        "engine": "google_shopping",
        "q": product,
        "api_key": SERPAPI_KEY,
        "gl": "In",
        "hl": "en"
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    prices = []
    for item in results.get("shopping_results", []):
        price = item.get("extracted_price")
        store = item.get("source")
        url = item.get("product_link") or item.get("link")
        image = item.get("thumbnail")

        if price is not None:
            prices.append({
                "store": store,
                "price": price,
                "price_inr": usd_to_inr(price),
                "url": url,
                "image": image
            })

    return prices

# -----------------------------
# Sort prices (lowest first)
# -----------------------------
def compare_prices(product):
    results = search_serpapi(product)
    sorted_results = sorted(
        results, 
        key=lambda x: float(str(x["price"]).replace("$", "").replace(",", ""))
    )
    # Return only the 5 cheapest results
    return sorted_results[:5]


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    product_name = "spotlight"
    results = compare_prices(product_name)

    print(f"\nIdentified Product: {product_name}")
    print("Top Results:\n")

    for r in results:
        print(f"Store: {r['store']}")
        print(f"Price: ${r['price']} (₹{r['price_inr']})")
        print("Link:", r["url"])
        print("Image:", r["image"])
        print("-" * 60)
