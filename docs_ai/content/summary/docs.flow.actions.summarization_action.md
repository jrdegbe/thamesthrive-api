This plugin is designed to summarize text using MeaningCloud's summarization API. It takes any payload as input and returns the response from the API on the response port, or an optional error on the error port if one occurs. The plugin can be configured with a form or with advanced configuration. 

When using the form, the user must select their MeaningCloud resource, containing their API token, and type in the path to the text they want to summarize, the path to the language of the text (or the language itself) and the number of sentences for the text to be summarized to. 

When using the advanced configuration, the user must provide a JSON object containing the name and ID of their MeaningCloud resource, the path to the text to analyze, the path to the language code or the language itself, and a numeric string for the number of sentences.
