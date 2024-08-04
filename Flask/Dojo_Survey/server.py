from flask import Flask, render_template, request, session, redirect # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'fido'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('dojo_survey.html')


@app.route('/info', methods=['POST'])          # The "@" decorator associates this route with the function immediately following
def user():
    print(request.form)

    session["name"] = ["name"]
    session["dojo_location"] = ["dojo_location"] 
    session["language"] = ["language"]
    session["comment"] = ["comment"] 
    return redirect('/form_results')


@app.route('/form_results')          # The "@" decorator associates this route with the function immediately following
def display_info():
    print('info.html')
    return render_template('/info.html')


if __name__=="__main__":    
    app.run(debug=True)    
