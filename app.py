from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/yarn')
def yarn():
    return render_template('yarn.html')

@app.route('/production')
def production():
    return render_template('production.html')

@app.route('/defect')
def defect():
    return render_template('defect.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



