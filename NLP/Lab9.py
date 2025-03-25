# Student Name:   Onur Onel
# Student No:     0865803
# Trent Email:    onuronel@trentu.ca
# Date:           18.03.2025
# Lab 9:          Natural Language Processing

# Natural Language Processing lets computers understand and work with human language.
# The NLTK library makes many NLP tasks easier in Python. For example,
# NLTK provides access to large collections of texts, like the Gutenberg corpus,
# which includes classic literature such as Shakespeare's Macbeth.
# One basic NLP step is tokenization—breaking a long text into smaller pieces (usually words).
# Once tokenized, we can count how often each word appears using frequency analysis.

import string
import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords

# Load Macbeth text from Gutenberg corpus
macbeth_raw_text = gutenberg.raw('shakespeare-macbeth.txt')

# Tokenize the Macbeth text
tokens = nltk.word_tokenize(macbeth_raw_text)

# Custom stopwords specific to Macbeth such as contractions, names, stage directions.
custom_stops = { 
    "'d", "'s", "vs", "enter", "exeunt", "exit", "scene", "act", 
    "macb", "macd", "rosse", "banquo", "haue", "vpon"
}

# Combine standard English stopwords with custom stopwords
all_stops = set(stopwords.words("english")).union(custom_stops)

# Filter out stopwords and punctuation
filtered_words = [
    word for word in tokens if word.lower() not in all_stops and word not in string.punctuation
]

# Compute word frequency distribution
freq_dist = nltk.FreqDist(filtered_words)

# Get the 15 most common words
most_common_15 = freq_dist.most_common(15)

# Print results
print("\nMost common words in Macbeth:")
for word, count in most_common_15:
    print(word + ": " + str(count))

