#!/usr/bin/env python3

import logging

logger = logging.getLogger()
logger.setLevel("INFO")


def main(event, _context):
    logger.info("Hello!")
    logger.info(event)


if __name__ == "__main__":
    main({'foo': "bar"}, {})
