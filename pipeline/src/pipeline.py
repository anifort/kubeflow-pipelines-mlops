import kfp
import kfp.dsl as dsl
import kfp.gcp as gcp
import os


dname = os.path.dirname( os.path.abspath(__file__))

# Initialize component store
component_store = kfp.components.ComponentStore(local_search_paths=[dname+'/../../component'])

# Create component factories
tfidfvec_op = component_store.load_component('tfidf-vectoriser')

# Define pipeline
@dsl.pipeline(
  name='A Simple CI pipeline',
  description=''
)
def preprocessing_pl(
  data_path: str="gs://kubeflow_pipelines_sentiment/data/test.csv",
  vectorizer_gcs_location: str="gs://kubeflow_pipelines_sentiment/assets/x.pkl"
):
  tfidfvec_step = tfidfvec_op(data_path=data_path, vectorizer_gcs_location=vectorizer_gcs_location).apply(gcp.use_gcp_secret('user-gcp-sa')) # We do not define output local file, that is auto-generated.
  tfidfvec_step.set_display_name('vectorizing')
  tfidfvec_step.outputs['local_output']


  '''with kfp.dsl.Condition(sum_value != 0):
    divide_step = divide_op(x_value=sum_value, y_value=z_value)
    divide_step.set_display_name('Divide sum by z')
    add_step2 = add_op(
      x_value=divide_step.outputs['quotient'],
      y_value=divide_step.outputs['remainder'])
    add_step2.set_display_name('Add quotient and remainder')
  '''


'''
pipeline_func = preprocessing_pl
pipeline_filename = pipeline_func.__name__ + '.zip'


import kfp.compiler as compiler
compiler.Compiler().compile(pipeline_func, pipeline_filename)
'''
# dsl-compile --py pipeline.py --output pipeline_build.tar.gz
