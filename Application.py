from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
      app.run(debug=True)

@app.route("/")
def index():
      headline = "Python - First page"
      return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
      headline = "Python - Goodbye!!"
      return render_template("index.html", headline = headline)

@app.route("/more")
def more():
      headline = "Python - More page"
      return render_template("more.html", headline = headline)
      
@app.route("/<string:name>")
def hello(name):
      name = name.capitalize()
      return f"Hello, {name}!"
      
      
      