import time
import Microtuber_vesting.preset
from Microtuber_vesting.vesting import vesting
import logging

logging.basicConfig(filename='log_SEEDBOX.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

address = Microtuber_vesting.preset.SEEDBOX
priv = Microtuber_vesting.preset.SEEDBOX_PRIV

if __name__ == '__main__':
    for i in range(48):
        start_time = time.time()
        logger.info(f'-------------STEP------------- {i}')
        try:
            if i == 5:  # пропускаем, чтоб в 6 получить за 5 и 6
                continue
            if address != Microtuber_vesting.preset.SEEDBOX and i in range(27, 38):  # пропускаем чтоб склеймить потом
                continue
            else:
                vesting(address, priv, logger)
        except Exception as e:
            logger.error(f'ERROR {e}')
        if i == 2:  # Клеймим повторно после того как уже склеймили
            logger.info('повторный клейм')
            try:
                vesting(address, priv, logger)
            except Exception as e:
                logger.error(f'ERROR {e}')
        end_time = time.time()
        time_diff = 60 - (int(end_time) - int(start_time))
        time.sleep(time_diff)