import sqlite3


def reg_account(login, password):
    con = sqlite3.connect("usersctf.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT id FROM users
                WHERE username == "{login}" """).fetchall()
    if result:
        con.close()
        return False
    cur.execute("INSERT INTO users (username, password, is_banned, score) VALUES (?, ?, ?, ?)",
                (login, password, False, 0))

    con.commit()
    con.close()
    return True


def login_user(login, user_password):
    con = sqlite3.connect("usersctf.db")
    cur = con.cursor()
    result = cur.execute("""SELECT id FROM users
                            WHERE username = ? AND password = ?""", (login, user_password)).fetchall()

    if result:
        con.close()
        return result[0][0]
    con.close()
    return False


def anti_sqli(name, password):
    to_check = str(name + password)
    if len(to_check) != len((to_check.replace("\"", "")).replace("\'", "")):
        return False
    return True
