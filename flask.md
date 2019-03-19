## Notes
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
    - url_for() - function is used for dynamically building a URL for a specific function















## Links:
