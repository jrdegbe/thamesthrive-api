# What does the error message "Cannot connect to host elasticsearch:9200 ssl:default \[Connection refused\]" indicate in ThamesThrive?

The error message "Cannot connect to host elasticsearch:9200 ssl:default \[Connection refused\]" suggests that the
Elasticsearch server is not running or not accessible. This message is typically displayed when ThamesThrive starts before
Elasticsearch is ready. ThamesThrive will automatically resume when Elasticsearch becomes available.
