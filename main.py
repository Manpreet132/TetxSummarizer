from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Name"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e