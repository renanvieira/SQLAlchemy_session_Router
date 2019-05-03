import setuptools

from SQLAlchemy_session_router import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SQLAlchemy_session_router",
    version=__version__,
    author="Renan Vieira",
    author_email="renanvieira@live.com",
    description="An engine router to allow SQLAlchemy session connect in  multiple engine/databases using the same model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renanvieira/SQLAlchemy_session_Router",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
