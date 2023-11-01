## create Pipeline
from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.Model_Evaluation import ModelEvaluation
from src.TextSummarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.evaluate()