import json
import language_tool_python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

tool = language_tool_python.LanguageTool('en-US')
reviews = [];
corrected_reviews = [];
#sums of sentiment scores

def grammar_check(title_text):
    matches = tool.check(title_text)
    if len(matches)!=0:
        print(matches)
        print("\n")
        with open('/Users/ashleyzhou/Desktop/matches.txt', 'a') as text_file:
            for match in matches:
             text_file.write(match)
    corrected_title_text = language_tool_python.utils.correct(title_text, matches) 
    corrected_reviews.append(corrected_title_text)    
'''
'''
#function opens text file and adds difference of each score between title and text
#for each review. 
def open_file(file_name):
    neg_sum = 0
    neu_sum = 0
    pos_sum = 0
    compound_sum = 0
    with open(file_name, 'r') as file:#title minus text
        for line in file:
            review = json.loads(line)
            title = review['title']
            text = review['text']
            title_neg, title_neu, title_pos, title_compound = get_positivity_score(title)
            text_neg, text_neu, text_pos, text_compound = get_positivity_score(text)
            #get differences in the score
            #add to existing sum of differences, want to find avg
            neg_diff = title_neg-text_neg 
            neg_sum+=neg_diff
            neu_diff = title_neu-text_neu
            neu_sum+=neu_diff
            pos_diff = title_pos-text_pos
            pos_sum+=pos_diff
            compound_diff = title_compound-text_compound
            compound_sum+=compound_diff
        print(neg_sum, neu_sum, pos_sum, compound_sum)

def get_positivity_score(statement):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(statement)
    return score['neg'], score['neu'], score['pos'], score['compound']

open_file('/Users/ashleyzhou/Desktop/amazon_reviews/All_Beauty.jsonl')

for i in range(1,11):
    file_name = '/Users/ashleyzhou/Desktop/syntheticData/100syndata'+str(i)+'.jsonl'
    
    #the numbers printed are the average difference of scores in each file 
    #neg, neu, pos, compound
print("\n\n")
for i in range(1,11):
    file_name = '/Users/ashleyzhou/Desktop/syntheticData/500syndata'+str(i)+'.jsonl'
    
print("\n\n")
for i in range(1,11):
    file_name = '/Users/ashleyzhou/Desktop/syntheticData/1000syndata'+str(i)+'.jsonl'
   
'''
with open('/Users/ashleyzhou/Desktop/corrected_reviews.txt', 'w') as text_file:
    for corrected_review in corrected_reviews:
        text_file.write(corrected_review+"\n\n")

with open('/Users/ashleyzhou/Desktop/orig_reviews.txt', 'w') as text_file:
    for review in reviews:
        text_file.write(review+"\n\n")
'''
   