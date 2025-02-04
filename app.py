from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""

    return (
        	"""<h2> It's a simple web app! 🦊 </h2>"""
		"""<br>"""
		"""<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
            </form>"""
        + "Fahrenheit: "
        + '<a id="fahrenheit">' +fahrenheit+ '</a>'

    )
 
@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3) 
    return str(fahrenheit)

@app.route("/<string:script>")
def run(script):
    script=request.args.get("script", "")
    return (
	"""<h2> Run! 🕸 </h2>"""
	"""<form action="" method="get">
                <input type="text" name="script">
                <input type="submit" value="Run">
            </form>"""
    + '<a id="script">' + script + '</a>'
) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
