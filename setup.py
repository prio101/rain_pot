from setuptools import setup, find_packages

setup(
    name="Rain Pot",
    version="0.1.0",
    author="Mahabub Islam",
    author_email="miprio101@gmail.com",
    description="Collects Video from cloud, Generates video with text overlay, watermark, and background music; Collects and saves into a single file",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prio101/rain_pot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "certifi==2023.11.17",
        "charset-normalizer==3.3.2",
        "decorator==4.4.2",
        "idna==3.6",
        "imageio==2.33.0",
        "imageio-ffmpeg==0.4.9",
        "moviepy==1.0.3",
        "numpy==1.24.4",
        "Pillow==9.5.0",
        "proglog==0.1.10",
        "requests==2.31.0",
        "tqdm==4.66.1",
        "urllib3==2.1.0",
    ],
)
