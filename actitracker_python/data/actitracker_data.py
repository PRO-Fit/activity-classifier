import mysql.connector as mysql
import pandas as pd


class ActitrackerData:
    @staticmethod
    def get_conn(database):
        conn = None
        try:
            conn = mysql.connect(user='root', password='admin', host='localhost', database=database)
        except mysql.connector.Error as err:
            print(err)
            conn.close()
        return conn

    @staticmethod
    def get_features():
        conn = ActitrackerData.get_conn('actitracker')
        cursor = conn.cursor()

        query = """SELECT
                      mean0,
                      mean1,
                      mean2,
                      variance0,
                      variance1,
                      variance2,
                      avgabsdiff0,
                      avgabsdiff1,
                      avgabsdiff2,
                      resultant,
                      avgtimepeak
                   FROM
                      activity_with_features_3"""

        cursor.execute(query)
        columns = tuple([d[0].decode('utf8') for d in cursor.description])
        records = []
        for record in cursor:
            records.append(dict(zip(columns, record)))

        data = pd.DataFrame(records)
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def get_lables():
        conn = ActitrackerData.get_conn('actitracker')
        cursor = conn.cursor()

        lable_query = """SELECT
                            lable
                         FROM
                            activity_with_features_3"""

        cursor.execute(lable_query)
        columns = tuple([d[0].decode('utf8') for d in cursor.description])
        lables = []
        for lable in cursor:
            lables.append(dict(zip(columns, lable)))

        lable_data = pd.DataFrame(lables)
        cursor.close()
        conn.close()
        return lable_data

    @staticmethod
    def get_records_to_predict(last_read):
        conn = ActitrackerData.get_conn('profit')
        cursor = conn.cursor()

        query = """SELECT user_id,
                        mean0,
                        mean1,
                        mean2,
                        variance0,
                        variance1,
                        variance2,
                        avgabsdiff0,
                        avgabsdiff1,
                        avgabsdiff2,
                        resultant,
                        avgtimepeak,
                        distance,
                        start_timestamp
                  FROM t_user_activity_features
                  WHERE start_timestamp >= %s""" % last_read

        cursor.execute(query)
        columns = tuple([d[0].decode('utf8') for d in cursor.description])
        records = []
        for record in cursor:
            records.append(dict(zip(columns, record)))

        cursor.close()
        conn.close()
        return records

    @staticmethod
    def insert_activity(user_activity):
        conn = ActitrackerData.get_conn('profit')
        cursor = conn.cursor()

        query = ("""INSERT INTO t_user_activity
                            (user_id,
                            workout_type_id,
                            distance,
                            start_datetime,
                            end_datetime)
                         VALUES
                            (%(user_id)s,
                            %(workout_type_id)s,
                            %(distance)s,
                            %(start_datetime)s,
                            %(end_datetime)s)""")
        cursor.execute(query, user_activity)
        conn.commit()
        cursor.close()
        conn.close()
