# Keyword Parser for CHI Conference Research

A Python script to analyze keyword trends in the *CHI Conference on Human Factors in Computing Systems* (HCI research). The tool extracts and ranks frequently used terms from paper metadata to identify emerging trends in Human-Computer Interaction.

- **Data Source**: Scopus (max sample size: 5,000 records)  
- **Output**: Ranked lists of top author-keywords and index-keywords.

Output suggests an emerging trend of incorporating large language models and related artificial intelligence technology into accessbility research.

## Features
- Parses author keywords and index keywords from Scopus CSV exports.
- Generates a sorted frequency count of terms.
- Outputs top 40 keywords for analysis. Able to change number depending on usage.

## Top Keywords

### Author Keywords
| Keyword                  | Frequency |
|--------------------------|-----------|
| virtual reality          | 329       |
| accessibility            | 180       |
| augmented reality        | 174       |
| generative AI            | 143       |
| large language models    | 138       |


### Index Keywords
| Keyword                  | Frequency |
|--------------------------|-----------|
| human engineering        | 461       |
| user interfaces          | 393       |
| virtual reality          | 376       |
| language model           | 349       |

## Full Output 

### Author Keywords
[('virtual reality', 329), ('accessibility', 180), ('augmented reality', 174), ('', 152), ('generative ai', 143), ('large language models', 138), ('artificial intelligence', 113), ('user experience', 105), ('human-ai interaction', 104), ('social media', 100), ('privacy', 92), ('design', 91), ('mixed reality', 87), ('participatory design', 85), ('human-computer interaction', 75), ('older adults', 75), ('human-ai collaboration', 74), ('machine learning', 71), ('visualization', 70), ('interaction design', 69), ('co-design', 68), ('sustainability', 61), ('mental health', 57), ('children', 57), ('collaboration', 57), ('ai', 54), ('haptics', 53), ('trust', 52), ('large language model', 51), ('explainable ai', 47), ('hci', 46), ('ethics', 45), ('chatbot', 44), ('human-robot interaction', 43), ('reflection', 40), ('education', 40), ('health', 40), ('covid-19', 39), ('llm', 38), ('misinformation', 38)]

### Index Keywords
[('human engineering', 461), ('user interfaces', 393), ('virtual reality', 376), ('language model', 349), ('human computer interaction', 265), ('large language model', 230), ('visualization', 224), ("users' experiences", 220), ('user study', 206), ("'current", 206), ('students', 194), ('mixed reality', 185), ('accessibility', 178), ('social media', 170), ('design', 167), ('augmented reality', 163), ('behavioral research', 155), ('decision making', 154), ('user centered design', 151), ('case-studies', 149), ('data visualization', 146), ('haptics', 144), ('social networking (online)', 135), ('generative ai', 134), ('teaching', 129), ('creatives', 125), ('co-designs', 125), ('decisions makings', 124), ('machine-learning', 124), ('interaction design', 122), ('computer interaction', 121), ('performance', 121), ('interactive computer graphics', 113), ('immersive', 112), ('chatbots', 107), ('participatory design', 107), ('well being', 105), ('game design', 105), ('engineering education', 103), ('smart phones', 99)]
