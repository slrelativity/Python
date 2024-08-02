# Cory assisted my greatly with this exercise



from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)   


@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def index_a(color = "blue"):
    print(color)
    return render_template('index.html', color = "blue", x = 3)   # noqa: F821


@app.route('/play/<int:times>')          # The "@" decorator associates this route with the function immediately following
def index_1(times, color = "blue"):
    print(color)
    return render_template('index.html', x = times, color = "blue")   # noqa: F821


@app.route('/play/<int:times>/<color>')          # The "@" decorator associates this route with the function immediately following
def index_2(times, color):
    print(color * times)
    return render_template('index.html', x = times, color = color)   # noqa: F821



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    # app.run(debug=True) should be the very last statement! 