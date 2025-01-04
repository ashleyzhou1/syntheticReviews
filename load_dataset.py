import json
import os
from datasets import load_dataset

'''
# Load the dataset
dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023")

# Define the output directory
output_dir = "/Users/ashleyzhou/Desktop/amazon_reviews"
os.makedirs(output_dir, exist_ok=True)

# Save the entire dataset to a single JSON file
output_file_path = os.path.join(output_dir, "dataset.json")

with open(output_file_path, "w") as f:
    for split in dataset.keys():
        split_data = dataset[split]
        for entry in split_data:
            json.dump(entry, f)
            f.write("\n")  # Write each review on a new line

print(f"Saved entire dataset to {output_file_path}")
'''


from datasets import load_dataset

#dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Appliances", trust_remote_code=True)
#print(dataset["full"][2128604])

dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_Toys_and_Games", trust_remote_code=True)
print(dataset["full"][2])



'''
def load_reviews(category):
    # Load the dataset
    dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", category)

    # Define the absolute output directory path
    output_dir = "/Users/ashleyzhou/Desktop/amazon_reviews"
    os.makedirs(output_dir, exist_ok=True)

    # Save each split as a separate JSON file
    for split in dataset.keys():
        split_data = dataset[split]
        json_file_path = os.path.join(output_dir, f"{split}.json")

        with open(json_file_path, "w") as f:
            for entry in split_data:
                json.dump(entry, f)
                f.write("\n")  # Write each review on a new line

        print(f"Saved {split} to {json_file_path}")

#load_reviews('raw_review_All_Beauty')
load_reviews('raw_review_CDs_and_Vinyl')
'''

'''
with open('/Users/ashleyzhou/Desktop/review_categories.txt', 'r') as file:
    for line in file:
        load_reviews('raw_review_All_Beauty')
'''