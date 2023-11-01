## create Pipeline
from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.Data_Transformation import DataTransformation
from src.TextSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()   