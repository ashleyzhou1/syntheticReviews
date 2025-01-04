import subprocess
import os
import random
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def count_lines_in_file(file_path):
    result = subprocess.run(['wc', '-l', file_path], capture_output=True, text=True)
    return int(result.stdout.split()[0])

#takes the directory, for each file it random selects a specified number of reviews
# and finds the average compound difference between the title and text (title-text)
def count_lines_in_files(directory, number):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):

            line_count = count_lines_in_file(file_path)
            if file_path=='/Users/ashleyzhou/Desktop/amazon_reviews/.DS_Store':
                continue
            #print("line count is: "+str(line_count)+"\n")
            sum = 0
            for i in range(1,number):
                line_num = random.randint(0, line_count-1)
                #print("line num is: "+str(line_num)+"\n")
                line = get_line_from_file(file_path, line_num)
                review = json.loads(line)
                title = review.get('title', 'No title')
                text = review.get('text', 'No text')
                title_score = get_positivity_score(title)
                text_score = get_positivity_score(text)
                diff = title_score-text_score
                sum+=diff
            average = (sum)/number
            print(average)
                #calculate sentiment scores for whatever line it is

def get_positivity_score(statement):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(statement)
    return score['compound']

def get_line_from_file(file_path, line_number):
    # Construct the `sed` command to extract the specific line
    command = ['sed', '-n', f'{line_number}p', file_path]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Return the output, which will be the desired line
        return result.stdout.strip()  # Strip to remove any trailing newlines
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

def get_line_from_file(file_path, line_number):
    # Construct the `sed` command to extract the specific line
    command = ['sed', '-n', f'{line_number}p', file_path]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Return the output, which will be the desired line
        return result.stdout.strip()  # Strip to remove any trailing newlines
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None
    
#print(get_line_from_file('/Users/ashleyzhou/Desktop/amazon_reviews/Amazon_Fashion.jsonl', 2500930))

#count_lines_in_file('/Users/ashleyzhou/Desktop/amazon_reviews/All_Beauty.jsonl')

directory = '/Users/ashleyzhou/Desktop/amazon_reviews'
count_lines_in_files(directory, 100)
'''
line_counts = count_lines_in_files(directory)
for filename, count in line_counts.items():
    print(f"{filename}: {count} lines")
'''