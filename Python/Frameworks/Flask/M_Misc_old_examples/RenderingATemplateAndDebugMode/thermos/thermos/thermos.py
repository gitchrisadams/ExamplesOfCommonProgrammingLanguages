# Import flask library:
# Import render_template for using templates in template folder.
# Import url_for
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Define a route for root view and /index view.
@app.route('/')
@app.route('/index')

def index():
    # Use render_template we imported to render the html page
    # in the templates folder.
    return render_template('index.html')

# Run the app:
# debug=True means put app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)