import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000/query"

st.set_page_config(page_title="Agentic AI System", layout="centered")

st.title("🔍 AI-Powered Query System")
st.write("Ask any question and get an AI-generated response!")

# Input Box
query = st.text_input("Enter your query:")

# Submit Button
if st.button("Get Answer"):
    if query:
        with st.spinner("Fetching response..."):
            response = requests.post(FASTAPI_URL, json={"query": query})
            if response.status_code == 200:
                if isinstance(response, bytes):  
                    response = response.decode("utf-8")
    
                answer = response.content
                st.success(answer)
            else:
                st.error("⚠️ Error fetching response. Please try again.")
    else:
        st.warning("⚠️ Please enter a query.")


# Footer
st.markdown("---")
st.markdown("🚀 **Powered by FastAPI & Streamlit**")
