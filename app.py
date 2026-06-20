import gradio as gr

faq = {
    "admission": "Students must submit transcripts and application forms.",
    "scholarship": "Scholarships can be applied through the student portal.",
    "services": "Career counseling, tutoring, and library services."
}

def chatbot(message):
    message = message.lower()

    for key in faq:
        if key in message:
            return faq[key]

    return "Sorry, I do not have information about that."

demo = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="University Student Support Chatbot"
)

demo.launch()