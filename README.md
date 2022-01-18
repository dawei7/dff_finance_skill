# dff-TEMPLATE-skill

## Description

**dff_finance_skill** 
## Quickstart

```bash
pip install -r requirements.txt
```
Run interactive mode
```bash
python run_interactive.py
```
Run tests
```bash
python run_test.py
```
## External APIs
### DEEPL API (Authentication key required)
This chat-bot uses DEEPL API (Free 500'000 characters a month) -> https://deepl.com
To avoid writing my key in source code, I set it in an environment variable
called "DEEPL_AUTH_KEY" with the API KEY value. This is a precondition, that the chat works properly.

### yFinance (No authentication key required)
This is a yahoo finance wrapper library, requesting/scraping data from YAhoo Finance.
I use it in the context to get historical data by ticker symbol like "F" for Ford.
The return value is a pandas framework, which I can use to plot the share price in plotly.

### Wikipedia-API (No authentication key required)
Wikipedia-API is another wrapper for requesting/scraping text data from Wikipedia. It is not an official API.
With this API I get back the summary of the ticker companies to load in the context of distilbert-QA NLP model.

### HuggingFace Transformers (No authentication key required)
Huggingface hosts pretrained NLP models. I use "distilbert-base-cased-distilled-squad", which is derived from BERT.
It has been trained with Wikipedia articles for QA.

## Resources
#TODO: resources
* Execution time: depends on user inputs, there is no fixed execution time
* Starting time: Around 20 seconds starting time (Loading distilbert model 250 MB)
* RAM: Max. 500 MB
