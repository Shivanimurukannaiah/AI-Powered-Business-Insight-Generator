
import openai
import yaml

def load_api_key(config_path='../config/settings.yaml'):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config['openai_api_key']

def generate_insights(summary):
    prompt = f"Here is a summary of business data: {summary}\nGenerate a few insights:"
    openai.api_key = load_api_key()
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['choices'][0]['message']['content']
