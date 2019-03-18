# Solution to Asia Miles Data Challenge

Currently tested on Python 3.6, Ubuntu 16.04.5

# Guidence of files

model.pkl - model file including Ridge, BayesianRidge, Lasso and XGBoost 

work.ipynb - main work and training code (as reference only)

predict.py - scoring code

evaluate.py - generate evaluation stats


# Guidence of scoring

Step 1. Install python packages

```
pip install -r requirements.txt
```

Step 2. Score test data

```
cat test.csv | python predict.py model.pkl > test_scored.csv
```

Step 3. Evaluate result

```
cat test.csv | python predict.py model.pkl > test_scored.csv | python evaluate.py > stats.log
```
