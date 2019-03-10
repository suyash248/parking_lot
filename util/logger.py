__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Handlers
handler = logging.StreamHandler()

# Create and add formatters to handlers
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(handler)