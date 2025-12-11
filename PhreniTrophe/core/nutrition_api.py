import requests

class NutritionAPI:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_calories(self, food):
        url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
        headers = {
            "x-app-id": self.app_id,
            "x-app-key": self.app_key,
            "Content-Type": "application/json"
        }
        try:
            res = requests.post(url, headers=headers, json={"query": food})
            res.raise_for_status()
            data = res.json()
            return data["foods"][0]["nf_calories"]
        except Exception as e:
            print(f"⚠️ Error fetching {food}: {e}")
            return 0
