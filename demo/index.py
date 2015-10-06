from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("second.html")

@app.route('/show_data', methods=["GET", "POST"])
def show_data():
    Madical_name = request.form['Madical_name']
    Unit_price = request.form['Unit_price']
    Quantity = request.form['Quantity']
    Cost = request.form['Cost']
    print Madical_name,Unit_price,Quantity,Cost
    return render_template('show_user.html', Madical_name=Madical_name,Unit_price=Unit_price,Quantity=Quantity,Cost=Cost)

if __name__ == "__main__":
    app.run()
