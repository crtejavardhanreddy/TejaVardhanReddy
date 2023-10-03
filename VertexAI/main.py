# from google.cloud import vertexai.preview
import google.cloud.aiplatform as aiplatform

dataset = aiplatform.TextDataset(
    name= 'my_dataset',
    gcs_source = 'gs://my-bucket/my-dataset'
)

training_pipeline = aiplatform.PipelineJob(
    name = "my_training_pipeline",
    dataset = dataset,
    model_to_train = 'my_model',
    training_task_defination = aiplatform.CustomTrainingJob()
)

training_pipeline.run()