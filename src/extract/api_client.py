"""
API client for fetching currency exchange rates
Handles HTTP requests, error handling and data validation
"""
import requests
import logging
from typing import Dict, Any, Optional

from config.config import API_BASE_URL, BASE_CURRENCY, TARGET_CURRENCIES

logger = logging.getLogger(__name__)

def fetch_exchange_rates(base_currency: str = BASE_CURRENCY) -> Optional[Dict[str, Any]]:
    """
    Fetch latest exchange rates from Frankfurter API

    Args:
        base_currency: Base currency for conversation (default: USD)

    Returns:
        Dictionary with API response or None if failed

    Raises:
        requests.RequestException: If network or API error occurs
    """
    try:
        logger.info(f"Fetching exchange rates for base currency: {base_currency}")

        # Construct API URL
        url = f"{API_BASE_URL}/latest"
        params = {
            'base': base_currency,
            'symbols': ','.join(TARGET_CURRENCIES)
        }

        logger.debug(f"API request: {url} with params: {params}")

        # Make HTTP GET request with timeout
        response = requests.get(url, params=params, timeout=10)

        # Check if request was successful
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        logger.info(f"Successfully fetched rates for {len(data.get('rates', {}))} currencies")
        logger.debug(f"API response: {data}")
        
        return data

    except requests.exceptions.Timeout:
        logger.error("API request timed out after 10 seconds")
        return None

    except requests.exceptions.ConnectionError:
        logger.error("Network connection error")
        return None

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None

    except ValueError as e:
        logger.error(f"Failed to parse JSON response: {e}")

def validate_api_response(data: Dict[str, Any]) -> bool:
    """
    Vaildate structure of API response

    Args:
        data: API response dictionary

    Returns:
        True if response is valid, False otherwise
    """
    required_fields = ['base', 'date', 'rates']

    if not data:
        logger.error("Empty API response")
        return False

    for field in required_fields:
        if field not in data:
            logger.error(f"Missing required field in API response: {field}")
            return False

    if not isinstance(data['rates'], dict):
        logger.error("Rates field should be a dictionary")
        return False

    logger.debug("API response validation passed")
    return True