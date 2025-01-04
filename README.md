# Code for comparing synthetic Amazon reviews to actual reviews
The python files are for performing statistical analysis on a dataset of synthetic Amazon reviews, and comparing these to actual Amazon reviews.
1) reviews_grammar_check.py first uses LanguageTool to grammar edit the synthetic reviews, then it calculates sentiment scores for synthetic
   reviews using Vader Sentiment Analysis.
2) sentiment_analysis_actual_data.py performs calculations with Vader Sentiment Analysis for the actual reviews.
3) t_test.py performs a t-test using NumPy and SciPy.
