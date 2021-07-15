from flask import Flask, request

import db_utils
import email_utils
import git_utils

app = Flask(__name__)


@app.route('/publish', methods=["GET", "POST"])
def publish_to_cloud():
    key = request.json['key']
    msg = email_utils.fetch_raw_email_from_aws(key)
    filepath = '_posts/' + email_utils.fetch_filename(msg)
    post = email_utils.format_post(msg)
    email = email_utils.fetch_from_address(msg)
    repo = db_utils.get_blog_from_email(email)
    git_utils.push_file_to_github(filepath, post, repo)

    return 'Thanks', 200


@app.route('/register', methods=["GET", "POST"])
def register_user():
    key = request.json['key']
    blog = request.json['blog']
    msg = email_utils.fetch_raw_email_from_aws(key)

    email = email_utils.fetch_from_address(msg)
    db_utils.register_user(email, blog)
    git_utils.update_template(blog)

    return 'Registered', 200


if __name__ == '__main__':
    app.run()
