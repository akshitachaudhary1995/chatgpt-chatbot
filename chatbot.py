from openai import OpenAI
import gradio 

OPENAI_API_KEY= "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"
client = OpenAI(api_key=OPENAI_API_KEY)

messages = [{"role": "system", "content": "You are a writing assistant"}]

def CustomChatGPT(askme):
    messages.append({"role": "user", "content": askme})
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Akshita's Chatbot")

demo.launch(share=True)