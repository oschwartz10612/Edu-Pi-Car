from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello(name=None):
    return render_template('index.html')

@socketio.on('left')
def left():
    #code to turn left
    print('left')

@socketio.on('right')
def right():
    #code to turn right
    print('right')

@socketio.on('up')
def up():
    #code to drive forward
    print('up')

@socketio.on('down')
def down():
    #code to drive backward
    print('down')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
