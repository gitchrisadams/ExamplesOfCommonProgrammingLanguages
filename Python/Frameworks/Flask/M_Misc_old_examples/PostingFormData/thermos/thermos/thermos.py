# Import flask library:
# Import render_template for using templates in template folder.
# Import request which will be bound to current http request.
# Import redirect to redirect user to another page.
# Import url_for for url routing.
from flask import Flask, render_template, request, redirect, url_for

# Import datetime:
from datetime import datetime

from logging import DEBUG

app = Flask(__name__)

# Set debugging level:
app.logger.setLevel(DEBUG)

# Create empty bookmarks array:
bookmarks = []

# Define method to store a bookmark:
def store_bookmark(url):
	bookmarks.append(dict(
		url = url,
		user = "Adams",
		date = datetime.utcnow()
	))

# Define a route for root view and /index view.
@app.route('/')
@app.route('/index')

def index():
    # Use render_template we imported to render the html page
    # in the templates folder.
    return render_template(
    	'index.html'
    )

# Define route for add.html
# Must use methods=['GET', 'POST'] to use POST when submitting form.
@app.route('/add', methods=['GET', 'POST'])
def add():
	# If the request method a POST Request process the input data.
	if request.method == "POST":

		# Get the text the user has entered in the input form.
		url = request.form['url']
		store_bookmark(url)
		app.logger.debug('stored url: ' + url)

		# App has been submitted so redirect to the index page:
		return redirect(url_for('index'))

	# If there is no POST then just render the add.html page:
	return render_template('add.html')

# Define custom error 404 pages:
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Define custom error 500 pages:
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

# Run the app:
# debug=True means put app in debug mode. 
if __name__ == "__main__":
    app.run(debug=True)