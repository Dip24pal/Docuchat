import urllib.parse
import feedparser
import json
import os
import time
from fpdf import FPDF
import urllib.request
import urllib.parse

def fetch_arxiv_papers(topic, max_results=50):
    """
    Fetch research papers from arXiv based on the given topic.

    Args:
        topic (str): The search topic for research papers.
        max_results (int): Maximum number of results to return.

    Returns:
        list: A list of dictionaries containing paper details.
    """
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'all:{urllib.parse.quote_plus(topic)}'
    query = f'search_query={search_query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'
    
    response = urllib.request.urlopen(base_url + query).read()
    feed = feedparser.parse(response)




    try:
        response = urllib.request.urlopen(base_url + query).read()
    except Exception as e:
        print(f"Error fetching data from arXiv: {e}")
        return []






    

    research_articles = []
    for entry in feed.entries:
        paper_details = {
            'arxiv_id': entry.id.split('/abs/')[-1],
            'published': entry.published,
            'title': entry.title,
            'summary': entry.summary
        }
        research_articles.append(paper_details)

    # Save results to /app/data
    save_path_jsonl = "/app/data/arxiv_results.jsonl"
    with open(save_path_jsonl, 'a', encoding='utf-8') as f:
        for article in research_articles:
            f.write(json.dumps(article, ensure_ascii=False) + '\n')

    # Save results to PDF
    timestamp = int(time.time())
    save_path_pdf = f"/app/data/arxiv_results_{timestamp}.pdf"
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for article in research_articles:
        pdf.multi_cell(0, 10, f"Title: {article['title']}\n"
                               f"arXiv ID: {article['arxiv_id']}\n"
                               f"Published: {article['published']}\n"
                               f"Summary: {article['summary']}\n\n")
    
    pdf.output(save_path_pdf)

    return research_articles
