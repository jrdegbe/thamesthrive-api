This plugin allows users to fetch a contact from Mautic, based on a provided contact ID. The plugin takes any payload as input and returns a response from the Mautic API on the port 'response', or an optional error info on the port 'error' if one occurs.

The plugin configuration requires two form fields: the Mautic resource, which should contain the Mautic API URL, Mautic Client private key, and Mautic Client public key; and the Contact ID, which should be the path to the ID of the contact that the user wants to fetch. Additionally, the plugin requires a JSON configuration, which should include the source ID and name of the Mautic resource, as well as the path to the contact ID.

