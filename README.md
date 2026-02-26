# IntelliSQL – Intelligent SQL Querying with LLMs Using Gemini Pro

IntelliSQL is an AI-powered application that allows users to query a database using **natural language**.  
It leverages **Google Gemini Pro (LLM)** to convert plain English questions into SQL queries and executes them on a **SQLite database**, displaying results through a **Streamlit web interface**.

---

## 🚀 Features
- Natural Language → SQL query conversion
- Powered by Google Gemini Pro
- Interactive Streamlit UI
- SQLite database integration
- Beginner-friendly setup
- Real-time query execution

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit**
- **SQLite**
- **Google Gemini API**
- **python-dotenv**

---

## 📂 Project Structure

IntelliSQL-Intelligent-SQL-Querying-with-LLMs-Using-Gemini-Pro
├── Project Files
│ ├── app.py # Streamlit application
│ ├── sql.py # Database creation & sample data
│ ├── requirements.txt # Python dependencies
│ ├── data.db # SQLite database
│ ├── .env.example # Environment variables template (committed)
│ └── .env # Environment variables (create manually, DO NOT commit)


---

## ⚙️ Installation & Setup

Clone the repository and navigate into the project directory, create and activate a virtual environment, install dependencies, configure environment variables, initialize the database, and run the application using the following commands.

```bash
git clone https://github.com/himavarshini38/IntelliSQL-Intelligent-SQL-Querying-with-LLMs-Using-Gemini-Pro.git
cd IntelliSQL-Intelligent-SQL-Querying-with-LLMs-Using-Gemini-Pro

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r "Project Files/requirements.txt"

# Create .env file inside Project Files and add:
# GOOGLE_API_KEY=your_google_gemini_api_key_here

python "Project Files/sql.py"
streamlit run "Project Files/app.py"
