import csv
from collections import defaultdict

FILENAME = "scopus.csv"
author_keywords = defaultdict(int)
index_keywords = defaultdict(int)

def main():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader: #Each row is 1 list of 1 link and  2 strings
            #split text by ;
            author_keywords_list = row[1].split(";")
            index_keywords_list = row[2].split(";")

            #preprocessing

            ##Did not account for hypens for now ##Could abstract this into a function next time
            for i in range(len(author_keywords_list)):
                author_keywords_list[i] = author_keywords_list[i].strip().lower()
            for i in range(len(index_keywords_list)):
                index_keywords_list[i] = index_keywords_list[i].strip().lower()

            #add to dictionary
            for keyword in author_keywords_list:
                author_keywords[keyword] += 1
            for keyword in index_keywords_list:
                index_keywords[keyword] += 1

        print(sorted(author_keywords.items(), key = lambda x : x[1], reverse=True)[:40])
        print(sorted(index_keywords.items(), key = lambda x : x[1], reverse=True)[:40])

if __name__ == "__main__":
    main()