import os

from flask import Flask, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static",
)


def find_index_folder():
    """Look for index.html in static/ first, then next to app.py."""
    for folder in (os.path.join(BASE_DIR, "static"), BASE_DIR):
        if os.path.isfile(os.path.join(folder, "index.html")):
            return folder
    return None


@app.route("/")
def index():
    folder = find_index_folder()
    if folder is None:
        return (
            "index.html was not found. Upload the 'static' folder (with "
            "index.html inside it) to the same place as app.py in your "
            "GitHub repository, then redeploy.",
            500,
        )
    return send_from_directory(folder, "index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
