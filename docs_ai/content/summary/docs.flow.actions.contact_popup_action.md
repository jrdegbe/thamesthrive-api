This plugin is used to show a contact widget to the user. The widget allows the user to provide contact data (phone number or email address) which will be sent back in a ThamesThrive event. The plugin takes any payload as input and returns the same payload on the port **payload** without any changes. 

The plugin configuration requires the user to provide a URL of the API where the widget is located, a URL of the API to send the event back to, a template of the message for the contact popup, the type of contact data to be provided (email or phone number), the horizontal and vertical positions for the popup, the type of event to be sent back, whether the event should be saved or not, and whether the dark theme should be enabled or not. 

The advanced configuration requires the user to provide a JSON object with the following fields: uix_source, api_url, content, contact_type, horizontal_pos, vertical_pos, event_type, save_event, and dark_theme.
