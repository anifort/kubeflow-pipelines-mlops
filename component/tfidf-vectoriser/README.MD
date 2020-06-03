##### Running tests
You can  run test from project root using : 
```terminal
$ python -m unittest
OR
$ python -m unittest discover

```

For this to work you need to have:
1) empty \_\_init\_\_.py file in your tests folder
2) your tests files start with test_



to run coverage:
```terminal
$ coverage run -m unittest discover
$ coverage html --omit="*/venv*,*/tests/*" -d tmp/coverage

$ coverage report -m --omit="*/venv*,*/tests/*" --fail-under 75 // returns exit code 2 if condition is not met

$ coverage erase
 
OR using nosetests

$ nosetests 

OR 

>> This runs both tests and coverage test. See setup.cfg
$ python setup.py nosetests

```

docker build -f ./Dockerfile -t gcr.io/myfirstproject-226013/kubeflow_pipelines_sentiment:v1 ./

!docker push $IMAGE_URI

docker run 10429779fa62 ./run_tests.sh

docker run 10429779fa62 /app/run_tests.sh

docker run 10429779fa62 python /app/src/main.py

docker run 77d99f1f3263 python /app/src/main.py --train_data_paths gs://kubeflow_pipelines_sentiment/data/test.csv --trained_vectorizer_output gs://kubeflow_pipelines_sentiment/assets/v.pkl 


### To run component locally:
```bash 
$ python main.py --train_data_paths test.csv --vectorizer_output gs://kubeflow_pipelines_sentiment/assets/x.pkl --local_out out.txt
```