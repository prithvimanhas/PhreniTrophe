import json
from core.voice_input import listen_meal
from core.meal_parser import extract_foods
from core.database import Database
from core.image_recognition import ImageRecognizer
from core.nutrition_api import NutritionAPI

def main():
    with open("config.json") as f:
        cfg = json.load(f)

    db = Database(cfg["database"])
    api = NutritionAPI(cfg["nutritionix_app_id"], cfg["nutritionix_app_key"])
    img_ai = ImageRecognizer()

    print("\n🤖 AI Nutrition Assistant — Alpha v1")
    print("[1] Voice Input")
    print("[2] Text Input")
    print("[3] Image File")
    print("[4] Live Camera")
    choice = input("→ Choose mode: ")

    foods = []
    method = ""

    if choice == "1":
        text = listen_meal()
        foods = extract_foods(text or "")
        method = "voice"
    elif choice == "2":
        text = input("📝 Enter meal: ").lower()
        foods = extract_foods(text)
        method = "text"
    elif choice == "3":
        path = input("📸 Enter image path: ")
        foods = img_ai.recognize_file(path)
        method = "image"
    elif choice == "4":
        foods = img_ai.recognize_camera()
        method = "camera"
    else:
        print("❌ Invalid option.")
        return

    total_cal = 0
    for f in foods:
        cal = api.get_calories(f)
        db.add_meal(f, cal, method)
        total_cal += cal
        print(f"🍴 {f}: {cal:.1f} kcal")

    daily = db.get_today_total()
    print("\n📊 Summary:")
    print(f"  ➤ This meal: {total_cal:.1f} kcal")
    print(f"  ➤ Today total: {daily:.1f}/{cfg['daily_goal']} kcal")
    print(f"  ➤ Remaining: {cfg['daily_goal'] - daily:.1f} kcal")

    print("\n📜 Recent Meals:")
    for date, food, cal, method in db.get_recent():
        print(f" - {date} | {food} | {cal:.1f} kcal | via {method}")

if __name__ == "__main__":
    main()
