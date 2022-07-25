from flask import Flask
from flask import render_template

import numpy as np
from scipy import stats

app = Flask(__name__)

""" 
Basic "Hello, World!" get request
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


"""
Python logic demo with scipy descriptive statistics
"""
@app.route("/stats")
def describe_stats():
    names = ["a", "b", "c", "d", "e", "f", "g"]
    # generate random data
    random_data = np.random.rand(100, len(names))
    # add some NaNs
    random_data.ravel()[np.random.choice(random_data.size, 30, replace=False)] = np.nan
    # describe statistics
    data = stats.describe(random_data, axis=0, nan_policy="omit")
    # reorganize data by column and stat for display
    stat_fields = ["nobs", "minmax", "mean", "variance", "skewness", "kurtosis"]
    named_data = dict(zip(stat_fields, data))
    results = dict()
    for idx,field in enumerate(names):
        result = {}
        for stat,arr in named_data.items():
            if stat == "minmax":
                result['min'] = arr[0][idx]
                result['max'] = arr[1][idx]
            else:
                result[stat] = arr[idx]
        results[field] = result
    # build html for return
    html = []
    for field,stat_dict in results.items():
        stat_html = "".join([f"<li><b>{key}</b>: {value}</li>" for key,value in stat_dict.items()])
        html.append(f"<li>{field}<ul>{stat_html}</ul></li>")
    return "<h1>Randomly Generated Descriptive Statistics</h1><ul>" + "".join(html) + "</ul>"


"""
Uses a template instead of writing html in python. Template is located at "templates/sum.html"
"""
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

"""
POST demo for taking input from user and returning sum of 2 numbers.
"""
