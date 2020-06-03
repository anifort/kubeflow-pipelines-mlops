from kfp import Client as KfpClient
import pipeline


client=KfpClient(
    host="https://kubeflow-oct.endpoints.myfirstproject-226013.cloud.goog/pipeline",
    client_id="478111835512-94l3kca44ueiudgm9tr2ibg4ihah5g3d.apps.googleusercontent.com");

client.create_pipeline_version(
    pipeline_id="1234",
    name="$COMMIT_SHA",
    repo_name="$REPO_NAME",
    commit_sha="$COMMIT_SHA",
    url="https://storage.googleapis.com/$REPO_NAME/$COMMIT_SHA/pipeline.zip")

''' 
client = KfpClient(
     host="https://kubeflow-oct.endpoints.myfirstproject-226013.cloud.goog/pipeline",
     client_id="478111835512-94l3kca44ueiudgm9tr2ibg4ihah5g3d.apps.googleusercontent.com"
)

pipeline_func = pipeline.preprocessing_pl

client.create_run_from_pipeline_func(
    pipeline_func=pipeline_func,
    arguments={'data_path': 'gs://kubeflow_pipelines_sentiment/data/test.csv',
               'vectorizer_gcs_location': 'gs://kubeflow_pipelines_sentiment/assets/x.pkl'},
    experiment_name='test2',
    run_name='001'

)'''