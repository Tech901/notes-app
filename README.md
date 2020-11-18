# Notes app

This is a demo app that includes examples of the following:

- a simple command-line app using Python to talk to a SQLite Database (`notes.py`)
- a simple Flask-based app that gives you a web app to talk to the same database (`application.py`).


## Dependencies

All of this code was written using Python 3. The command-line tool uses only
code from the python standard library, but for the web app, you'll need to
install Flask:

    pip install flask


## The command-line app

Run the command line app as follows:


- `python notes.py -h` to see the menu
- `python notes.py -c "Some content"` to create a note
- `python notes.py -d ID` to delete a note.


## The web app

Run the app using flask's development server in debug mode:

    FLASK_ENV=development FLASK_DEBUG=1 flask run

## License.

This code is freely available under the terms of the MIT license. See the included
`LICENSE` file.
