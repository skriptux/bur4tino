from setuptools import setup, find_packages

setup(
    name='bur4tino',
    version='0.1',
    packages=find_packages(),
    install_requires=[  # Убираем aiogram
        # Другие зависимости, если они появятся в будущем
    ],

    # include_package_data=True,  # Включает дополнительные файлы, такие как .md
    # package_data={
    #     # че нибудь
    # },

    entry_points={
        'console_scripts': [
            'bur4tino=bur4tino.utils:generate_json_auth',
        ],
    },
)

