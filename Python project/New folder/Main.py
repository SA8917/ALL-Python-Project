import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str) -> dict:
    with open('All Html pages/Chat.bot/Knowledge_base.json', 'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open('All Html pages/Chat.bot/Knowledge_base.json', 'w') as file:
        json.dump(data, file, indent=4)


def find_best_match(question: str, knowledge_base: dict) -> str | None:
    matches : list = get_close_matches(question, knowledge_base, n=1, cutoff=0.8)
    return matches[0] if matches else None

def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base['questions']:
        if q['question'].lower() == question.lower():
            return q['answer']
    return None

def chatbot():
    knowledge_base = load_knowledge_base('Knowledge_base.json')
    while True:
        User_questions = input("You: ")
        best_match : str | None = find_best_match(User_questions, [q['question'] for q in knowledge_base['questions']])
        if User_questions.lower() == 'exit' or User_questions.lower() == 'bye':
            print("Web.Assistant: Goodbye!")
            break
        if best_match:
            answer = get_answer(best_match, knowledge_base)
            print(f"Web.Assistant: {answer}")
        else:
            print("Web.Assistant: I'm sorry, I don't understand that question.Can you teach me?")
            new_question : str =input("Type the 'answer' for the question or "'type (skip)'" if you don't want to answer: ")

            if new_question.lower() != 'skip':
                knowledge_base['questions'].append({'question': User_questions, 'answer': new_question})
                save_knowledge_base('Knowledge_base.json', knowledge_base)
                print("Web.Assistant: Thank you for teaching me!")
            elif new_question.lower() == 'skip':
                print("Web.Assistant: Thanks for your time!")
            else:
                print("Web.Assistant: I'm sorry, I don't understand that question.")

if __name__ == "__main__":
    chatbot()

