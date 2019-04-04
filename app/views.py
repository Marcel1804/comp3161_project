from app import app, db
from flask import render_template, request, redirect, url_for, flash

@app.route("/")
def main():
    return "Welcome!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
