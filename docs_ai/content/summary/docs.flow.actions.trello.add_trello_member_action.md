This plugin adds a member to a given card in Trello. It takes any payload as input and returns response from Trello API on port response, or empty payload on error port, if an error occurs. To begin working with Trello inside Tracardi, you need an API key and token. These can be retrieved by logging into Trello and visiting https://trello.com/app-key/. The API key is located at the top of the page and the token is located below the key. Once these are retrieved, they can be typed into Tracardi resources, which can be found under Traffic -> Outbound resources. 

When creating a Trello resource, the form fields must be filled out. This includes the Trello resource, URL of Trello board, name of Trello list, name of your card, and ID of the member. Additionally, the JSON configuration must be filled out, which includes the source, board_url, list_name, list_id, card_name, and member_id. The list_id parameter does not matter and should be left as "" or null. 

It is important to note that if there are two lists with the same name on one board, Tracardi will pick one of them without a method of specifying which one will be picked. This rule also applies to the cards.