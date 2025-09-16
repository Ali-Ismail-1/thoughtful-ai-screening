import gradio as gr
from logic import get_answer

def chatbot(user_input: str, history: list) -> str:
    return get_answer(user_input)

with gr.Blocks() as demo:
    gr.Markdown("## Thoughtful AI Support Agent")
    gr.ChatInterface(fn=chatbot)

if __name__ == "__main__":
    demo.launch()