import openai

secret_key = "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"

openai.api_key = secret_key

prompt = (f"Write an article on ChatGPT API")

completions = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
