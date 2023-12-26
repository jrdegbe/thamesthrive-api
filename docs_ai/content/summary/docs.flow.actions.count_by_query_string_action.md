This plugin is designed to count records in a given index, that match a given query and are within a given time range. It takes any payload as input and returns the number of records on port **result**, or optional error information on port **error** if one occurs. 

The plugin can be configured either with a form or with advanced configuration. With the form, the user must provide the index, time range, and query string. The time range must be a valid negative time expression, such as **-14d** or **-15 minutes**. The query string must be a valid Elasticsearch query string, such as **profile.id:{{profile@id}} AND type:page-view**. 

The advanced configuration requires a JSON object with the index, time range, and query. The index must be one of the following: event, session, or profile. The time range must be a valid negative time expression, and the query must be a valid Elasticsearch query string.

