from nltk.chat.util import Chat, reflections
import re

PAIRS = [
    [r"hi|hello|hey", ["Hi there!", "Hello!"]],
    [r"what is your name", ["I'm EduBot, created by Erica."]],
    [r"how are you", ["Doing well, here to help!"]],
    [r"what is edtech", ["Tech that supports learning."]],
    [r"how to study better", ["Use recall, review often, stay focused."]],
    [r"what is nlp", ["It helps machines understand language."]],
    [r"what language do you prefer", ["I can chat in English, unless Erica says otherwise:)"]],
    [r"sorry (.*)", ["No problem."]],
    [r"quit", ["Bye! Keep learning."]],
    [r"(.*)", ["Not sure I got that. Try again?"]],
]

def normalize(text: str) -> str:
    text = text.lower().strip()
    return re.sub(r"[^\w\s]", "", text)

def create_chatbot():
    return Chat(PAIRS, reflections)

def get_response(chatbot: Chat, user_input: str) -> str:
    cleaned = normalize(user_input)
    return chatbot.respond(cleaned) or "Not sure I got that. Try again?"