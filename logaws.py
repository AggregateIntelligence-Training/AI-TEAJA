import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def my_handler(event, context):
   logger.info('Using logger to print messages to cloudwatch logs')
   return "aws lambda in python using zip file"