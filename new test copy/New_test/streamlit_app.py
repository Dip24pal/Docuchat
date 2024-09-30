import streamlit as st
import requests
import os
from pathlib import Path
from data_uploader import save_pdf
from arxiv_search import fetch_arxiv_papers  # Import the search function

st.set_page_config(page_title="Pathway LLM Interface", layout="wide")

st.title("Pathway LLM Interface")
st.header("Document Interaction")

with st.sidebar:
    st.image("https://static.vecteezy.com/system/resources/thumbnails/010/214/734/small_2x/llm-letter-technology-logo-design-on-white-background-llm-creative-initials-letter-it-logo-concept-llm-letter-design-vector.jpg", use_column_width=True)
    st.subheader("Navigation")
    nav = st.radio("Go to", ["Upload Documents", "Manage Documents", "Ask Questions", "Search research articles"]) 
    st.markdown("---")
    st.info("Developed by Prem")

data_directory = Path("/app/data")

if not data_directory.exists():
    data_directory.mkdir(parents=True)

def list_documents():
    return [f.name for f in data_directory.glob("*.pdf")]

if nav == "Upload Documents":
    st.subheader("Upload PDF Files")
    uploaded_files = st.file_uploader("Choose PDF files to upload", type="pdf", accept_multiple_files=True)
    
    if st.button("Upload"):
        if uploaded_files:
            with st.spinner("Uploading files..."):
                for uploaded_file in uploaded_files:
                    file_path = save_pdf(uploaded_file, str(data_directory))
                    if file_path:
                        st.success(f"Successfully uploaded {uploaded_file.name}.")
                    else:
                        st.error(f"Failed to upload {uploaded_file.name}.")
        else:
            st.warning("No files selected for upload.")
    
    st.markdown("---")
    st.subheader("Uploaded Documents")
    documents = list_documents()
    if documents:
        for doc in documents:
            st.write(f"- {doc}")
    else:
        st.info("No documents uploaded yet.")

elif nav == "Manage Documents":
    st.subheader("Manage Uploaded Documents")
    documents = list_documents()
    
    if documents:
        for doc in documents:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(doc)
            with col2:
                delete = st.button("Delete", key=doc)
                if delete:
                    try:
                        (data_directory / doc).unlink()
                        st.success(f"Deleted {doc}")
                        st.rerun()  # Updated here
                    except Exception as e:
                        st.error(f"Error deleting {doc}: {e}")
    else:
        st.info("No documents to manage.")

elif nav == "Ask Questions":
    st.subheader("Ask Questions About Your Documents")
    
    documents = list_documents()
    
    if documents:
        selected_doc = st.selectbox("Select a document", documents)
    else:
        st.warning("No documents available. Please upload a document first.")
        selected_doc = None
    
    prompt = st.text_area("Enter your question:")
    
    if st.button("Get Answer"):
        if selected_doc and prompt.strip():
            with st.spinner("Fetching answer..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/v1/pw_ai_answer",
                        json={"prompt": prompt, "document": selected_doc}
                    )
                    if response.status_code == 200:
                        answer = response.json()
                        st.success("Answer:")
                        st.write(answer)
                    else:
                        st.error("Failed to get answer from the backend.")
                except requests.exceptions.RequestException as e:
                    st.error(f"API request failed: {e}")
        else:
            st.warning("Please select a document and enter a question.")

elif nav == "Search research articles": 
    st.subheader("Search for Research Papers on arXiv")
    topic = st.text_input("Enter a topic to search:")
    max_results = st.number_input("Max results", min_value=1, max_value=100, value=10)

    if st.button("Search"):
        if topic.strip():
            with st.spinner("Searching for papers..."):
                research_articles = fetch_arxiv_papers(topic, max_results)
                if research_articles:
                    st.success(f"Found {len(research_articles)} papers:")
                    for article in research_articles:
                        st.write(f"**Title:** {article['title']}")
                        st.write(f"**Published:** {article['published']}")
                        st.write(f"**Summary:** {article['summary']}")
                        st.write(f"[View Paper](https://arxiv.org/abs/{article['arxiv_id']})")
                else:
                    st.warning("No papers found for this topic.")
        else:
            st.warning("Please enter a topic.")

st.markdown("---")
st.write("© 2024 Your Company Name. All rights reserved.")
































# import streamlit as st
# import requests
# import os
# from pathlib import Path
# from data_uploader import save_pdf
# from arxiv_search import fetch_arxiv_papers  # Import the search function

# st.set_page_config(page_title="Pathway LLM Interface", layout="wide")

# st.title("Pathway LLM Interface")
# st.header("Document Interaction")

# with st.sidebar:
#     st.image("https://static.vecteezy.com/system/resources/thumbnails/010/214/734/small_2x/llm-letter-technology-logo-design-on-white-background-llm-creative-initials-letter-it-logo-concept-llm-letter-design-vector.jpg", use_column_width=True)
#     st.subheader("Navigation")
#     nav = st.radio("Go to", ["Upload Documents", "Manage Documents", "Ask Questions", "Search research articles"]) 
#     st.markdown("---")
#     st.info("Developed by Prem")

# data_directory = Path("/app/data")

# if not data_directory.exists():
#     data_directory.mkdir(parents=True)

# def list_documents():
#     return [f.name for f in data_directory.glob("*.pdf")]

# if nav == "Upload Documents":
#     st.subheader("Upload PDF Files")
#     uploaded_files = st.file_uploader("Choose PDF files to upload", type="pdf", accept_multiple_files=True)
    
#     if st.button("Upload"):
#         if uploaded_files:
#             with st.spinner("Uploading files..."):
#                 for uploaded_file in uploaded_files:
#                     file_path = save_pdf(uploaded_file, str(data_directory))
#                     if file_path:
#                         st.success(f"Successfully uploaded {uploaded_file.name}.")
#                     else:
#                         st.error(f"Failed to upload {uploaded_file.name}.")
#         else:
#             st.warning("No files selected for upload.")
    
#     st.markdown("---")
#     st.subheader("Uploaded Documents")
#     documents = list_documents()
#     if documents:
#         for doc in documents:
#             st.write(f"- {doc}")
#     else:
#         st.info("No documents uploaded yet.")

# elif nav == "Manage Documents":
#     st.subheader("Manage Uploaded Documents")
#     documents = list_documents()
    
#     if documents:
#         for doc in documents:
#             col1, col2 = st.columns([4, 1])
#             with col1:
#                 st.write(doc)
#             with col2:
#                 delete = st.button("Delete", key=doc)
#                 if delete:
#                     try:
#                         (data_directory / doc).unlink()
#                         st.success(f"Deleted {doc}")
#                         st.experimental_rerun()
#                     except Exception as e:
#                         st.error(f"Error deleting {doc}: {e}")
#     else:
#         st.info("No documents to manage.")

# elif nav == "Ask Questions":
#     st.subheader("Ask Questions About Your Documents")
    
#     documents = list_documents()
    
#     if documents:
#         selected_doc = st.selectbox("Select a document", documents)
#     else:
#         st.warning("No documents available. Please upload a document first.")
#         selected_doc = None
    
#     prompt = st.text_area("Enter your question:")
    
#     if st.button("Get Answer"):
#         if selected_doc and prompt.strip():
#             with st.spinner("Fetching answer..."):
#                 try:
#                     response = requests.post(
#                         "http://localhost:8000/v1/pw_ai_answer",
#                         json={"prompt": prompt, "document": selected_doc}
#                     )
#                     if response.status_code == 200:
#                         answer = response.json()
#                         st.success("Answer:")
#                         st.write(answer)
#                     else:
#                         st.error("Failed to get answer from the backend.")
#                 except requests.exceptions.RequestException as e:
#                     st.error(f"API request failed: {e}")
#         else:
#             st.warning("Please select a document and enter a question.")

# elif nav == "Search research articles": 
#     st.subheader("Search for Research Papers on arXiv")
#     topic = st.text_input("Enter a topic to search:")
#     max_results = st.number_input("Max results", min_value=1, max_value=100, value=10)

#     if st.button("Search"):
#         if topic.strip():
#             with st.spinner("Searching for papers..."):
#                 research_articles = fetch_arxiv_papers(topic, max_results)
#                 if research_articles:
#                     st.success(f"Found {len(research_articles)} papers:")
#                     for article in research_articles:
#                         st.write(f"**Title:** {article['title']}")
#                         st.write(f"**Published:** {article['published']}")
#                         st.write(f"**Summary:** {article['summary']}")
#                         st.write(f"[View Paper](https://arxiv.org/abs/{article['arxiv_id']})")
#                 else:
#                     st.warning("No papers found for this topic.")
#         else:
#             st.warning("Please enter a topic.")

# st.markdown("---")
# st.write("© 2024 Your Company Name. All rights reserved.")












# import streamlit as st
# import requests
# import os
# from pathlib import Path
# from data_uploader import save_pdf
# from arxiv_search import fetch_arxiv_papers  # Import the search function

# st.set_page_config(page_title="Pathway LLM Interface", layout="wide")

# st.title("Pathway LLM Interface")
# st.header("Document Interaction")

# with st.sidebar:
#     st.image("https://static.vecteezy.com/system/resources/thumbnails/010/214/734/small_2x/llm-letter-technology-logo-design-on-white-background-llm-creative-initials-letter-it-logo-concept-llm-letter-design-vector.jpg", use_column_width=True)
#     st.subheader("Navigation")
#     nav = st.radio("Go to", ["Upload Documents", "Manage Documents", "Ask Questions", "Search arXiv"])
#     st.markdown("---")
#     st.info("Developed by Prem")

# data_directory = Path("/app/data")

# if not data_directory.exists():
#     data_directory.mkdir(parents=True)

# def list_documents():
#     return [f.name for f in data_directory.glob("*.pdf")]

# if nav == "Upload Documents":
#     st.subheader("Upload PDF Files")
#     uploaded_files = st.file_uploader("Choose PDF files to upload", type="pdf", accept_multiple_files=True)
    
#     if st.button("Upload"):
#         if uploaded_files:
#             with st.spinner("Uploading files..."):
#                 for uploaded_file in uploaded_files:
#                     file_path = save_pdf(uploaded_file, str(data_directory))
#                     if file_path:
#                         st.success(f"Successfully uploaded {uploaded_file.name}.")
#                     else:
#                         st.error(f"Failed to upload {uploaded_file.name}.")
#         else:
#             st.warning("No files selected for upload.")
    
#     st.markdown("---")
#     st.subheader("Uploaded Documents")
#     documents = list_documents()
#     if documents:
#         for doc in documents:
#             st.write(f"- {doc}")
#     else:
#         st.info("No documents uploaded yet.")

# elif nav == "Manage Documents":
#     st.subheader("Manage Uploaded Documents")
#     documents = list_documents()
    
#     if documents:
#         for doc in documents:
#             col1, col2 = st.columns([4, 1])
#             with col1:
#                 st.write(doc)
#             with col2:
#                 delete = st.button("Delete", key=doc)
#                 if delete:
#                     try:
#                         (data_directory / doc).unlink()
#                         st.success(f"Deleted {doc}")
#                         st.experimental_rerun()
#                     except Exception as e:
#                         st.error(f"Error deleting {doc}: {e}")
#     else:
#         st.info("No documents to manage.")

# elif nav == "Ask Questions":
#     st.subheader("Ask Questions About Your Documents")
    
#     documents = list_documents()
    
#     if documents:
#         selected_doc = st.selectbox("Select a document", documents)
#     else:
#         st.warning("No documents available. Please upload a document first.")
#         selected_doc = None
    
#     prompt = st.text_area("Enter your question:")
    
#     if st.button("Get Answer"):
#         if selected_doc and prompt.strip():
#             with st.spinner("Fetching answer..."):
#                 try:
#                     response = requests.post(
#                         "http://localhost:8000/v1/pw_ai_answer",
#                         json={"prompt": prompt, "document": selected_doc}
#                     )
#                     if response.status_code == 200:
#                         answer = response.json()
#                         st.success("Answer:")
#                         st.write(answer)
#                     else:
#                         st.error("Failed to get answer from the backend.")
#                 except requests.exceptions.RequestException as e:
#                     st.error(f"API request failed: {e}")
#         else:
#             st.warning("Please select a document and enter a question.")

# elif nav == "Search arXiv":
#     st.subheader("Search for Research Papers on arXiv")
#     topic = st.text_input("Enter a topic to search:")
#     max_results = st.number_input("Max results", min_value=1, max_value=100, value=10)

#     if st.button("Search"):
#         if topic.strip():
#             with st.spinner("Searching for papers..."):
#                 research_articles = fetch_arxiv_papers(topic, max_results)
#                 if research_articles:
#                     st.success(f"Found {len(research_articles)} papers:")
#                     for article in research_articles:
#                         st.write(f"**Title:** {article['title']}")
#                         st.write(f"**Published:** {article['published']}")
#                         st.write(f"**Summary:** {article['summary']}")
#                         st.write(f"[View Paper](https://arxiv.org/abs/{article['arxiv_id']})")
#                 else:
#                     st.warning("No papers found for this topic.")
#         else:
#             st.warning("Please enter a topic.")

# st.markdown("---")
# st.write("© 2024 Your Company Name. All rights reserved.")
