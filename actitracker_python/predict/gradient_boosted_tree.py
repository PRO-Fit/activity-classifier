from sklearn.externals import joblib
import pandas as pd

from util.constants import MODEL_FILE
from util import predict_helper as helper
from data.actitracker_data import ActitrackerData as db


class GradientBoostedPredictor(object):
    def __init__(self):
        self.classifier = joblib.load(MODEL_FILE)

    def fetch_predict_load_activities(self):
        user_activities = self.predict_activities()
        for user_activity in user_activities:
            db.insert_activity(user_activity)

    def predict_activities(self):
        records = db.get_records_to_predict(helper.last_read())
        helper.write_last_read()
        user_activities = []
        for record in records:
            user_activities.append({
                'user_id': record.pop('user_id'),
                'distance': round(float(record.pop('distance')), 2),
                'start_datetime': int(record['start_timestamp']),
                'end_datetime': int(record.pop('start_timestamp')) + 5000,
                'workout_type_id': int(float(self.classifier.predict(pd.DataFrame(record, index=[0]))[0]))
            })
        return user_activities
