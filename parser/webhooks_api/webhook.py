import logging
from logging.handlers import RotatingFileHandler

# Настройка регистратора
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Настройка обработчика (ротация логов)
handler = RotatingFileHandler(
    f'{__name__}.log',
    maxBytes=50000000,
backupCount=5)
logger.addHandler(handler)

# Настройка форматера
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

class WebHook:
    def __init__(self, data):
        self.data_new_post = data
    def check_id(self):
        try:
            id = self.data.get('blog').get('id')
            logger.info('id получен')
            return id
        except Exception as e:
            logger.error('Не удалосьт получить id поста')
            return None
    def get_id_new_post(self):
        return self.check_id()
