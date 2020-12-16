import logging
import os

other_folder = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'logs/file.log'))
# print("Other file: " + other_folder)

log_dir = 'logs'
logging.basicConfig(filename=other_folder)
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)
log_str = '%(asctime)s - %(filename)s - %(lineno)s - %(message)s'
formatter = logging.Formatter(log_str)

fh = logging.FileHandler(other_folder, mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)
