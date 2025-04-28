import streamlit as st
from io import StringIO
import time

# Set page title and configuration
st.set_page_config(page_title="News Summarizer", layout="wide")
st.title("News Article Summarizer")

# Initialize session state to store the summary
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'article_text' not in st.session_state:
    st.session_state.article_text = ""
if 'summarized' not in st.session_state:
    st.session_state.summarized = False

# Function to generate summary (placeholder for Hugging Face integration)
def generate_summary(article_text):
    # In your actual app, replace this with your Hugging Face model code
    # Example:
    # from transformers import pipeline
    # summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # summary = summarizer(article_text, max_length=150, min_length=30, do_sample=False)
    # return summary[0]['summary_text']
    
    # For demonstration purposes, we'll just return a placeholder
    st.info("Processing with NLP model... (simulated)")
    time.sleep(2)  # Simulate processing time
    return f"This is a summary of the article that's {len(article_text)//10} words long. The article discusses important topics and provides insights on current events."

# Main input area
st.subheader("Input News Article")
text_input = st.text_area("Paste your article text here:", height=200)

# Add a file uploader as an alternative input method
uploaded_file = st.file_uploader("Or upload a text file:", type=['txt'])
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    text_input = stringio.read()
    st.text_area("Article content:", text_input, height=200)

# Generate summary button
if st.button("Generate Summary"):
    if text_input:
        st.session_state.article_text = text_input
        with st.spinner("Generating summary..."):
            summary = generate_summary(st.session_state.article_text)
            st.session_state.summary = summary
            st.session_state.summarized = True
    else:
        st.error("Please enter some text or upload a file first!")

# Display the summary section only if a summary exists
if st.session_state.summarized:
    st.subheader("Summary Results")
    st.markdown(st.session_state.summary)
    
    # Download button
    summary_text = st.session_state.summary
    st.download_button(
        label="Download Summary",
        data=summary_text,
        file_name="article_summary.txt",
        mime="text/plain"
    )

# Add some helpful information in the sidebar
with st.sidebar:
    st.header("About")
    st.info("""
    This app summarizes news articles using NLP techniques.
    
    1. Paste your article or upload a text file
    2. Click 'Generate Summary'
    3. Download the summary if desired
    """)
