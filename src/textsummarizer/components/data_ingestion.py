from dataclasses import dataclass
import os
from pathlib import Path
import zipfile
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size
import urllib.request as request


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Ensure parent directory exists
            Path(self.config.local_data_file).parent.mkdir(
                parents=True, exist_ok=True)

            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(
                f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        # Convert to absolute path to avoid Windows relative path issues
        unzip_path = Path(self.config.unzip_dir).resolve()
        unzip_path.mkdir(parents=True, exist_ok=True)

        # Convert paths to strings for zipfile
        with zipfile.ZipFile(str(self.config.local_data_file), 'r') as zip_ref:
            zip_ref.extractall(str(unzip_path))

        logger.info(f"Dataset extracted to {unzip_path}")
