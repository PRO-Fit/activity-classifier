import logging

from model.gradient_boosted_tree import GradientBoostedModel
from predict.gradient_boosted_tree import GradientBoostedPredictor
from util import predict_helper as helper

if __name__ == "__main__":
    # gb = GradientBoostedModel()
    # gb.train_model()
    model = GradientBoostedPredictor()
    model.fetch_predict_load_activities()
