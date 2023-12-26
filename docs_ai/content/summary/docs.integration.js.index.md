This documentation provides instructions on how to integrate a JavaScript snippet into a web page for tracking and
personalization purposes with ThamesThrive. The snippet must be pasted in the header of the web page, and it includes a
configuration code and an event source ID. The configuration code includes the URL of the ThamesThrive tracker and API, and
the event source ID is found in the Inbound traffic section of the ThamesThrive GUI. Events are defined in a separate
script, and they consist of an event type and additional data. The event type is a unique identifier that helps
differentiate events from one another, and it is essential for proper categorization and processing of events within
ThamesThrive. After refreshing the web page with the JavaScript code, a response from ThamesThrive may appear if the event
source ID was not defined correctly. To resolve this, create an event source in ThamesThrive and replace the string <
your-resource-id-HERE> with the actual event source ID from ThamesThrive. Additionally, the IP of the ThamesThrive API must be
replaced in the configuration code. Following these steps will ensure that the JavaScript snippet is properly integrated
into the web page.
