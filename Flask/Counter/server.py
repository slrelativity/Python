#worked with Cory
#from click import clear
from flask import Flask, render_template, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "fido"

@app.route("/")  # This route is just the path of the url
def check_count():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template("counter.html")

@app.route("/plus_1", methods=["POST"])   # This route is just the path of the url
def plus_1():
    if "count" in session:
        session["count"] + 1
    else:
        session["count"] = 1
    return redirect("/")

@app.route("/reset", methods=["POST"])  # This route is just the path of the url
def reset_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    # app.run(debug=True) should be the very last statement! 