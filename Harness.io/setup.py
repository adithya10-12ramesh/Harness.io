from setuptools import setup, find_packages

setup(
    name="harness-tictactoe",
    version="1.0.0",
    description="Web-based Tic-Tac-Toe game",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "gunicorn==21.2.0"
    ],
    python_requires=">=3.7",
)