# Import flask library:
# Import render_template for using templates in template folder.
# Import url_for
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Create a user class w/ first and last names:
class User:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	# Return the user's initials:
	def initials(self):
		return "{}. {}.".format(self.firstname[0], self.lastname[0])

	# ToString method to return first and last name.
	def __str__(self):
		return self.firstname + " " + self.lastname

# Define a route for root view and /index view.
@app.route('/')
@app.route('/index')

def index():
    # Use render_template we imported to render the html page
    # in the templates folder.
    # title and text are passed into the view.
    # So this text will appear in the {{ title }} and the {{ text }} in
    # index.html
    return render_template(
    	'index.html',
    	title="Title passed from the view template",
    	text="Text passed from the view template",

   		# Array Example:
    	myArray=["first", "second", "third", "Knie"],

    	# Passing a function w/ arg into the template example:
    	user=User("Christopher", "Adams")
    )

# Define route for add.html
@app.route('/add')
def add():
	return render_template('add.html')

# Run the app:
# debug=True means put app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)