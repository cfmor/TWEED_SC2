from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor

import numpy as np

def svm_model(X_train, y_train, X_test, y_test): 
     #%% Define the SVM pipeline and parameters for RandomizedSearchCV
    SVM_pipe = Pipeline([('scaler', StandardScaler()), 
                    ('svm', SVR())])

    SVM_parameters = {"svm__C": np.logspace(-6, 10,17), 
                    "svm__kernel": ["linear", "rbf"],
                    "svm__gamma": ["scale", "auto"]}

    SVM_pipe = RandomizedSearchCV(SVM_pipe, 
                        SVM_parameters, 
                        scoring="neg_mean_absolute_error", 
                        n_jobs=4,
                        n_iter=5,      
                        cv=5,
                        random_state=42,
                        verbose = 3)

    SVM_pipe.fit(X_train, y_train)
    # SVM_pipe_df = pd.DataFrame(SVM_pipe.cv_results_)

    target_SVM = SVM_pipe.predict(X_test)
    # print("MAE for SVM: ", parameter_metrics(y_test, target_SVM))

    return target_SVM, SVM_pipe



def NN_model(X_train, y_train, X_test, y_test):

    #%% Define the NN pipeline and parameters for RandomizedSearchCV
    NN_pipe = Pipeline([('scaler', StandardScaler()), 
                    ('NN', MLPRegressor())])

    NN_parameters = {"NN__hidden_layer_sizes": [(100,), (50, 50), (100, 50), (100, 100)],
                    "NN__activation": ["relu", "tanh"],
                    "NN__solver": ["adam", "lbfgs"],
                    "NN__alpha": np.logspace(-6, -1, 6),
                    "NN__learning_rate": ["constant", "adaptive"]}

    NN_pipe = RandomizedSearchCV(NN_pipe, 
                        NN_parameters, 
                        scoring="neg_mean_absolute_error", 
                        n_jobs=4,
                        n_iter=20,      
                        cv=5,
                        random_state=42, 
                        verbose = 2)

    NN_pipe.fit(X_train, y_train)
    # NN_pipe_df = pd.DataFrame(NN_pipe.cv_results_)

    target_NN = NN_pipe.predict(X_test)
    # print("MAE for NN: ", metrics(y_test, target_NN))

    return target_NN, NN_pipe