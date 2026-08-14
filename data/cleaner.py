"""
Data cleaner module for Amazon reviews.

Functions to clean and normalize review text.
"""

import re

def remove_html(text):
    """remove HTML tags from text."""
    if not isinstance(text, str):
        return text
    #remove anthing between < and >
    return re.sub(r'<[^>]+>', '', text)

def remove_urls(text):
    """Remove URLs from text."""
    if not isinstance(text, str):
        return text
    # Remove http/https URLs
    text = re.sub(r'http[s]?://[^\s]+', '', text)
    # Remove www URLs
    text = re.sub(r'www\.[^\s]+', '', text)
    return text

def normalize_whitespace(text):
    """Normalize whitespace - remove extra spaces and newlines."""
    if not isinstance(text, str):
        return text
    # Replace multiple spaces/newlines with single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading and trailing whitespace
    return text.strip()

def clean_text(text):
    """Apply all cleaning steps to text."""
    if not isinstance(text, str):
        return text
    
    # Step 1: Remove HTML
    text = remove_html(text)
    
    # Step 2: Remove URLs
    text = remove_urls(text)
    
    # Step 3: Normalize whitespace
    text = normalize_whitespace(text)
    
    # Step 4: Lowercase
    text = text.lower()
    
    return text

def filter_by_length(text, min_length=20, max_length=5000):
    """Check if text meets length requirements."""
    if not isinstance(text, str):
        return False
    
    text_len = len(text)
    return min_length <= text_len <= max_length