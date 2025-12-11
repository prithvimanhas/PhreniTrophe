def extract_foods(text):
    common = [
        "rice", "pasta", "salad", "chicken", "bread", "fish", "egg", "apple",
        "banana", "pizza", "burger", "soup", "noodles", "cake", "chocolate", "milk"
    ]
    return [f for f in common if f in text]
