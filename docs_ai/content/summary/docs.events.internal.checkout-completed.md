This documentation provides information about the event "Checkout Completed". This event should be used when a customer has completed the check-out process, such as when they add items to their cart, enter their payment and shipping information, and click "Submit Order". The expected properties for this event are optional, and if any property is missing it will not be processed and no error will be reported. The expected properties are "id" which is a string, and an example of this is "Checkout ID: 5678-efgh-1234-abcd".

Auto indexing is also discussed in this documentation, which helps to make data easy to find by creating a structure that organizes the data. This structure is made by copying information from the different parts of the data and putting it into a specific format that can be used to analyze and group the data. This table describes which event property will be copied to event traits, such as "ec.checkout.id" and "ec.checkout.status".

Finally, this documentation states that data will not be copied to profile for this event. An example of the JSON properties for this event is also provided.

