# Indian Mythology Story Generator

## Getting Started

To run the application, you need to have Python 3 and pip installed on your system. Once you have those, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/AkshayGMys/StoryGenerationAI
    ```

2. Navigate to the project directory:
    ```bash
    cd StoryGenerationAI
    ```

3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # on Linux/macOS
    venv\Scripts\activate      # on Windows
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Obtain an API key from OpenAI and save it in a file named `.env` in the project directory with the following content:
    ```
    OPENAI_API_KEY=your_api_key_here
    ```

6. Run the application:
    ```bash
    python app.py
    ```

7. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to use the application.

## How it Works

The application consists of two routes:

- **/:** This is the home route where the user can enter a prompt and submit it. The application then generates a story based on the prompt and displays it on the same page.
  
- **/prompt:** This route displays the prompt and the generated story. It also allows the user to enter a new prompt and submit it.

The application uses the OpenAI API to generate the stories. The `prompt` global variable is used to store the current prompt, and the `generated_answer` global variable is used to store the generated story.

