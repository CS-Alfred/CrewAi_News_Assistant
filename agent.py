from crewai import Agent, Task, Crew, Process

#creating the agents for the finding, summarizing and dispatching the information.

researcher = Agent(
    role="Senior Digital Research Specialist", 
    goal="Discover, extract, and verify the latest factual advancements in emerging technologies and financial markets.", 
    backstory="""You are a veteran investigative researcher with a background in computer science and library science. 
    You have decades of experience executing precision digital research. You have worked with industry leaders in tech 
    and research faculties at prestigious universities. You specialize in separating facts from fluff.""", 
    allow_delegation=False, 
    verbose=True
)

summarizer = Agent(
    role="Executive Editor and Summarizer",
    goal="Distill complex raw research findings into highly readable, concise, and engaging bullet points.", 
    backstory="""You are a ruthless copy editor and technical writer. You have spent your career taking dense, 
    complex research reports and turning them into clear, actionable briefings for busy executives. You know how 
    to highlight the most important data without losing context.""",
    allow_delegation=False,
    verbose=True
)

dispatcher = Agent(
    role="Communications Dispatcher",
    goal="Securely and accurately transmit finalized briefings to the designated external platform (Telegram).",
    backstory="""You are a strict, no-nonsense logistics and API coordinator. You do not edit or change the message 
    content; your sole purpose is to ensure the payload is successfully delivered to the target audience via the 
    required communication protocols. You never fail a delivery.""",
    allow_delegation=False,
    verbose=True
)


#Defining the task for the agents to perform.

research_task = Task(
    description="""Scour the web using your search tool to identify the 5 most impactful news stories 
    published in the last 24 hours covering technology, the economy, and the stock market. 
    Prioritize highly reputable financial and tech news sources (e.g., Reuters, Bloomberg, TechCrunch) 
    and strictly ignore opinion pieces, rumors, or clickbait. Extract the core factual details of each story.""",
    expected_output="""A structured raw data report containing 5 news items. Each item must include:
    - The exact Headline
    - The Publication Source
    - The URL
    - A 2-paragraph extraction of the most important facts and figures.""",
    agent=researcher
)


summarize_task = Task(
    description="""Analyze the raw news report provided by the Researcher and distill each of the 5 stories 
    into a concise, punchy 3-bullet-point summary. Eliminate all journalistic fluff and focus strictly 
    on what happened, why it matters, and any relevant market or technological impact. 
    Format the entire compilation specifically for Telegram by using appropriate emojis (e.g., 📈, 🚀, 📰) 
    for section headers and bolding key entities, company names, or financial numbers.""",
    expected_output="""A single, highly polished, readable text block containing all 5 summarized stories, 
    fully formatted with Markdown and emojis, ready to be pasted directly into a messaging app. 
    Do not include any conversational filler.""",
    agent=summarizer
)


dispatch_task = Task(
    description="""Take the finalized, Telegram-formatted digest provided by the Summarizer and execute the 
    secure transmission to the designated Telegram channel using your Telegram communication tool. 
    You must send the payload exactly as received; do not alter, edit, or append any text to the digest.""",
    expected_output="""A final confirmation string indicating the success or failure of the Telegram API call, 
    including the timestamp of delivery and the exact message payload that was transmitted.""",
    agent=dispatcher
)


news_crew = Crew(
    agents=[researcher, summarizer, dispatcher],
    tasks=[research_task, summarize_task, dispatch_task],
    process=Process.sequential, # ensures tasks are executed sequentially.
    verbose=True
)
    
