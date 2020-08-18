import logging

log_dir = 'logs'
logging.basicConfig(filename='logs/file.log')
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)
log_str = '%(filename)s - %(lineno)s - %(message)s'
formatter = logging.Formatter(log_str)

fh = logging.FileHandler('logs/file.log', mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)
