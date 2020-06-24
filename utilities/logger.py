import logging

log_dir = '/test/vnfs_deploy'
# logging.basicConfig(filename='test/vnfs_deploy/file.log')

# os.chmod(log_dir, 0o777)

log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)

log_str = '%(asctime)s - %(filename)s - %(lineno)s - %(funcName)20s() - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_str)

fh = logging.FileHandler('test.log', mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)
