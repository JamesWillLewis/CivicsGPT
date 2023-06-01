# CivicsGPT

## About

CivicsGPT is a GPT-based chatbot for practicing the US naturalization Civics test.

At some point I'll make a website for this. 

## Requirements

This requires `Python 3.7.1` or above. 

## Installation

To check out the code, run

```commandline
gh repo clone JamesWillLewis/CivicsGPT
```

Or

```commandline
git clone https://github.com/JamesWillLewis/CivicsGPT.git
```

Install dependencies

```commandline
pip3 install -r requirements.txt
```

Set your OpenAI API key with

```commandline
export OPENAI_API_KEY="YOUR_API_KEY"
```

Or alternatively, create an `.env` file.

```commandline
echo 'export OPENAI_API_KEY="YOUR_API_KEY"' >> .env
```

## Usage 

To run without any options

```commandline
./cli.sh
```

You can optionally specify `temperature` and `max_tokens` as arguments
```commandline
./cli.sh 0.8 16
```




## Development

After adding or changing dependencies, run
```commandline
pip3 freeze > requirements.txt
```
