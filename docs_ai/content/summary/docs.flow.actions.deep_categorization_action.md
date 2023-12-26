This plugin is used to send text to MeaningCloud's Deep Categorization API to analyze it. It takes any payload as input and returns the response from the API on the response port, or optional error info on the error port if one occurs. The plugin can be configured with a form or with advanced configuration. 

When configuring with a form, the user must select their MeaningCloud resource, containing their MeaningCloud API token, and type in the path to the text they want to analyze. The API analyzes text using different models, such as IAB_2.0_**language**, IAB_2.0-tier3_**language**, and IAB_2.0-tier4_**language**. The user can also use these models without the _**language** suffix for automatic language detection. 

When configuring with advanced configuration, the user must provide a name and ID of their MeaningCloud resource, the path to the text they want to analyze, and the model name. The advanced configuration is provided in JSON format.

