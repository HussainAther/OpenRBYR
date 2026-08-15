from setuptools import setup, find_packages

setup(
    name="openrbyr-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "opencv-python",
        "torch",
        "scipy",
        "pydicom",
    ],
    author="Syed Hussain Ather",
    author_email="shussainather@gmail.com",
    description="Ray-by-ray CT simulation engine and utilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HussainAther/OpenRBYR",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

