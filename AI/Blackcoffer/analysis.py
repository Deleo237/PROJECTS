import nltk
import re
nltk.download('punkt')

def content_analysis(text):
    stop_words = []  # Empty list to store stop words

    # List of stop words files
    stop_words_files = ['StopWords/StopWords_Auditor.txt', 'StopWords/StopWords_Currencies.txt', 'StopWords/StopWords_DatesandNumbers.txt', 'StopWords/StopWords_Generic.txt', 'StopWords/StopWords_GenericLong.txt', 'StopWords/StopWords_Geographic.txt', 'StopWords/StopWords_Names.txt']

    # Iterate over each stop words file
    for file_name in stop_words_files:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()  # Split contents into individual words
            stop_words.extend(words)  # Add words to the stop words list

    # Convert stop words to lowercase
    stop_words = [word.lower() for word in stop_words]
    
    # 1	Sentimental Analysis
    
        # Step 1: Clean the text using stop words

            # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)

            # Remove stop words from the tokens
    cleaned_tokens = [token for token in tokens if token.lower() not in stop_words]
    
        # Step 2: Create a dictionary of positive and negative words
    positive_words_path = "MasterDictionary/positive-words.txt"  # Path to the positive words file
    negative_words_path = "MasterDictionary/negative-words.txt"  # Path to the negative words file

    positive_words = set()
    negative_words = set()

            # Read positive words from the file
    with open(positive_words_path, "r") as file:
        for line in file:
            positive_words.add(line.strip())

            # Read negative words from the file
    with open(negative_words_path, "r") as file:
        for line in file:
            negative_words.add(line.strip())

        # Step 3: Extract derived variables
    positive_score = sum(1 for token in cleaned_tokens if token in positive_words)
    negative_score = sum(1 for token in cleaned_tokens if token in negative_words)
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_tokens) + 0.000001)


    # 2	Analysis of Readability
    
        # Step 1: Calculation of various variables
    total_sentences = nltk.sent_tokenize(text)
    total_words = nltk.word_tokenize(text)
    
    sentences = set(total_sentences)  # Set of unique sentences without repetition
    words = set(total_words)  # Set of unique words without repetition
    complex_words = [word for word in words if len(word) > 2 and syllable_count(word) > 2]
        
        # Step 2: Get length
    num_sentences = len(sentences)
    num_words = len(words)
    num_complex_words = len(complex_words)
    
        # Step 3: Extract derived variables
    avg_sentence_length = num_words / num_sentences
    percentage_complex_words = (num_complex_words / num_words)
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # 3	Average Number of Words Per Sentence
    avg_words_per_sentence = len(total_words) / len(total_sentences)
    
    # 4	Complex Word Count
    num_complex_words = len(complex_words)
    
    # 5	Word Count
        # Remove symbols like "?", ",", ".", "!" from the text
    cleaned_text = re.sub(r'[?,.!]', '', text)
    
        # Calculate word count
    cleaned_words = [word for word in nltk.word_tokenize(cleaned_text) if word.lower() not in stop_words]
    num_words = len(cleaned_words)

    # 6	Syllable Count Per Word
    syllable_count_per_word = sum([syllable_count(word) for word in cleaned_words])
    
    
    # 7	Personal Pronouns
    personal_pronouns = ['I', 'we', 'my', 'ours', 'us']
    personal_pronouns_count = sum(1 for word in nltk.word_tokenize(text) if word.lower() in personal_pronouns)

    # 8	Average Word Length
    total_word_length = sum(len(word) for word in cleaned_words)
    avg_word_length = total_word_length / num_words
    
    # Print the derived variables
    print("Positive Score:", positive_score)
    print("Negative Score:", negative_score)
    print("Polarity Score:", polarity_score)
    print("Subjectivity Score:", subjectivity_score)
    print("Average Sentence Length:", avg_sentence_length)
    print("Percentage of Complex Words:", percentage_complex_words)
    print("Fog Index:", fog_index)
    print("Average Number of Words Per Sentence:", avg_words_per_sentence)
    print("Complex Word Count:", num_complex_words)
    print("Word Count:", num_words)
    print("Syllable Count Per Word:", syllable_count_per_word)
    print("Personal Pronouns Count:", personal_pronouns_count)
    print("Average Word Length:", avg_word_length)
    
    alldata =[positive_score,
            negative_score,
            polarity_score,
            subjectivity_score,
            avg_sentence_length,
            percentage_complex_words,
            fog_index,
            avg_words_per_sentence,
            num_complex_words,
            num_words,
            syllable_count_per_word,
            personal_pronouns_count,
            avg_word_length]
    
    print('Collected Data')
    return alldata

    
def syllable_count(word):
    word = word.lower()
    if len(word) <= 2:
        return 1
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("ed"):
        count -= 1
    if word.endswith("es"):
        count -= 1
    if count == 0:
        count += 1
    return count