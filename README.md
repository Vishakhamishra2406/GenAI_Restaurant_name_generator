# 🍴 Restaurant Name Generator (AI-powered)

An AI-powered Streamlit app that generates **creative restaurant names** and **popular menu ideas** based on a chosen cuisine.  
It uses **Google Gemini (via LangChain)** to generate responses and **Streamlit** for the frontend.

---
📺 Demo
👉 Try the live demo here: Restaurant Name Generator App

 https://restaurant-app-165165518476.us-central1.run.app


## 🚀 Features
- ✅ Generate a **catchy restaurant name** from a cuisine (e.g., "Italian", "Mexican").  
- ✅ Suggest a **list of menu items** based on the generated restaurant name.  
- ✅ Powered by **Gemini 1.5 Flash** through LangChain.  
- ✅ Simple, interactive Streamlit interface.  

---

## 🛠️ Tech Stack
- [Python 3.10+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – frontend  
- [LangChain](https://www.langchain.com/) – orchestration  
- [Google Generative AI (Gemini)](https://ai.google.dev/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – manage API keys  

---

## 📂 Project Structure
restaurant_name_generator_genai/
│── res.py # Streamlit entry file
│── langchain_helper.py # Core LangChain + Gemini logic
│── requirements.txt # Python dependencies
│── .env # Stores your API key (not uploaded to GitHub)
│── README.md # Documentation

yaml
Copy code

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/restaurant_name_generator_genai.git
cd restaurant_name_generator_genai
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Setup Environment Variables
Create a .env file in the root folder:

ini
Copy code
GOOGLE_API_KEY=your_api_key_here
⚠️ Replace your_api_key_here with your actual Gemini API key from Google AI Studio.

5️⃣ Run the App
bash
Copy code
streamlit run res.py
🌐 Deployment on Streamlit Cloud
Push your code to GitHub.

Go to Streamlit Cloud.

Connect your repo and deploy.

Under Settings → Secrets, add:

ini
Copy code
GOOGLE_API_KEY = "your_api_key_here"
Done ✅ Your app will be live!

📸 Example
Input: Cuisine = Italian
Output:

Restaurant Name: Bella Cucina

Menu Items:

Margherita Pizza

Fettuccine Alfredo

Tiramisu

Bruschetta

Caprese Salad

🧑‍💻 Author
Built by Vishakha Mishra ✨

📜 License
This project is licensed under the MIT License.


