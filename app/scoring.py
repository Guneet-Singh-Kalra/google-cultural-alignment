def calculate_hipo(responses):
    # Logic to check Q7 for initiative
    keywords = ["initiative", "self-taught", "growth", "learning"]
    q7 = responses.get("Q7", "").lower()
    is_hipo = any(word in q7 for word in keywords)
    return is_hipo