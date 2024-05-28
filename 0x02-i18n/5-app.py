#!/usr/bin/env python3
'''Task 4: Force locale with URL parameter
'''

from flask import Flask, g, request, render_template

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Retrieve a user dictionary or None if the ID is invalid."""
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            return None
    return None

@app.before_request
def before_request():
    """Set the user in the global context before each request."""
    g.user = get_user()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

