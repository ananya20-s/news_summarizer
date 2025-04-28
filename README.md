## News Summarizer using pretrained BART




The aim of this exercise is to build a web based interface where user can provide a company name and receive a summary of news articles related to that company.

**Approach:**

	- Build a simple Streamlit based front end interface to accept the company name
	- Fetch list of news articles using NewsData API
	- Fetch the content of the first article using NewsPaper3k
	- Use a pretrained BART to summarise the content
	- Display the summary on the user interface
	- Include options to download the summary or view the full article
	
**Results:**

	- Designed a Streamlit front end with session state handling
	- Loaded pretrained BART from Hugging Face for generating the summary
	
	
**Tools and Technologies:**

	Streamlit, NewsData API, Newspaper3k, Hugging Face Transformers, BART
	
**Setup:**

	- Use the requirements.txt to setup a virtual environment
	- Run streamlit run welcome.py to start the application
	
**Next steps:**

	- Display the list of possible articles so that user can choose which article to Summarizer
	- Separate the summarization into FastAPI interface
	- Use Docker Compose for deployment