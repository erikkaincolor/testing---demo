"""Simple Flask app to demonstrate some testing."""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Show homepage."""

    return render_template("index.html")


@app.route('/fav-color', methods=['POST'])
def fav_color():
    """Show favorite color."""

    fav_color = request.form.get('color')

    return render_template("color.html", fav_color=fav_color)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
