from flask import Flask, jsonify, Response, current_app
import threading
import time

app = Flask(__name__)

def background_thread():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        message = {'count': count, 'data': 'Some data from the background thread'}
        with app.app_context():
            current_app._eventlet.queue.append(message)

@app.route('/sse')
def sse():
    def generate():
        while True:
            message = current_app._eventlet.queue.get()
            if message:
                yield f"data: {jsonify(message)}\n\n"
            else:
                time.sleep(1)

    return Response(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'

    # Start the background thread
    thread = threading.Thread(target=background_thread)
    thread.start()

    # Run the application with the built-in development server
    app.run(threaded=True, use_reloader=False)
