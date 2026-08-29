from flask import flask, render_template, request, redirect, url_for    

app = flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    units = int(request.form['units'])
    bill = units * 5
    
    if units < 100:
        message='great! you are an energy saver'
    elif units < 700:
        message='not bad! try to save more energy'
    else:
        message='woha! time to switch offf some lights!'
        
    return render_template('success.html', units=units, bill=bill, message=message)
if __name__ == '__main__':
    app.run(debug=True)