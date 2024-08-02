from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return 'Dojo'


@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi_flask(name):
    return "Hi " + name + "!"


# Here the second parameter is cast into an integer before being passed to the function
@app.route('/repeat/<int:times>/<name>') 
def repeat(name, times):
    print(name * times)
    return name * times


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    # app.run(debug=True) should be the very last statement! 