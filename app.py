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

#localhost:5000/user/amit
@app.route('/user/<name>')
#הסימני קריאה יהיו קבועים לפני השם שאני מקליד
def user (name):
    return "<h1>Hello {}!!!</h1>".format(name)

# Run the application only if this script is the main entry point
#הפעל את היישום רק אם סקריפט זה הוא נקודת הכניסה הראשית
if __name__ == "__main__":
    app.run(debug=True)



