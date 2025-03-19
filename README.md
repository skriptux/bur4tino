# bur4tino

`bur4tino` — это генератор JSON, который берет ключи и email'ы из исходных файлов и добавляет пароль. Этот модуль можно импортировать в другие проекты и использовать там, где это потребуется.  

TODO: Обновить код так, чтобы он:
1. Читал нужные файлы с ключами и email'ами.
2. Генерировал пароль 

```python
def generate_random_password():
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(symbols, k=12))
```

3. Собирал JSON и выдавал его в нужном формате.  

Окей, файлы будут храниться в ~/.bur4tino/. Тогда алгоритм работы программы будет таким:

Проверять, существует ли директория ~/.bur4tino/.
Если нет — создавать её и предлагать пользователю добавить файлы emails.md и keys.md.
Загружать данные из этих файлов.
Генерировать JSON с ключами, email'ами и паролем.
Теперь надо обновить код, чтобы он умел работать с этой папкой. Начнём?
