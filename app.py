from flask import Flask, request

app = Flask(__name__)


@app.route('/publish', methods=["GET", "POST"])
def publish_to_cloud():
    return request.json


if __name__ == '__main__':
    app.run()
