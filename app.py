from flask import Flask, render_template, request
from costCalculator import totalCost
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/form_demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'POST':
        adults = int(request.form['numAdults'])
        children = int(request.form['numChildren'])
        total = totalCost(adults, children)
        return render_template('result.html',
                               adults=adults,
                               children=children,
                               total=total)
    return render_template('form_demo.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

#@app.route('/test')
#def test():  # put application's code here
#    return 'test'

#@app.route('/purchase')
#def purchase():  # put application's code here
#    return 'item purchased'

#@app.route('/html')
#def html():  # put application's code here
#    return '<html> <h1> Heading <\h1> normal <html>'

#@app.route('/info')
#def info1():  # put application's code here
#    return render_template('info.html')

if __name__ == '__main__':
    app.run()



