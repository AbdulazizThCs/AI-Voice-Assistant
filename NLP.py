import cohere

# Initialize Cohere client with your API key
co = cohere.Client("")

def generate_reply(prompt):
    # Generate a short Arabic reply from prompt
    response = co.chat(
        message=prompt,
        temperature=0.5,
        chat_history=[
            {"role": "SYSTEM", "message": "أجب بالعربية فقط، وباختصار شديد."}
        ]
    )
    return response.text.strip()