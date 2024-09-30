<h1 align="center"> LLM Document Assistant </h1> <p align="center"> <img src="https://static.vecteezy.com/system/resources/thumbnails/010/214/734/small_2x/llm-letter-technology-logo-design-on-white-background-llm-creative-initials-letter-it-logo-concept-llm-letter-design-vector.jpg" alt="Logo" width="200"/> </p>
LLM Document Assistant is designed to efficiently handle document processing and querying, providing accurate results by leveraging powerful Language Learning Models (LLMs). It integrates document uploading, parsing, and response generation using OpenAI's models, offering both ease of use and detailed insights.

# Project Title

A brief description of what this project does and who it's for

![img](https://res.cloudinary.com/dzcqq0wvy/image/upload/v1727685081/Screenshot_2024-09-30_021447_ctqetl.png)

![img](https://res.cloudinary.com/dzcqq0wvy/image/upload/v1727685081/Screenshot_2024-09-30_135613_rfv19l.png)

## Features

- Upload PDFs: Users can upload PDF documents and store them for future reference.
- Document Management: Users can view and delete previously uploaded documentsFul.
- Ask Questions: The app allows users to ask questions related to uploaded PDFs.
- Search research articles: Users can search for recent research papers on arXiv by topic and download summaries.

## Installation

**1.Clone the Repository:**

```bash
git clone https://github.com/Dip24pal/Docuchat.git
cd Docuchat
```
**2.Install the Dependencies: Make sure you have Docker installed, then run the following:**
```bash
docker build -t pathway-llm .
docker run -p 8501:8501 pathway-llm
```
**Alternatively, you can use pip to install dependencies:**
```bash
pip install -r requirements.txt
```
**3.Run the Application: You can start the app by running the following:**
```bash
streamlit run app.py
```
**If you're using Docker:**
```bash
docker-compose up
```
## Usage

**Upload Documents:**Use the sidebar to navigate to the "Upload Documents" section. Select one or more PDF files and upload them. Uploaded files are stored in the /app/data directory.
![upload](https://res.cloudinary.com/dzcqq0wvy/image/upload/v1727691653/ezgif-5-e1f5ef3309_eb4y6e.gif)

**Manage Documents:** In the "Manage Documents" section, you can view all uploaded PDFs and delete them as needed.

**Ask Questions:**
- Go to the "Ask Questions" section.
- Select an uploaded PDF and type in your question.
- The application will send the document and question to the backend for processing, and the LLM will generate a response based on the document content.

![ask](https://res.cloudinary.com/dzcqq0wvy/image/upload/v1727691800/ezgif-5-5d3d8fe7d0_zqogz0.gif)

**Search search articles:** Enter a topic in the "Search research articles" section and specify the maximum number of results.
The application will retrieve and display recent research papers from arXiv based on the specified topic.

![search](https://res.cloudinary.com/dzcqq0wvy/image/upload/v1727691994/ezgif-5-ac363c21f6_gx1kwq.gif)

## Contributing

Contributions are always welcome!

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Commit your changes (git commit -am 'Add new feature').

4. Push to the branch (git push origin feature-branch).

5. Open a pull request.

```markdown
  pathway-llm-interface/
│
├── app.py                   # Main Streamlit app
├── arxiv_search.py           # Module for handling arXiv searches and generating PDFs
├── data_uploader.py          # Module for uploading and saving PDFs
├── config.yaml               # Configuration file for LLM model and host settings
├── Dockerfile                # Docker configuration for running the app
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```
## API Reference

#### The Application Interacts with two backend APIs:

**1. LLM API for Document QA:**
- **Endpoint:** /v1/pw_ai_answer
- **Method:** POST
- **Requestbody:**


```json
{
  "prompt": "Your question here",
  "document": "document_name.pdf"
}
```
**arXiv Search API:**

- Fetches research papers from arXiv based on the user's input.
- The search is implemented using the feedparser library, parsing arXiv’s Atom feeds.

## Project Structure

```bash
  pathway-llm-interface/
│
├── app.py                   # Main Streamlit app
├── arxiv_search.py           # Module for handling arXiv searches and generating PDFs
├── data_uploader.py          # Module for uploading and saving PDFs
├── config.yaml               # Configuration file for LLM model and host settings
├── Dockerfile                # Docker configuration for running the app
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

```
- app.py: The main file for the Streamlit frontend interface.
- arxiv_search.py: Contains the logic to search arXiv and save search results to a file.
- data_uploader.py: Handles file uploading and storage.
- config.yaml: Holds configuration options for the LLM and caching settings.
- Dockerfile: Docker container configuration for setting up the environment and running the app.

# Improvements

### Improvements and Enhancements

- **Preprocessing PDFs:** Improve the text extraction process to better handle complex PDFs with images, tables, or non-standard fonts.
- **Document Chunking:** For long documents, implement a chunking mechanism to send only relevant sections to the LLM.
- **Caching:** Add caching for repeated questions or frequent document queries to reduce response time.
- **Fine-tuning LLM:** Consider fine-tuning the LLM on your specific dataset for more accurate and domain-specific answers.
- **Security:** Add authentication for document access and usage, especially for sensitive files.