import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GCA_Agent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.system_instructions = """
        You are the Google Cultural Alignment (GCA) AI Coach. 
        Ask exactly ONE question at a time. Wait for a response.
        Tone: Professional, supportive, and 'Googly'.
        
        FLOW:
        Q1: Positive/negative qualities from friends?
        Q2: Self-observed qualities?
        Q3: How do negatives affect others?
        Q4: How do positives help at work?
        PIVOT: Analyze Enneagram. Ask candidate to choose between top 2 types.
        Q5: Resonating strengths?
        Q6: Areas for development?
        Q7: Learning orientation/Self-initiative?
        """

    def get_chat_response(self, chat_session, user_input):
        response = chat_session.send_message(user_input)
        return response.text