import logging

log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')

fh = logging.FileHandler('test.log', mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)