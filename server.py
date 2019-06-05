from flask import Flask, render_template
app = Flask(__name__)
import script

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/fortune')
def print_reading():
    script.print_reading()
    print('should have printed reading')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
