# Event options

Event options in ThamesThrive allow you to define the behavior of events and add contextual information associated with an
event. When events are triggered using the ThamesThrive JavaScript snippet, they automatically include default context
information, such as browser information and metadata, to provide additional details about the event.

## Default Event Context in JavaScript Snippet

The default event context attached by the ThamesThrive JavaScript snippet includes the following information:

```json
{
  "page": {
    "url": "<page-url>",
    "path": "<page-path>",
    "hash": "<page-hash>",
    "title": "<page-title>",
    "referer": {
      "host": null,
      "query": null
    },
    "history": {
      "length": 10
    }
  },
  "ip": "127.0.0.1"
}
```

The event context includes details about the current page, such as its URL, path, hash, title, referer information (host
and query), and browsing history length. It also includes the IP address of the user.

!!! Tip

    When working with ThamesThrive, you have the option to configure whether or not to include page data in the context of 
    each event. This configuration is done at the tracker level and can be customized according to your requirements. 
    By adjusting the tracker context configuration, you can easily control whether or not page data is sent along with 
    each event, providing you with flexibility and control over the data captured and processed.

## Customizing Event Context

You can add additional context information to events by including a "context" key in the options when triggering events
using the ThamesThrive JavaScript snippet. For example:

```javascript title="Example" linenums="1" hl_lines="5"
window.tracker.track(
   "page-view",
   {},
   {
    "context": {"tag": "search"}
   });
```

In the example above, a custom context object with a "tag" key and value "search" is added to the event options. This
allows you to include additional information that is relevant to your specific use case.

## Beacon tracks

Beacon events in ThamesThrive are events that are sent even if the customer leaves the page. These events allow you to track
user interactions that may occur after a user has navigated away from a page, providing valuable insights into user
behavior.

To configure a beacon event in ThamesThrive, you can add the asBeacon: true option to the track configuration. This
indicates that the event should be sent as a beacon event.

### Example of Beacon Event

Here is an example of how to configure a beacon event in ThamesThrive:

```javascript title="Example" linenums="1"
window.tracker.track("page-view", {}, {"fire": true, asBeacon: true});
```

In the above example, the asBeacon option is set to true, indicating that the "page-view" event should be sent as a
beacon event, even if the customer leaves the page.

Beacon events can be useful in scenarios where you want to track user interactions that may occur outside of the
webpage, such as form submissions, button clicks, or other events that may happen after the user has navigated away from
the page

