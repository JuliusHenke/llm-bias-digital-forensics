import os
from openai import OpenAI
from openai.types.chat import ChatCompletion

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate_responses(
        system_message: str,
        user_message: str,
        experiment_title: str,
        numer_of_choices: int = 1,
        max_output_tokens: int = 100,
        seed: int = 0) -> ChatCompletion:
    model = "gpt-3.5-turbo"
    temperature = 0

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model=model,
        n=numer_of_choices,
        max_tokens=max_output_tokens,
        seed=seed,
        temperature=temperature,
    )
    print(f"\n\n######## Experiment: {experiment_title} ########")
    print(f"\n### User message ###\n{user_message}")
    print(f"\n###Response choices###")
    for i in chat_completion.choices:
        print(str(i.index) + ") " + i.message.content)
    save_chat_completion(chat_completion,
                         experiment_title + "_" + model + "_seed" + str(seed) + "_temp" + str(temperature))
    return chat_completion


def save_chat_completion(chat_completion: ChatCompletion, experiment_title: str):
    full_path = "chat_logs/" + experiment_title + ".json"
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(chat_completion.model_dump_json(indent=2))
