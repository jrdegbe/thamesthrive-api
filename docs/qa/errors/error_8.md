# What issue can occur when using the "/track/" endpoint with HTTPS connection in ThamesThrive?

When using the "/track/" endpoint with an HTTPS connection in ThamesThrive, there can be an issue with the redirection. The
system redirects "/track/" to "/track," but this redirection may cause the HTTPS connection to be lost. It is
recommended to avoid using a trailing backslash in API calls to prevent this issue.
