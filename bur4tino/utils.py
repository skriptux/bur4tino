# import os
import json
import random
from pathlib import Path

def get_data_dir():
    """Возвращает путь к директории хранения данных."""
    data_dir = Path.home() / ".bur4tino"
    data_dir.mkdir(exist_ok=True)
    return data_dir

def read_first_line(file_path, placeholder):
    """Читает первую строку файла, удаляет её и возвращает. Если файла нет или он пуст, возвращает placeholder."""
    if not file_path.exists():
        return placeholder

    lines = file_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return placeholder

    first_line = lines[0].strip()
    file_path.write_text("\n".join(lines[1:]) + "\n", encoding="utf-8")  # Перезаписываем файл без первой строки
    return first_line if first_line else placeholder

def generate_random_password(length=12):
    """Генерирует случайный пароль."""
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(symbols, k=length))


def generate_json_auth():
    """Берёт первую строку из email'ов и ключей, создаёт JSON и удаляет их из файла."""
    data_dir = get_data_dir()
    email = read_first_line(data_dir / "emails.md", "нет имейла")
    key = read_first_line(data_dir / "keys.md", "нет ключа")

    result = {
        "email": email,
        "key": key,
        "password": generate_random_password()
    }

    return json.dumps(result, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print(generate_json_auth())

