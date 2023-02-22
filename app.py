# pip install flask
from flask import Flask

print('__name__ =>', __name__)
app = Flask(__name__)

# Register a route. A route is anything after the domain name.
# /: represents an empty route. Basically, the home page of the domain on which the website is hosted.
@app.route("/")
# Then when a user goes to that route or path, display Hello, World!
def hello_world():
  return("<p>Hello, World! Welcome</p>")

# Then run app. There are 2 ways to run
# Option 1:
  # export FLASK_APP=name_of_file
  # flask run
# Option 2:
if __name__=='__main__':
  app.run(
    host='0.0.0.0', 
    port = 5000,
    debug = True
  )