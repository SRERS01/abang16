In JavaScript, how you accept website input depends entirely on whether your code is running inside the web browser (Frontend) or on a web server (Backend/Node.js). [1, 2] 
Here is the complete list of built-in features used to capture website input for both environments:
## 1. Frontend JavaScript (The Web Browser)
Frontend JavaScript runs directly on the user's browser and interacts with the page (DOM). [3, 4, 5] 

* window.location.search: Captures the raw URL query string (everything starting from the ?).
* URLSearchParams: A built-in class used to easily parse and read specific parameters from window.location.search.
* FormData: A built-in object that instantly captures all inputs, textareas, and file selections from an HTML <form>.
* document.querySelector().value: Reads the live input value from specific text boxes, checkboxes, or dropdown selectors on the website page.
* document.cookie: Accesses a string containing all cookies stored by the browser for that website. [6, 7, 8, 9, 10] 

------------------------------
## 2. Backend JavaScript (Node.js Standard Library)
If you are running a server using raw Node.js without any libraries, you rely on the built-in HTTP request object (req) passed into the server callback.

* req.url: Captures the full incoming request path and query parameters as a string.
* URL module: A built-in Node.js module used to parse req.url to extract specific query values.
* req.headers: An object containing all HTTP headers sent by the browser.
* req.on('data', ...): A built-in event listener used to collect the incoming request body (like JSON or form submissions) piece by piece as a stream of raw bytes. [11, 12, 13] 

------------------------------
## 3. Express.js Framework (Standard Node.js Backend)
Because raw Node.js streams are complex, almost all JavaScript backend developers use the Express.js framework, which simplifies input parsing into a single req object. [14] 

* req.query: An object containing URL query parameters (equivalent to PHP's $_GET).
* req.body: Holds data submitted in the request body (like JSON payloads or form data). Requires built-in middleware like express.json() or express.urlencoded() to automatically read it.
* req.params: Captures route parameters from clean URLs (e.g., matching the 123 in /user/:id as /user/123).
* req.cookies: Reads incoming cookies. Requires the cookie-parser middleware.
* req.headers: Captures request headers sent from the browser. [15, 16, 17, 18, 19] 

Are you building a frontend site that reads text inputs from a page, or are you building a backend server in Node.js to receive data? Let me know so I can provide a matching code example! [20] 


