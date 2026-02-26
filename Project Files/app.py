import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv

# =========================
# Load environment variables
# =========================
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
API_KEY = os.getenv("GOOGLE_API_KEY")

st.write("API KEY LOADED:", bool(API_KEY))

# =========================
# Gemini setup (stable SDK)
# =========================
try:
    import google.generativeai as genai
except Exception:
    genai = None

client = None
if API_KEY and genai is not None:
    try:
        genai.configure(api_key=API_KEY)
        client = genai
    except Exception:
        client = None

# =========================
# Prompt for SQL generation
# =========================
prompt = """
You are an expert in converting English questions to SQL queries.

The SQL database has one table named Students with the following columns:
name, class, marks, company.

Examples:
How many entries are present?
SQL: SELECT COUNT(*) FROM Students;

Tell me all the students studying in MCom class?
SQL: SELECT * FROM Students WHERE class='MCom';

Only return the SQL query. Do not explain anything.
"""

# =========================
# Gemini → SQL
# =========================
def get_response(que, prompt):
    if not client:
        raise RuntimeError("Google API key not configured.")

    model = client.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt + "\n" + que)

    sql = response.text.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql

# =========================
# Run SQL on SQLite DB
# =========================
def read_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

# =========================
# Pages
# =========================
def page_home():
    st.title("Welcome to IntelliSQL 🚀")
    st.write("Convert natural language into SQL using Gemini LLM")

def page_about():
    st.title("About IntelliSQL")
    st.write("An intelligent SQL querying system powered by Gemini LLM.")

def page_intelligent_query_assistance():
    st.title("Intelligent Query Assistance")

    que = st.text_input("Enter your query:")
    submit = st.button("Get Answer")

    if not client:
        st.warning("Google API key not configured. LLM is disabled.")

        st.markdown("### Manual SQL fallback")
        manual_sql = st.text_area("Enter SQL:")
        if st.button("Run SQL"):
            try:
                rows = read_query(manual_sql, "data.db")
                st.table(rows)
            except Exception as e:
                st.error(e)
        return

    if submit and que:
        try:
            sql = get_response(que, prompt)
            st.markdown("### Generated SQL")
            st.code(sql, language="sql")

            rows = read_query(sql, "data.db")
            st.markdown("### Query Result")
            st.table(rows)

        except Exception as e:
            st.error(e)

# =========================
# Main
# =========================
def main():
    st.set_page_config(page_title="IntelliSQL", layout="wide")

    st.sidebar.title("Navigation")
    pages = {
        "Home": page_home,
        "About": page_about,
        "Intelligent Query Assistance": page_intelligent_query_assistance,
    }

    choice = st.sidebar.radio("Go to", list(pages.keys()))
    pages[choice]()

if __name__ == "__main__":
    main()