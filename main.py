#!/usr/bin/env python3
"""
QR Code Generator Application
Generates QR codes from URLs and saves them as PNG images.
"""

import argparse
import logging
import os
from datetime import datetime
from pathlib import Path

import qrcode


def setup_logging():
    """Set up logging configuration."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    log_file = logs_dir / f"qr_generator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)


def generate_qr_code(url, output_path="qr_codes"):
    """
    Generate a QR code from a URL and save it as a PNG file.
    
    Args:
        url (str): The URL to encode in the QR code
        output_path (str): The directory where QR code images will be saved
    
    Returns:
        str: The path to the generated QR code file
    """
    logger = logging.getLogger(__name__)
    
    # Create output directory if it doesn't exist
    output_dir = Path(output_path)
    output_dir.mkdir(exist_ok=True)
    
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Generate filename based on timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_code_{timestamp}.png"
        filepath = output_dir / filename
        
        # Save image
        img.save(filepath)
        logger.info(f"QR code generated successfully: {filepath}")
        
        return str(filepath)
    
    except Exception as e:
        logger.error(f"Error generating QR code for URL '{url}': {str(e)}")
        raise


def main():
    """Main function to handle command-line arguments and generate QR codes."""
    parser = argparse.ArgumentParser(
        description="Generate QR codes from URLs"
    )
    parser.add_argument(
        "--url",
        type=str,
        default=os.getenv("QR_CODE_URL", "http://github.com/kaw393939"),
        help="URL to encode in the QR code (default from QR_CODE_URL env var or http://github.com/kaw393939)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=os.getenv("QR_OUTPUT_DIR", "qr_codes"),
        help="Directory to save QR codes (default from QR_OUTPUT_DIR env var or 'qr_codes')"
    )
    
    args = parser.parse_args()
    
    logger = setup_logging()
    logger.info("QR Code Generator Application started")
    logger.info(f"Generating QR code for URL: {args.url}")
    
    try:
        qr_file = generate_qr_code(args.url, args.output)
        logger.info(f"QR code successfully generated at: {qr_file}")
    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
