import logging

log_dir = 'logs'
logging.basicConfig(filename='logs/file.log')

# os.chmod(log_dir, 0o777)

log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)

# log_str = '%(asctime)s - %(filename)s - %(lineno)s - %(funcName)s() - %(levelname)s - %(message)s'
log_str = '%(filename)s - %(lineno)s - %(message)s'
# log_str = "%(asctime)s %(name)-30s %(levelname)-8s %(message)s"
formatter = logging.Formatter(log_str)

fh = logging.FileHandler('logs/file.log', mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)
