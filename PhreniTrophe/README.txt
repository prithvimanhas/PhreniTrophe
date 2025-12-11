AI Nutrition Assistant — Alpha v1
=================================

Features:
- Voice input ("I ate pasta and salad")
- Text input
- Image recognition (from file or webcam)
- Real-time calorie fetching via Nutritionix API
- Daily tracking and summary in SQLite

Setup Instructions:
-------------------
1. Install dependencies:
   pip install tensorflow pillow opencv-python requests SpeechRecognition pyaudio numpy

2. Edit config.json:
   Replace "# <-- key here" with your Nutritionix App ID and App Key.

3. Run the app:
   python main.py

4. Choose mode:
   [1] Voice Input
   [2] Text Input
   [3] Image File
   [4] Live Camera

Data is stored locally in 'meals.db'.
