from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form['option']
    r.incr(option)
    return f'Voted for {option}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')


