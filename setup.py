from setuptools import setup, find_packages

setup(
    name="missing_words_game",
    version="0.1.0",
    packages=find_packages(),  # Auto-find packages (e.g., if you have a `/missing_words_game` folder)
    install_requires=[
        "numpy",  # Add your dependencies here (match conda-environment.yml)
        "pandas",
    ],
    python_requires=">=3.10",  # Match your conda Python version
)
