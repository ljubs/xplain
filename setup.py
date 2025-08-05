from setuptools import setup

setup(
    name='xplain',
    py_modules=['xplain'],
    install_requires=['openai', 'python-dotenv', 'rich'],
    entry_points={
        'console_scripts': [
            'xplain = xplain:main',
        ],
    },
)