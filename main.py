import openai
import os

# Set the API key
openai.api_key = "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"

# Set the model to use
model_engine = "text-davinci-002"

# Set the prompt
prompt = "What is the weather like today?"

# Set the number of completions
num_completions = 1

# Set the temperature (between 0 and 1)
temperature = 0.5

# Set the top_p value (between 0 and 1)
top_p = 1

# Set the frequency_penalty value (between 0 and 1)
frequency_penalty = 0

# Set the presence_penalty value (between 0 and 1)
presence_penalty = 0

# Send the request
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=num_completions,
    temperature=temperature,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty
)

# Print the response
print(completions.choices[0].text)
