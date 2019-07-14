## Flask notes
- hello.py
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
```
to run it: python hello.py - http://127.0.0.1:5000/ 

- Werkzeug WSGI Toolkit
- Jinja2 templating engine
- flask application is started by calling run() method
- enable debug mode:  app.run(debug = True)
- routing: 
- variable rules
- URL binding
    - The route() decorator in Flask is used to bind URL to a function
        ```@app.route('/blog/<int:postID>')```
    - url_for() - function is used for dynamically building a URL for a specific function
    - The add_url_rule() function of an application object is also available to bind a URL with a function
        ```app.add_url_rule(‘/’, ‘hello’, hello_world)```

## notes
- GET  - Sends data in unencrypted form to server
- HEAD - Same as GET, but without response body
- POST - Used to send HTML form data to server
- PUT  - Replaces all current representations of target resource with uploaded content
- DELETE - Removes all current representations of target resource given by URL













## Links
1. https://www.youtube.com/watch?v=lj4I_CvBnt0
