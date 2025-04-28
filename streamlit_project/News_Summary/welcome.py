# import module
import streamlit as st
import utils

# Initialize session state to store the summary
if 'companyname' not in st.session_state:
    st.session_state.companyname = ""
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'title' not in st.session_state:
    st.session_state.title = ""
if 'url' not in st.session_state:
    st.session_state.url = ""
if 'summarized' not in st.session_state:
    st.session_state.summarized = False


summary = None
#st.set_page_config(page_title="News Article Summarizer", page_icon=":newspaper:", layout="wide")
st.title("News Article Summarizer")
st.header("Get brief summary of news articles related to a company")
st.markdown("Enter the name of the company to get the news articles related to it")

# Text input for company name  
company_name = st.text_input("Company Name")

# Button to get news articles 
if st.button("Get News Summary"):
    if company_name:
        st.session_state.companyname = company_name
        with st.spinner("Summarizing news article..."):
            url,title,summary = utils.get_news_url(st.session_state.companyname)

            st.session_state.summary = summary
            st.session_state.title = title
            st.session_state.url = url
            st.session_state.summarized = True
            
    
    else:
        st.error("Please enter a company name to get news articles.")



html_str = f"""
        <style>
        p.a {{
        font: bold 15px Arial, sans-serif;
        }}
        </style>
        <p class="a">{st.session_state.title}</p>
        """
st.html(html_str)

if st.session_state.summarized:
    if st.session_state.summary != None :

        left_column, right_column = st.columns(2)
        st.write(st.session_state.summary)

        left_column.download_button(
                    label="Download Summary",
                    data=st.session_state.summary,
                    file_name="summary.txt",
                    mime="text/plain",
                    #on_click=set_summary,
                    #args=(summary,),
                    help="Click to download the summary",
                    icon=":material/download:"
                )
        right_column.link_button("Click here to view the full article", st.session_state.url)

# Add some helpful information in the sidebar
with st.sidebar:
    st.header("About")
    st.info("""
    This app summarizes news articles about a given company using NLP techniques.
    
    1. Mention the name of the company in the text box.
    2. Click 'Get News Summary'
    3. Download the summary if desired
    """)



