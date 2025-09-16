from rapidfuzz import process
from data import data

qa_list = data["questions"]
questions = [item["question"] for item in qa_list]

qa_dict = {item["question"]: item["answer"] for item in qa_list}

def get_answer(question: str) -> str:
    """ Return the answer to the question """
    match, score, _ = process.extractOne(question, questions)
    if score > 70:
        return qa_dict[match]
    else:
        # TODO: Implement asking OpenAI API for determining question type
        return "I'm sorry, I don't know the answer to that question."