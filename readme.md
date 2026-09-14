# CrewAi News Assistant
### This project is an automated multi agent AI pipeline built with Python, CrewAI, Gemini API, and the Telegram API that independently researches, summarizes, and dispatches daily financial and technology news.


## Overview
This application uses the CrewAi framework to coordinate a team of autonomous AI agents working together to automate daily tech news cycle.
We can save a lot of time which is lost in browsing and reading through each blog page or website, in this project there are three agents, the __Researcher__ agent does the web searching using googles's serper api to find recent news on technology, it is then passed to the __Summarizer__ which formats the information to concise bullet points and finally the __Dispatcher__ agent sents the points to __Telegram__ channel where the user can read it.

## Video Demo

## Features
* Utilizes CrewAI to assign specific roles, goals, and backstories to AI agents.
* Integrates __SerperDevTool__ to search Google and extract real time factual data from highly reputable financial and tech news sources.
* Distills dense journalistic articles into highly readable, punchy 3 bullet point executive summaries.
* Transmits the finalized, Markdown formatted digest directly to a designated Telegram chat using a custom tool.

## Technologies Used
* Python
* CrewAI & CrewAI Tools
* LiteLLM (Compatible with DeepSeek, Gemini, Groq, or OpenAI)
* Serper API
* Telegram Bot API

## Basic Requirements
* Python 3.11+
* Gemini API Key
* Serper API Key
* Telegram Bot Token & Chat ID

## Installation
1. Clone repository
    - git clone https://github.com/CS-Alfred/CrewAi_News_Assistant
        1. Navigate to project folder
           - cd CrewAi_News_Assistant
2. Create a virtual environment
    - python -m venv venv
        1. To activate in windows
            - venv\Scripts\activate
        2. To activate in macOS/Linux
            - source venv/bin/activate
3. Install Dependencies
    - pip install -r Requirements.txt

4. Configure API Keys
    - Create a .env file in the project root
        **GEMINI_API_KEY=your gemini api key**
        **SERPER_API_KEY=your serper api key**
        **TELEGRAM_BOT_TOKEN=your telegram bot token**
        **TELEGRAM_CHAT_ID=your telegram chat id**

    *** Replace the placeholder values with your own API keys. ***   

    *** Important: Never commit your .env file or expose your API keys publicly. *** 

5. Run the application
    - python agent.py

## References and Resources
This project was developed by studying and referring to documentation, tutorials, videos, and resources related to RAG, LangChain, vector databases, embeddings, and LLM applications.

### Documentation
* [CrewAi Documentation](https://docs.crewai.com/)
* [Serper Documentation](https://serper.dev/)
* [Gemini Documentation](https://aistudio.google.com/)
* [Telegram Documentation](https://core.telegram.org/)

## Author
[C S Alfred](https://github.com/CS-Alfred)

