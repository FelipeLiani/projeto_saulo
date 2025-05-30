from groq import Groq

client = Groq(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)


print(chat_completion.choices[0].message.content)
