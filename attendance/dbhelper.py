import sqlite3
import configparser
from models import Student



class Dbapi(object):

    __connection = None
    __cursor = None
    __DBNAME = None
    __TABLE_NAME = None
    __COLUMN_LNAME = None
    __COLUMN_FNAME = None
    __COLUMN_MATRIC = None
    __COLUMN_UID = None

    @classmethod
    def configure(cls):
        cls.__update();

    @classmethod
    def set_config(cls,dbname,tbname,col_last_name,col_first_name,col_matric, col_uid,port="/dev/ttyUSB0"):
        conf = configparser.ConfigParser()
        conf.add_section("Database")
        conf.set("Database", "db_name", dbname)
        conf.set("Database", "table_name", tbname)
        conf.set("Database", "col_last_name",col_last_name)
        conf.set("Database", "col_first_name",col_first_name)
        conf.set("Database", "col_matric",col_matric)
        conf.set("Database", "col_uid", col_uid)
        conf.add_section("Arduino")
        conf.set("Arduino","port",port)

        with open("dbconfig.ini","wb") as configfile:
            conf.write(configfile)



    @classmethod
    def __update(cls):
        config = configparser.ConfigParser()
        config.read("dbconfig.ini")
        dbsection = config["Database"]
        cls.__DBNAME = dbsection.get("db_name","StudentsDb.sqlite")
        cls.__TABLE_NAME = dbsection.get("table_name","Students").replace(' ', '_')
        cls.__COLUMN_LNAME = dbsection.get("col_last_name","Last Name").replace(' ', '_')
        cls.__COLUMN_FNAME = dbsection.get("col_first_name","First Name").replace(' ', '_')
        cls.__COLUMN_MATRIC = dbsection.get("col_matric","Matric Number").replace(' ', '_')
        cls.__COLUMN_UID = dbsection.get("col_uid","UID").replace(' ', '_')
        cls.__make_conn()
        cls.__create_table()


    @classmethod
    def __create_table(cls):
        query_string = "CREATE TABLE IF NOT EXISTS %s (%s TEXT PRIMARY KEY NOT NULL," \
                       "%s TEXT NOT NULL," \
                       "%s TEXT NOT NULL," \
                       "%s TEXT UNIQUE NOT NULL);"%(cls.__TABLE_NAME,
                                           cls.__COLUMN_UID,
                                           cls.__COLUMN_LNAME,
                                           cls.__COLUMN_FNAME,
                                           cls.__COLUMN_MATRIC)
        cls.__cursor.execute(query_string)
        cls.__connection.close()

    @classmethod
    def __make_conn(cls):
        cls.__connection = sqlite3.connect(cls.__DBNAME)
        cls.__cursor = cls.__connection.cursor()

    @classmethod
    def fetch_students(cls):
        cls.__make_conn()
        students = []
        rows = cls.__cursor.execute("SELECT * FROM %s;"%cls.__TABLE_NAME)
        for row in rows:
            students.append(Student(*row))
        cls.__connection.close()
        return students


    @classmethod
    def get_student_by_uid(cls,uid):
        cls.__make_conn()
        query_string = "SELECT * FROM %s WHERE %s=?;"%(cls.__TABLE_NAME,cls.__COLUMN_UID)
        curs = cls.__cursor.execute(query_string,(uid,))
        a = curs.fetchone()
        if a:
            student = Student(*a)
            cls.__connection.close()
            return student
        return None

    @classmethod
    def register_student(cls,student):
        cls.__make_conn()
        cls.__cursor.execute("INSERT INTO %s (%s,%s,%s,%s) VALUES(?,?,?,?);" % (cls.__TABLE_NAME,
                                                                              cls.__COLUMN_UID,
                                                                              cls.__COLUMN_LNAME,
                                                                              cls.__COLUMN_FNAME,
                                                                              cls.__COLUMN_MATRIC),
                       (
                           student.uid,
                           student.last_name,
                           student.first_name,
                           student.matric_number
                       ))
        cls.__connection.commit()
        cls.__connection.close()
        return "success"


    @classmethod
    def unregister_student(cls,uid):
        cls.__make_conn()
        cls.__cursor.execute("DELETE FROM %s WHERE %s=?;"%(cls.__TABLE_NAME,
                                                           cls.__COLUMN_UID),(uid,))
        cls.__connection.commit()
        cls.__connection.close()