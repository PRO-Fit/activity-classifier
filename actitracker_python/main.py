from model.random_forest import RandomForestModel
from model.extreme_tree import ExtremeTreeModel
from model.gradient_boosted_tree import GradientBoostedModel

if __name__ == "__main__":
    rf = RandomForestModel()
    rf.train_model()
    print "Random Forest 10 fold validation: ", rf.get_n_fold_validation_score()
    print "Random Forest: " + str(rf.accuracy)

    # et = ExtremeTreeModel()
    # et.train_model()
    # print "Extreme Tree 10 fold validation: ", et.get_n_fold_validation_score()
    # print "Extreme Tree: " + str(et.accuracy)
    #
    gb = GradientBoostedModel()
    gb.train_model()
    # print gb.accuracy
    print "Gradient Boosted Tree - 10 fold validation: ", gb.get_n_fold_validation_score()
    print "Gradient Boosted Tree - Holdout set: ", gb.accuracy
