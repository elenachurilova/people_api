from flask import (Flask, render_template)
import connexion

# creating the application instance
app = connexion.App(__name__, specification_dir='./')

# read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# create a URL route in the application for "/"
@app.route("/")
def home():
    """Home route function responding on localhost:5000/"""
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)

