import sqlite3

def connect_db():
    return sqlite3.connect("expenses.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    # Expenses (now supports users & groups)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        group_id INTEGER,
        amount REAL,
        category TEXT,
        date TEXT,
        month TEXT
    )
    """)

    # Budgets PER MONTH
    cur.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        category TEXT,
        month TEXT,
        budget REAL
    )
    """)

    # Users
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    # Groups (Splitwise-style)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT
    )
    """)

    # Group Members
    cur.execute("""
    CREATE TABLE IF NOT EXISTS group_members (
        group_id INTEGER,
        user_email TEXT
    )
    """)

    conn.commit()
    conn.close()

# ------------------ USER ------------------
def add_user(name, email):
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO users VALUES (?,?)", (email, name))
    con.commit()
    con.close()

# ------------------ EXPENSE ------------------
def add_expense(user, group_id, amount, category, date, month):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
    INSERT INTO expenses (user_email, group_id, amount, category, date, month)
    VALUES (?,?,?,?,?,?)
    """, (user, group_id, amount, category, date, month))
    con.commit()
    con.close()

def get_category_spending(user, month):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    WHERE user_email=? AND month=?
    GROUP BY category
    """, (user, month))
    data = cur.fetchall()
    con.close()
    return data

# ------------------ BUDGET ------------------
def set_budget(user, category, month, budget):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
    INSERT INTO budgets (user_email, category, month, budget)
    VALUES (?,?,?,?)
    """, (user, category, month, budget))
    con.commit()
    con.close()

def get_budget(user, category, month):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
    SELECT budget FROM budgets
    WHERE user_email=? AND category=? AND month=?
    """, (user, category, month))
    row = cur.fetchone()
    con.close()
    return row[0] if row else 0

# ------------------ GROUPS ------------------
def create_group(name):
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO groups (group_name) VALUES (?)", (name,))
    con.commit()
    gid = cur.lastrowid
    con.close()
    return gid

def add_member(group_id, email):
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO group_members VALUES (?,?)", (group_id, email))
    con.commit()
    con.close()
