from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)
# Create a route decorator
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/docker')
def docker():
    return render_template("docker.html")

@app.route('/lesson1')
def lesson1():
    return render_template("lesson1.html")



#localhost:5000/user/amit
@app.route('/user/<name>')
def user (name):
     return render_template("user.html", user_name=name)

# Run the application only if this script is the main entry point
#הפעל את היישום רק אם סקריפט זה הוא נקודת הכניסה הראשית
if __name__ == "__main__":
    app.run(debug=True)



