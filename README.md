**SG**
I modified this to use the schema developed from the other experiment. Modified this to call openai instead of mistral. Upload case studies where one txt file = one case study. You need an openai key. Haven't tested it with other models; see langchain for possibilities.

The [structured_attempt](structured_attempt.ipynb) notebook contains a workflow for taking unstructured information about antiquities or art trade and rendering it into a knowledge graph according to a predefined schema. It can use a variety of LLM via the langchain library to handle the natural language processing, and it uses pydantic and enum libraries to handle the validation. This means that most of the time, the entity names and predicates (relationships) are consistent.

That is to say, you'll usually get 'J. Paul Getty Museum' rather than several variations ('the Getty'; 'Getty Museum' etc) and the relationships will be those in the schema.py and prompt.py files. But sometimes there will be relationships returned that are not in your schema. These cases will be gathered into a separate dataframe for evaluation.

If you wish to add or modify the relationship and entities you are after, you need to modify both those files appropriately, save them. The code is written to reload those modules every time, assuming you want to play around with the schema/prompt.

You will need api access to a large language model access to which is supported by langchain. (eg. OpenAI, Groq, Mistral, etc). OpenAI will cost you, but Groq can be free for experimentation.

# Original README:

# The rising use case of LLM: Structuring unstructured data

This repo contains the code for the blog post ["The rising use case of LLM: Structuring unstructured data"](https://towardsdatascience.com/the-lesser-known-rising-application-of-llms-775834116477). 
The blog post discusses the use of LLMs for structuring unstructured data and show an example by structuring the recipes available at [publicdomainrecipes.com](https://publicdomainrecipes.com/)

## Installation

In order to reuse the code or to reproduce the results, you need to install the required libraries. You can install the required libraries by running the following command:

```bash

pip install -r requirements.txt

```

(Assuming you cloned the repo)

## Usage

The code is available in the form of a Jupyter notebook. You can run the notebook [demo.ipynb](https://github.com/VianneyMI/baker/blob/main/demo.ipynb) and follow along with the blog post.

Some of the logic leaves outside of the notebook.
In particular, the target schema for the recipes is defined in [schemas.py](https://github.com/VianneyMI/baker/blob/main/schemas.py), the prompt for the LLM is defined in [prompt.py](https://github.com/VianneyMI/baker/blob/main/prompt.py), and the communication channel with the LLM is defined in [core.py](https://github.com/VianneyMI/baker/blob/main/core.py).

In the article, I used [Mistral AI](https://mistral.ai/) models to structure the recipes. You can use any other LLMs like [GPT](https://openai.com/index/gpt-4/) or [Llama](https://llama.meta.com/), etc. by importing the ChatModel of your choice from [langchain](https://www.langchain.com/).
You're likely need to provide an API Key to use the LLM which implies that you have an account on the LLM Provider platform.

## Data

The original dataset available [here](https://github.com/VianneyMI/baker/blob/main/data/input/recipes_v1.json) in this repo, originally comes from [Sebastian Bahr's repo](https://github.com/sebastianbahr/RecipeRecommender)

The structured dataset is available [here](https://github.com/VianneyMI/baker/blob/main/data/output/parsed_recipes_all_8x7b.json).

## Contributing

You can  raise issues or pull requests on the [GitHub repo](https://github.com/VianneyMI/baker/issues) if you have any suggestions or improvements, you can also comment the article on [Towards Data Science](https://towardsdatascience.com/the-lesser-known-rising-application-of-llms-775834116477).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/VianneyMI/baker/blob/main/LICENSE)
