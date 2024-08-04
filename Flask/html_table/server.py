
from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)   



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def list():
    return render_template("html_table.html", users=users) 


users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
         ]


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    # app.run(debug=True) should be the very last statement! 

