import kfp;
import argparse;
import json;

def run_exp(pipeline_name,
            pipeline_archive,
            experiment_name=None,
            run_name=None,
            pipeline_args=None,
            kfp_namespace="kubeflow"):

    client=kfp.Client(namespace=kfp_namespace);

    # client.upload_pipeline(
    #     pipeline_package_path=pipeline_archive,
    #     pipeline_name=pipeline_name);

    run = client.create_run_from_pipeline_package(
        arguments=pipeline_args,
        run_name=run_name,
        experiment_name=experiment_name,
        pipeline_file=pipeline_archive);

    response = client.wait_for_run_completion(run_id=run.run_id, timeout=560)
    if response.run.error != None:
        print(response.run.error)
        raise RuntimeError("Execution of run {} failed. Please check kubeflow pipelines for details".format(run.run_id))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Input Arguments
    parser.add_argument(
        '--pipeline_name',
        help='pipeline_name',
        type=str,
        required=True
    )
    parser.add_argument(
        '--pipeline_archive',
        help='pipeline_archive',
        type=str,
        required=True
    )
    parser.add_argument(
        '--experiment_name',
        help='experiment_name',
        type=str,
        required=False,
        default=None
    )
    parser.add_argument(
        '--run_name',
        help='run_name',
        type=str,
        required=False,
        default=None
    )
    parser.add_argument(
        '--pipeline_args',
        help='pipeline_args',
        type=str,
        required=False,
        default=None
    )
    parser.add_argument(
        '--kfp_namespace',
        help='kfp_namespace',
        type=str,
        required=False,
        default="kubeflow"
    )

    args = parser.parse_args()
    arguments = args.__dict__

    arguments['pipeline_args'] = json.loads(arguments['pipeline_args'])

    run_exp(arguments['pipeline_name'],
            arguments['pipeline_archive'],
            arguments['experiment_name'],
            arguments['run_name'],
            arguments['pipeline_args'],
            arguments['kfp_namespace'])