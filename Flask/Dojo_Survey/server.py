from flask import Flask, render_template, request, session, redirect # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'fido'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('dojo_survey.html')


@app.route('/info', methods=['POST'])          # The "@" decorator associates this route with the function immediately following
def user():
    print(request.form)


    session["name"] = request.form["name"]
    session["location"] = request.form["location"] 
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"] 
    return redirect('/form_results')


@app.route('/form_results')          # The "@" decorator associates this route with the function immediately following
def display_info():
    print('info.html')
    return render_template('/info.html')


@app.route("/clear", methods=["POST"])  # This route is just the path of the url
def clear_session():
    session.clear()
    return redirect("/")


if __name__=="__main__":    
    app.run(debug=True)    
