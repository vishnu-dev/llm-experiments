import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def get_top_tags(description, top_n=5):
    # Process the description using spaCy
    doc = nlp(description)
    
    # Extract nouns and proper nouns as potential tags
    tags = [token.text.lower() for token in doc if token.pos_ in ("NOUN", "PROPN")]
    
    # Count the frequency of each tag
    tag_freq = Counter(tags)
    
    # Get the top 'n' tags based on frequency
    top_tags = [tag for tag, _ in tag_freq.most_common(top_n)]
    
    return top_tags


def test():
    text = "The image depicts a narrow street in Barcelona, Spain. The street is flanked by tall buildings with yellow and beige facades, some of which have balconies. A few cars are parked along the street, and people can be seen walking on the sidewalks. The sky above is clear blue with scattered clouds."

    print(get_top_tags(text))


if __name__ == "__main__":
    test()