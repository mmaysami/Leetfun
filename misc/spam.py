# """
# Build Spam Classifier  [MS]
# """

import numpy as np
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score, roc_auc_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC


def spam_detector(train_df, valid_df, test_df):
    tfidf_vect = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        # max_df=1,
        strip_accents='unicode',
        use_idf=True,
        smooth_idf=True,
        # sublinear_tf=True
    )

    # Fit on Train or Train+Valid
    # tfidf_vect.fit(np.concatenate([train_df['text'], valid_df['text']]))
    tfidf_vect.fit(train_df['text'])

    X_train = tfidf_vect.transform(train_df['text'])
    X_valid = tfidf_vect.transform(valid_df['text'])
    X_test = tfidf_vect.transform(test_df['text'])

    # Make Spam Class =1
    y_train = train_df['label'].values
    y_valid = valid_df['label'].values
    y_test = test_df['label'].values

    # Set Candid Model Parameters
    dict_models = {
        'LogisticRegression': LogisticRegression(random_state=0),
        'MultinomialNB': MultinomialNB(),
        'DecisionTreClassifier': DecisionTreeClassifier(max_depth=4, criterion='entropy', random_state=0),
        'LinearSVC': LinearSVC(),
    }

    # Loop over Classifier Choices and Pick Best
    best_score = -1
    conf_matrix = {}
    for model in dict_models.keys():
        clf = dict_models[model]
        # eval_set=[(X_train, y_train), (X_valid, y_valid)]
        clf.fit(X_train, y_train)
        clf_score_valid = roc_auc_score(y_valid, clf.predict(X_valid))
        if clf_score_valid > best_score:
            best_clf = model

        conf_matrix[model] = confusion_matrix(y_valid, clf.predict(X_valid))

    # Predict Test Cases
    y_pred = dict_models[best_clf].predict(X_test)

    # Form Result Dictionary
    results = {
        "LogisticRegression": conf_matrix['LogisticRegression'],
        "MultinomialNB": conf_matrix['MultinomialNB'],
        "DecisionTreeClassifier": conf_matrix['DecisionTreClassifier'],
        "LinearSVC": conf_matrix['LinearSVC'],
        "BestClassifier": best_clf,
        "TfidfVectorizer": X_test,
        "Prediction": y_pred
    }
    return results


# ================================================================================
#   Tests
# ================================================================================
from os.path import abspath, join, dirname
folder_data = abspath(join(dirname(__file__), '..', 'data'))

spam_detector(
    pd.read_csv(join(folder_data, 'train.csv')),
    pd.read_csv(join(folder_data, 'valid.csv')),
    pd.read_csv(join(folder_data, 'test.csv'))
)
