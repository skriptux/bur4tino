from setuptools import setup, find_packages

setup(
    name='bur4tino',
    version='0.1',
    packages=find_packages(),
    install_requires=[  # Убираем aiogram
        # Другие зависимости, если они появятся в будущем
    ],
    include_package_data=True,  # Включает дополнительные файлы, такие как .md
    package_data={
        '': ['data/*.md'],  # Указывает, что файлы данных должны быть включены в пакет
    },
    entry_points={
        'console_scripts': [
            'bur4tino=bur4tino.bot:main',  # Запуск бота через команду run-bot
        ],
    },
)

