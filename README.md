Solution to Asia Miles Data Challenge
=========================

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
