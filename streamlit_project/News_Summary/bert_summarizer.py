import transformers

from transformers import pipeline

import torch

def get_summary(text):
    """
    Summarizes the input text using a pre-trained BART model.
    
    Args:
        text (str): The text to summarize.
        
    Returns:
        str: The summarized text.
    """
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available, otherwise CPU
    
    # Load the summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn",device=device)
    
    # Generate the summary
    summary = summarizer(text[:3500], max_length=130, min_length=30, do_sample=False)
    
    # Return the summarized text
    return summary[0]['summary_text']