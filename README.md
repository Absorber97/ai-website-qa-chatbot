# AI-Powered Website Q&A Chatbot

This project is an AI-powered chatbot that can answer questions about website content using natural language processing and machine learning techniques.

## Features

- Web scraping to extract content from user-specified URLs
- Natural language processing for understanding user queries
- AI-powered response generation using GPT models
- User-friendly interface built with Streamlit

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-website-qa-chatbot.git
   cd ai-website-qa-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app:
```
streamlit run src/ui/streamlit_app.py
```

Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Project Structure

- `src/core/website_qa.py`: Core functionality for web scraping and AI-powered Q&A
- `src/ui/streamlit_app.py`: Streamlit-based user interface
- `src/utils/helpers.py`: Utility functions
- `.env`: Environment variables (not tracked by Git)
- `requirements.txt`: Python dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.