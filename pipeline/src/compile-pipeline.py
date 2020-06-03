import kfp.compiler as compiler
from kfp import Client as KfpClient
import pipeline
from google.cloud import storage
import os

from argparse import ArgumentParser

pipeline_filename = 'pipeline.tar.gz'

def compile():
    pipeline_func = pipeline.preprocessing_pl

    compiler.Compiler().compile(pipeline_func, pipeline_filename)

def upload(destination):
    uri = destination[5:]
    uri_parts = uri.split("/")
    bucket_name = uri_parts[0]
    source_blob_name = "/".join(uri_parts[1:])

    blob = storage.Client().bucket(bucket_name).blob("/".join(uri_parts[1:]))
    blob.upload_from_filename(pipeline_filename)

    # client = KfpClient(
    #     host="https://kubeflow-oct.endpoints.myfirstproject-226013.cloud.goog/pipeline",
    #     client_id="478111835512-94l3kca44ueiudgm9tr2ibg4ihah5g3d.apps.googleusercontent.com",
    #     namespace='kubeflow-aniftos'
    # );
    # client.create_run_from_pipeline_package(pipeline_file=pipeline_filename, arguments={
    #     'data-path': 'gs://kubeflow_pipelines_sentiment/data/test.csv',
    #     'vectorizer-gcs-location': 'gs://kubeflow_pipelines_sentiment/assets/x.pkl'}, run_name=None,
    #                                         experiment_name=None)
    #


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--dest",
                        dest="destination",
                        help="gs:// path to export pipeline including the archived name and extension")

    args = parser.parse_args()

    compile()
    upload(args.destination)
