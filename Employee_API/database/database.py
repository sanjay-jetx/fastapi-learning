import sqlite3


def get_db():
    return sqlite3.connect("test1.db",check_same_thread=False)

def init_db():
    conn=get_db()
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists employees(
                emp_id integer primary key ,
                Name text not null,
                Age int not null,
                role text,
                salary Real
        )
        ''')
    conn.commit()
    conn.close()