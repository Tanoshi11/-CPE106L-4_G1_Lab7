import flask
import sqlite3
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Function to connect to database
def get_db_connection():
    conn = sqlite3.connect("chinook.db")
    conn.row_factory = sqlite3.Row
    return conn

# Route to get albums (with optional filtering by AlbumId)
@app.route('/api/v1/resources/albums', methods=['GET'])
def get_albums():
    conn = get_db_connection()
    cur = conn.cursor()

    # Get the albumid from query parameters
    album_id = request.args.get('albumid')

    if album_id:
        query = "SELECT AlbumId, Title, ArtistId FROM albums WHERE AlbumId = ?"
        cur.execute(query, (album_id,))
    else:
        query = "SELECT AlbumId, Title, ArtistId FROM albums"
        cur.execute(query)

    rows = cur.fetchall()
    conn.close()

    # Convert query results to a list of dictionaries
    albums = [dict(row) for row in rows]

    # If album_id was provided, return a single album (or empty response if not found)
    if album_id:
        return jsonify(albums[0] if albums else {})

    return jsonify(albums)

# Run the application
if __name__ == '__main__':
    app.run()
