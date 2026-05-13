import requests

invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = True

headers = {
    "Authorization": "Bearer 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",
    "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
    "model": "google/gemma-3n-e2b-it",
    "messages": [{"role": "user", "content": "Hello, how are you?"}],
    "max_tokens": 512,
    "temperature": 0.20,
    "top_p": 0.70,
    "frequency_penalty": 0.00,
    "presence_penalty": 0.00,
    "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())