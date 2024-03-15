#!/usr/bin/env python3

import os
import time

from tqdm import tqdm
import logging

from PIL import Image


extensions = {'png', 'jpg', 'jpeg'}

ignore = {'.git', '.idea'}


def compressor(deep_dir=None):
    if deep_dir is not None:
        os.chdir(deep_dir)

    contents = set(os.listdir()) - ignore

    logging.debug(f"Current dir : {os.getcwd()}")

    for item in contents:
        f = os.open(item, os.O_RDONLY)

        if os.path.isdir(f):
            logging.debug(f"Dir : {item}")

            compressor(item)
            os.chdir(os.pardir)

            continue
        if os.path.isfile(f):
            logging.debug(f"File : {item}")
            try:
                if item.rsplit('.')[1] not in extensions:
                    logging.debug(f"{item} is not photo")
                    continue
            except IndexError:
                logging.debug(f"{item}: Unknown file extension")
                continue

            image = Image.open(item)
            image = image.convert('RGB')
            image.save(f'{os.getcwd()}/{item.rsplit(".")[0]}.webp', 'webp')

            os.remove(item)

            logging.debug(f"{item} was compressed")

            continue

        os.close(f)


def long_running_function():
    for i in tqdm(range(5)):  # Прогресс-бар будет отображать 10 шагов
        compressor()  # Вызываем ваш скрипт здесь
        time.sleep(0.1)  # Демонстрационная задержка


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('The script has started its execution.')
    long_running_function()
    logging.info('The script has completed its execution.')
