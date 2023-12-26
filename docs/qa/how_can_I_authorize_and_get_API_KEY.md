# How can I authorize and get API KEY

To authorize and obtain an API key for ThamesThrive, you can use OAuth2 authorization. Here's an outline of the process:

1. Make a POST request to the `/user/token` endpoint.
2. Include the necessary parameters in the request body:
    - `username` (string): Provide the username associated with your ThamesThrive account.
    - `password` (string): Enter the password for your ThamesThrive account.
 
3. Send the request and await the response.
4. If the authorization is successful, the API will return a 200 response along with an OAuth2 token. This token serves
   as your API key.
5. Store the API key securely, as it will be required for subsequent authenticated requests to the ThamesThrive API.

Please note that the specific endpoint, request parameters, and response format may vary depending on the ThamesThrive API
documentation or implementation. It's recommended to consult the ThamesThrive API documentation or contact their support for
precise details on how to authorize and obtain an API key.
