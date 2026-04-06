import os
from textsummarizer.entity import DataValidationConfig
from textsummarizer.logging import logger
from textsummarizer.constants import *
from textsummarizer.utils.common import read_yaml, create_directories


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            # Use absolute path to the dataset
            dataset_path = PROJECT_ROOT / "artifacts" / "data_ingestion" / "samsum_dataset"

            if not dataset_path.exists():
                validation_status = False
                logger.error(f"Dataset directory not found: {dataset_path}")
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
                return validation_status

            all_files = os.listdir(dataset_path)
            logger.info(f"Found files: {all_files}")
            logger.info(f"Required files: {self.config.ALL_REQUIRED_FILES}")

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    logger.warning(f"File {file} is not in required files")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            logger.info(f"Validation completed. Status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.error(f"Validation error: {str(e)}")
            raise e
