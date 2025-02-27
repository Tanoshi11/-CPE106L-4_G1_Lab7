import flask
import sqlite3
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Function to convert query results to a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Route: Home Page
@app.route("/", methods=["GET"])
def home():
    return "<h1>Accessing Chinook Database</h1><p>A prototype API for accessing the Chinook SQLite database.</p>"

# Route: Get all albums
@app.route("/api/v1/resources/albums/all", methods=["GET"])
def get_all_albums():
    conn = sqlite3.connect("chinook.db")  # Connect to the database
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("SELECT AlbumId, Title, ArtistId FROM albums")  # Query albums table
    albums = cur.fetchall()
    return jsonify(albums)

# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
