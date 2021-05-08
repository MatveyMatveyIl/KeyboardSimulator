try:
    import sqlite3
    import sys
except Exception as e:
    print('Modules not found: "{}". Try reinstalling the app.'.format(e))
    sys.exit(4)

db = sqlite3.connect('user.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS user_results(
    datetime TEXT,
    wpm BIGINT,
    cpm BIGINT,
    errors BIGINT
)""")
db.commit()


def save_results(date, new_wpm, new_cpm, new_errors):
    sql.execute("SELECT datetime FROM user_results")
    if sql.fetchone() is None:
        sql.execute("""INSERT INTO user_results VALUES (?, ?, ?, ?)""", (date, new_wpm, new_cpm, new_errors))
        db.commit()
    else:
        for old_wpm in sql.execute(f"SELECT wpm FROM user_results WHERE datetime = '{date}'"):
            sql.execute(f"UPDATE user_results SET wpm = {(old_wpm[0] + new_wpm) // 2} WHERE datetime = '{date}'")
            db.commit()
        for old_cpm in sql.execute(f"SELECT cpm FROM user_results WHERE datetime = '{date}'"):
            sql.execute(f"UPDATE user_results SET cpm = {(old_cpm[0] + new_cpm) // 2} WHERE datetime = '{date}'")
            db.commit()
        for old_errors in sql.execute(f"SELECT errors FROM user_results WHERE datetime = '{date}'"):
            sql.execute(f"UPDATE user_results SET errors = {(old_errors[0] + new_errors) // 2} WHERE datetime = '{date}'")
            db.commit()


def take_results():
    results = []
    for result in sql.execute('SELECT * FROM user_results'):
        results.append(result)

    return results

save_results('t', 1, 1, 1)
for result in sql.execute('SELECT * FROM user_results'):
        print(result)