from src.TextSummarizer.logging import logger
# logger.info("Welcome to our custom log")
from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

except Exception as e:
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

except Exception as e:
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

except Exception as e:
    raise e

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_traner = ModelTrainerTrainingPipeline()
    model_traner.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

except Exception as e:
    raise e

STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")

except Exception as e:
    raise e