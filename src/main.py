"""
The main script of ETL pipeline
"""
import os
import sys
import logging

# Add src diectory to Python import path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# import modules
from config.config import API_BASE_URL, BASE_CURRENCY, LOG_LEVEL
from extract.api_client import fetch_exchange_rates, validate_api_response
# future imports:
# from transform.data_processor import process_rates
# from load.file_writer import save_to_csv

# Configure logging
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_etl():
    """
    main ETL pipeline function
    """
    logger.info("Starting ETL pipeline")

    try:
        # extract
        logger.info(f"Extracting data from {API_BASE_URL}")
        logger.info(f"Base currency: {BASE_CURRENCY}")
        
        raw_data = fetch_exchange_rates(BASE_CURRENCY)

        # Check if extraction was sucessful
        if raw_data is None:
            logger.error("Data extraction failed - stopping pipeline")
            return None

        # Validate API response structure
        if not validate_api_response(raw_data):
            logger.error("API response validation failed - stopping pipeline")
            return None

        logger.info(f"Extracted data for {len(raw_data.get('rates', {}))} currencies")

        # transform
        logger.info(f"Transforming data")
        # processed_data = process_rates(raw_data)
        processed_data = raw_data # Temporary

        # load
        logger.info(f"Loading data to destination")
        # output_file = save_to_csv(processed_data)

        # temporary stub
        output_file = "data/processed/temp_output.csv"
        logger.info(f"ETL pipeline completed. Output: {output_file}")

        return output_file

    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_etl()