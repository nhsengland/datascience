import sys
from shutil import rmtree
from pathlib import Path
from setuptools import setup, Command, find_packages

HERE = Path(__file__).parent
setup(
    name="suppress_logs",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "suppress_logs = suppress_logs:SuppressLogsPlugin"
        ]
    }
)