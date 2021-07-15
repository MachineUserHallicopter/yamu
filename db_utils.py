import sqlite3

DB_FILE = "internetblogs.db"


def init_db():
    # create a database named backup
    cnt = sqlite3.connect(DB_FILE)
    cnt.execute('CREATE TABLE users(BLOG TEXT, EMAIL TEXT);')


def create_connection(db_file=DB_FILE):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


def get_blog_from_email(email):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT blog FROM users WHERE email = ?", (email,))
    blog = cur.fetchall()[0]

    return blog[0]


def register_user(email, blog):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users(blog, email) VALUES(?, ?)', (blog, email))
    conn.commit()
    return cur.lastrowid
