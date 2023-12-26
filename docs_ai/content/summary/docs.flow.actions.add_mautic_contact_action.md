This plugin allows users to add a new contact to their Mautic account. It takes any payload as input and returns a response from the Mautic API on the response port, or an optional error info on the error port if one occurs.

The plugin configuration requires users to select their Mautic resource, which should contain the Mautic API URL, Mautic Client private key, and Mautic Client public key. Additionally, users must provide the path to the email address of their new contact, as well as any optional mapping for their contact, such as lastname: profile@traits.public.surname. Finally, users can choose to overwrite fields that are not mentioned in the configuration with empty values.

The JSON configuration for this plugin includes the source ID and name of the Mautic resource, the path to the email address of the new contact, any additional mapping, and a boolean value for whether or not to overwrite fields with blank.

