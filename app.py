import streamlit as st
import re

# Set page configuration
st.set_page_config(
    page_title="Text Analyzer",
    page_icon="📝",
    layout="wide",
)

# Custom CSS for a professional look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
        color: #212529;
    }
    .stTextInput, .stTextArea {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
    }
    .highlight {
        color: #0d6efd;
        font-weight: bold;
    }
    .title {
        color: #212529;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .subtitle {
        color: #495057;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .result {
        background-color: #ffffff;
        padding: 1.25rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
        box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    }
    .emoji-header {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #ffffff;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0d6efd;
        color: white;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #0d6efd;
    }
    .metric-label {
        font-size: 1rem;
        color: #6c757d;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #f8f9fa;
        border-top: 1px solid #dee2e6;
        margin-top: 2rem;
    }
    /* Chart colors */
    .st-emotion-cache-1lb4qcp {
        background-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown('<div class="title">📊 Text Analyzer</div>', unsafe_allow_html=True)
st.markdown("""
This professional application analyzes your text and provides various insights and transformations.
Enter a paragraph below to get started! ✨
""")

# User input section
st.markdown('<div class="subtitle">📝 Enter Your Text</div>', unsafe_allow_html=True)
user_text = st.text_area("Type or paste your paragraph here:", height=150, 
                         placeholder="Enter your text here for analysis...")

# Validate input
if user_text.strip() == "":
    st.warning("⚠️ Please enter some text to analyze!")
else:
    # Create tabs for different analysis sections
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Basic Analysis", "🔍 Search & Replace", "🔄 Text Transformations", "📈 Advanced Metrics"])
    
    with tab1:
        st.markdown('<div class="subtitle">📊 Basic Text Analysis</div>', unsafe_allow_html=True)
        
        # Word count
        words = re.findall(r'\b\w+\b', user_text)
        word_count = len(words)
        word_count_str = str(word_count)  # Type casting to string
        
        # Character count
        char_count = len(user_text)
        char_count_str = str(char_count)  # Type casting to string
        
        # Vowel count
        vowels = re.findall(r'[aeiouAEIOU]', user_text)
        vowel_count = len(vowels)
        vowel_count_str = str(vowel_count)  # Type casting to string
        
        # Display results in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">🔤</span> <b>Word Count</b>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-value">{word_count_str}</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Total words in text</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">📏</span> <b>Character Count</b>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-value">{char_count_str}</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Total characters in text</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col3:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">🔠</span> <b>Vowel Count</b>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-value">{vowel_count_str}</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Total vowels in text</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Check if the text contains "Python" using comparison operator
        contains_python = "Python" in user_text
        
        st.markdown('<div class="result">', unsafe_allow_html=True)
        if contains_python:  # Using if statement (Python keyword)
            st.markdown(f'<span class="emoji-header">✅</span> <b>Python Check</b>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">The text contains the word "Python"</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<span class="emoji-header">❌</span> <b>Python Check</b>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">The text does not contain the word "Python"</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="subtitle">🔍 Search and Replace</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            search_word = st.text_input("Enter a word to search for:", placeholder="Search term...")
        with col2:
            replace_word = st.text_input("Enter a word to replace it with:", placeholder="Replacement term...")
        
        if search_word:
            # Perform search and replace
            modified_text = user_text.replace(search_word, replace_word)
            
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">📝</span> <b>Original Text</b>', unsafe_allow_html=True)
            st.write(user_text)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">✏️</span> <b>Modified Text</b>', unsafe_allow_html=True)
            st.write(modified_text)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Count occurrences
            occurrences = user_text.lower().count(search_word.lower())
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">🔢</span> <b>Occurrences</b>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-value">{occurrences}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-label">Found "{search_word}" {occurrences} times in the text</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="subtitle">🔄 Text Transformations</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">⬆️</span> <b>Uppercase</b>', unsafe_allow_html=True)
            st.write(user_text.upper())
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">⬇️</span> <b>Lowercase</b>', unsafe_allow_html=True)
            st.write(user_text.lower())
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional transformations
        st.markdown('<div class="result">', unsafe_allow_html=True)
        st.markdown(f'<span class="emoji-header">🔠</span> <b>Title Case</b>', unsafe_allow_html=True)
        st.write(user_text.title())
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="result">', unsafe_allow_html=True)
        st.markdown(f'<span class="emoji-header">🔄</span> <b>Reversed Text</b>', unsafe_allow_html=True)
        st.write(user_text[::-1])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="subtitle">📈 Advanced Metrics</div>', unsafe_allow_html=True)
        
        # Calculate average word length using arithmetic operators
        if word_count > 0:
            # Remove spaces for accurate character count in words
            text_without_spaces = ''.join(words)
            # Calculate average word length (total characters without spaces / total words)
            avg_word_length = len(text_without_spaces) / word_count
            avg_word_length_formatted = f"{avg_word_length:.2f}"
        else:
            avg_word_length_formatted = "0.00"
        
        # Word frequency analysis
        word_freq = {}
        for word in words:
            word_lower = word.lower()
            if word_lower in word_freq:
                word_freq[word_lower] += 1
            else:
                word_freq[word_lower] = 1
        
        # Sort by frequency
        sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">📏</span> <b>Average Word Length</b>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-value">{avg_word_length_formatted}</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Average characters per word</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="result">', unsafe_allow_html=True)
            st.markdown(f'<span class="emoji-header">📃</span> <b>Sentence Count</b>', unsafe_allow_html=True)
            sentences = re.split(r'[.!?]+', user_text)
            sentence_count = len([s for s in sentences if s.strip()])
            st.markdown(f'<div class="metric-value">{sentence_count}</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Total sentences in text</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Word frequency chart
        st.markdown('<div class="result">', unsafe_allow_html=True)
        st.markdown(f'<span class="emoji-header">📊</span> <b>Word Frequency Analysis</b>', unsafe_allow_html=True)
        
        # Get top 10 words
        top_words = list(sorted_word_freq.items())[:10]
        
        # Create a bar chart
        if top_words:
            import matplotlib.pyplot as plt
            import numpy as np
            
            words_list = [word for word, _ in top_words]
            counts = [count for _, count in top_words]
            
            fig, ax = plt.subplots(figsize=(10, 5))
            bars = ax.barh(words_list, counts, color='#0d6efd')
            ax.set_xlabel('Frequency')
            ax.set_ylabel('Words')
            ax.set_title('Top Word Frequencies')
            ax.set_facecolor('#ffffff')
            fig.set_facecolor('#ffffff')
            ax.tick_params(colors='#212529')
            ax.xaxis.label.set_color('#212529')
            ax.yaxis.label.set_color('#212529')
            ax.title.set_color('#212529')
            
            # Add count labels to bars
            for i, v in enumerate(counts):
                ax.text(v + 0.1, i, str(v), color='#212529', va='center')
            
            st.pyplot(fig)
        else:
            st.write("Not enough unique words for frequency analysis.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("📝 **Text Analyzer** - Created by Taha Shabbir")
st.markdown("Developed with ❤️ using Python and Streamlit")
st.markdown('</div>', unsafe_allow_html=True)