from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lis')
def lis():
    return render_template('lis.html')

@app.route('/zeb')
def zeb():
    return render_template('zeb.html')

@app.route('/lama')
def lama():
    return render_template('lama.html')

@app.route('/zubr')
def zubr():
    return render_template('zubr.html')

@app.route('/capuz')
def capuz():
    return render_template('capuz.html')

@app.route('/enot')
def enot():
    return render_template('enot.html')

@app.route('/tapir')
def tapir():
    return render_template('tapir.html')

@app.route('/lev')
def lev():
    return render_template('lev.html')

@app.route('/raf')
def raf():
    return render_template('raf.html')

@app.route('/ozoo')
def ozoo():
    return render_template('ozoo.html')




if __name__ == '__main__':
    app.run(debug=True)