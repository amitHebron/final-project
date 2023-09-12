from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)
# Create a route decorator
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/lesson1')
def lesson1():
    return render_template("lesson1.html")

@app.route('/lesson2')
def lesson2():
    return render_template("lesson2.html")

@app.route('/lesson3')
def lesson3():
    return render_template("lesson3.html")

@app.route('/lesson4')
def lesson4():
    return render_template("lesson4.html")

@app.route('/lesson5')
def lesson5():
    return render_template("lesson5.html")

@app.route('/lesson6')
def lesson6():
    return render_template("lesson6.html")

@app.route('/lesson7')
def lesson7():
    return render_template("lesson7.html")

@app.route('/lesson8')
def lesson8():
    return render_template("lesson8.html")

@app.route('/lesson9')
def lesson9():
    return render_template("lesson9.html")

@app.route('/lesson10')
def lesson10():
    return render_template("lesson10.html")

@app.route('/lesson11')
def lesson11():
    return render_template("lesson11.html")

@app.route('/lesson12')
def lesson12():
    return render_template("lesson12.html")

@app.route('/lesson13')
def lesson13():
    return render_template("lesson13.html")

@app.route('/lesson14')
def lesson14():
    return render_template("lesson14.html")

@app.route('/lesson15')
def lesson15():
    return render_template("lesson15.html")

@app.route('/lesson16')
def lesson16():
    return render_template("lesson16.html")


#localhost:5000/user/amit
@app.route('/user/<name>')
def user (name):
     return render_template("user.html", user_name=name)

# Run the application only if this script is the main entry point
#הפעל את היישום רק אם סקריפט זה הוא נקודת הכניסה הראשית
if __name__ == "__main__":
    app.run(debug=True)



