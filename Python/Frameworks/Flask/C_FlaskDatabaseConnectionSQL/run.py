import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    """Allows access to database and database operations
    in the flask shell with flask shell command in terminal"""
    return {"sa": sa, "so": so, "db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run(debug=True)
