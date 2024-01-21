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
        prompt = request.form['prompt']
        print(f"Received prompt: {prompt}")
        client = OpenAI(api_key="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")
        user_input = "Generate a story about " + prompt + " if it is directly or indirectly related to Indian Mythology,Indian Folklore,ancient Indian collection of interrelated animal fables , folk tales,vedas , puranas , upanishads or ancient Indian collection of stories in under 100 words. If the entered promt does not belong to Indian Mythology or Indian Folklore,tell me that the entered prompt is not related to Indian Mythology or Indian Folklore. "
        chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "assistant",
            "content": "You are a helpful assistant that specializes in Indian mythological stories,indian folklore,indian animal fable tales,puranas,upanishads.",
        },
        {
            "role": "user",
            "content": user_input,
        },
        {
            "role": "assistant",
            "content": "",
        }],
        model="gpt-3.5-turbo",
        max_tokens=1000 )
        generated_answer = chat_completion.choices[0].message.content
        print(f"Prompt: {prompt}")
        print(f"Generated Answer: {generated_answer}")
        return render_template('prompt.html', prompt=prompt, generated_answer=generated_answer  )
    return render_template('index.html')

@app.route('/prompt', methods=['GET', 'POST'])
def display():
    global generated_answer
    global prompt
    if request.method == 'POST':
        print(request.method)
        import os
        from openai import OpenAI
        prompt = request.form['prompt']
        print(f"Received prompt: {prompt}")
        client = OpenAI(api_key="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")
        user_input = "Generate a story about " + prompt + " if it is directly or indirectly related to Indian Mythology,Indian Folklore,ancient Indian collection of interrelated animal fables, folk tales,ancient Indian collection of stories or indian epics in under 100 words. If the entered promt does not belong to Indian Mythology or Indian Folklore,tell me that the entered prompt is not related to Indian Mythology or Indian Folklore. "
        chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "assistant",
            "content": "You are a helpful assistant that specializes in Indian mythological stories based on Indian history, folklore,epics and tales.",
        },
        {
            "role": "user",
            "content": user_input,
        },
        {
            "role": "assistant",
            "content": "",
        }],
        model="gpt-3.5-turbo",
        max_tokens=1000 )
        generated_answer = chat_completion.choices[0].message.content
        print(f"Prompt: {prompt}")
        print(f"Generated Answer: {generated_answer}")
        return render_template('prompt.html', prompt=prompt, generated_answer=generated_answer)
    return render_template('prompt.html', prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True)
