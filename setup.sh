#!/bin/bash

# Обновляем pip (менеджер пакетов Python)
pip install --upgrade pip

# Устанавливаем зависимости из файла requirements.txt (если он есть)
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "File requirements.txt not found"
fi

chmod +x main.py

mv photo_compressor.py /usr/local/bin
