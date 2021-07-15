import email
import uuid
from email import policy

import requests
from dateutil.parser import parse

BASE_URL = 'https://internetblog.s3.amazonaws.com/post/'
POST_METADATA = '---\nlayout: post\ntitle:  "{title}"\n---\n'


def fetch_raw_email_from_aws(key):
    url = BASE_URL + key
    r = requests.get(url)

    msg = email.message_from_bytes(r.content, policy=policy.default)
    return msg


def fetch_post_body_html(msg):
    body = msg.get_body(preferencelist=('html', 'plain'))
    # Remove the Content-Type: text/html; charset="UTF-8" parts
    return body.as_string().split('\n', 1)[1]


def fetch_post_title(msg):
    return msg['subject']


def fetch_post_timestamp(msg):
    date = msg['date']
    return parse(date)


def fetch_from_address(msg):
    # Extract email from 'Advait Raykar <advait.raykar@gmail.com>'
    return msg['from'].split('<')[-1][:-1]


def fetch_to_address(msg):
    return msg['to']


def format_post(msg):
    title = fetch_post_title(msg)
    body = fetch_post_body_html(msg)
    post = POST_METADATA.format(title=title) + body
    return post


def fetch_filename(msg):
    post_uuid = uuid.uuid4().__str__()
    timestamp = fetch_post_timestamp(msg)
    filename = timestamp.strftime('%d-%m-%y-') + post_uuid + '.md'
    return filename
