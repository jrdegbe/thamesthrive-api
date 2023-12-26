This plugin allows users to add or subtract points from a given contact in Mautic, based on the contact's ID. The plugin takes any payload as input and returns a payload on the success port if the action was successful, or additional error info on the error port if one occurs. 

The plugin configuration requires users to select a Mautic resource, containing private and public key with API URL, define an action (add or subtract), type in the path to the field containing contact's ID, and type in the number of points that they want to add to or subtract from the given contact. Additionally, the plugin requires a JSON configuration, which includes the source (ID and name of the Mautic resource), action (add or subtract), contact ID, and number of points as a string.

