#
#uv run --directory /media/aleksei/home/MyProject/python/files test_loguru.py
#


from loguru import logger
import os

if not os.path.isfile("log/somefile.log"):
    raise(Exception('not file path'))

logger.add("log/somefile.log", enqueue=True, rotation="500 MB")

logger.debug('debug')
logger.info('info')
logger.warning('warn')
logger.error('error')
logger.exception('exception')