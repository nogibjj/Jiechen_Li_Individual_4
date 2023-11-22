from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load CSV Data
books_df = pd.read_csv("books.csv", on_bad_lines="skip")


@app.route("/")
def index():
    return "Welcome to BookBuddy!"


@app.route("/recommend", methods=["GET"])
def recommend():
    title = request.args.get("title")
    author = request.args.get("authors")
    column, query = ("title", title) if title else ("authors", author)

    if query:
        recommended_books = books_df[
            books_df[column].str.contains(query, case=False, na=False, regex=False)
        ].head(5)
        return jsonify(recommended_books.to_dict(orient="records"))

    error_msg = "Please provide a title or an author's name for recommendations"
    return jsonify({"error": error_msg}), 400


if __name__ == "__main__":
    app.run(debug=True)
