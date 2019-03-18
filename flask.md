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

