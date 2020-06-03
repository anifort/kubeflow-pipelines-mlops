from vectorizer.Vectorizer import Vectorizer
import argparse, os, json
from pathlib import Path

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Input Arguments
    parser.add_argument(
        '--train_data_path',
        help='GCS or local path to training data',
        type=str,
        required=True
    )
    parser.add_argument(
        '--vectorizer_output',
        help='Location to output vectoriser',
        type=str,
        required=True
    )
    parser.add_argument(
        '--local_out',
        help='Location to output vectoriser',
        type=str,
        required=True
    )



    args = parser.parse_args()
    arguments = args.__dict__


    Vectorizer(arguments['train_data_path'], arguments['vectorizer_output'])

    Path(arguments['local_out']).parent.mkdir(parents=True, exist_ok=True)
    Path(arguments['local_out']).write_text(arguments['vectorizer_output'])

    metadata = {
        'outputs': [
            # Markdown that is hardcoded inline
            {
                'storage': 'inline',
                'source': '# Inline Markdown\n[A link](https://www.kubeflow.org/)',
                'type': 'markdown',
            }]
    }
    with open('/mlpipeline-ui-metadata.json', 'w') as f:
        json.dump(metadata, f)