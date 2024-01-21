from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
prompt = ''
generated_answer = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    global generated_answer
    global prompt
    if request.method == 'POST':
        import os
        from openai import OpenAI
        import pandas as pd
        import spacy
        from sklearn.model_selection import train_test_split
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.naive_bayes import MultinomialNB

    api_key = os.environ.get("OPENAI_API_KEY")

    if api_key is None:
        print("API key is not set. Please set the OPENAI_API_KEY environment variable.")
    else:
        client = OpenAI(api_key=api_key)


    def is_valid_prompt(prompt):

       
        df = pd.read_csv("response.csv")

       
        nlp = spacy.load("en_core_web_lg")

        
        def tokenize_entities(text):
            doc = nlp(text)
            return [ent.text.lower() for ent in doc.ents]

        
        df['Tokenized_Entities'] = df['Stories'].apply(tokenize_entities)

        train_df = train_test_split(df, test_size=0.2, random_state=42)

        
        vectorizer = CountVectorizer()
        X_train = vectorizer.fit_transform(train_df['Tokenized_Entities'].apply(lambda x: ' '.join(x)))
        y_train = train_df['Label']

        
        classifier = MultinomialNB()
        classifier.fit(X_train, y_train)

        user_entities = tokenize_entities(prompt)

        X_user_story = vectorizer.transform([' '.join(user_entities)])

        user_prediction = classifier.predict(X_user_story)
            
        if user_prediction == "Yes":

            return True;
        else:

            return False;


        def is_valid_response(response):

            mythology_keywords = [
            "Ramayana", "Mahabharata", "Hindu mythology", "Indian gods", "Mythological creatures", 
            "Epics of India", "Vedas", "Puranas", "Upanishads", "Bhagavad Gita", 
            "Krishna", "Rama", "Vishnu", "Shiva", "Ganesha", "Lakshmi", "Saraswati", "Hanuman", 
            "Kali", "Durga", "Parvati", "Brahma", "Indra", "Varuna", "Agni", "Yama", "Surya", 
            "Chandra", "Navagrahas", "Asuras", "Devas", "Rakshasas", "Yakshas", "Gandharvas", 
            "Kinnaras", "Nagas", "Garuda", "Vamana", "Narasimha", "Kurma", "Matsya", "Dhanvantari", 
            "Vedavyasa", "Manu", "Mandodari", "Kubera", "Ahalya", "Shakuntala", "Sita", "Draupadi", 
            "Arjuna", "Bhima", "Yudhishthira", "Nakula", "Sahadeva", "Karna", "Duryodhana", 
            "Dhritarashtra", "Pandavas", "Kauravas", "Kamadeva", "Rati", "Apsaras", "Narada", 
            "Valmiki", "Vyasa", "Markandeya", "Agastya", "Vashishta", "Chyavana", "Bharadwaja", 
            "Durvasa", "Sage Kashyapa", "Ashtavakra", "Maitreya", "Yajnavalkya", "Shukracharya", 
            "Brihaspati", "Shabala", "Suryavansha", "Chandravansha", "Kuru Dynasty", "Ikshvaku Dynasty", 
            "Raghuvansha", "Ayodhya", "Dandaka Forest", "Lanka", "Kishkindha", "Hampi", "Panchavati", 
            "Mount Kailash", "Yamunotri", "Gangotri", "Kedarnath", "Badrinath", "Chardham Yatra", 
            "Ganga", "Yamuna", "Sarasvati", "Sarayu", "Godavari", "Krishna River", "Yamuna River", 
            "Indus River", "Sarasvati River", "Ganges River"]

            
            story_phrases = [
                "for kids", "children's story", "kids tale", "kid-friendly", "childhood tale",
                "bedtime story", "young audience", "storybook","story","tale"
            ]

            
            keywords_present = any(keyword.lower() in response.lower() for keyword in mythology_keywords)

            story_present = any(phrase.lower() in response.lower() for phrase in story_phrases)

            if keywords_present and story_present:
                return True
            else:
                return False

        user_input = input("Enter your prompt: ")
        user_updated_input = "Generate a story about " + user_input + " if it is related to Indian Mythology or Indian Folklore in under 100 words"

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_updated_input,
                },
                {
                    "role": "assistant",
                    "content": "Provide a story with the title keep it limited to 100 words and also generate a moral for the story.",
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=500  
        )


        generated_answer = chat_completion.choices[0].message.content


        if is_valid_response(generated_answer) and is_valid_prompt(user_input):
            print(generated_answer)
        else:
            print("The generated response is not related to Indian mythological stories, history, or folklore.")
        return render_template('prompt.html', prompt=prompt, generated_answer=generated_answer  )
    return render_template('index.html')

@app.route('/prompt', methods=['GET', 'POST'])
def display():
    global generated_answer
    global prompt
    if request.method == 'POST':
        
        return render_template('prompt.html', prompt=prompt, generated_answer=generated_answer)
    return render_template('prompt.html', prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True)
