from setuptools import setup, find_packages

setup(
    name='openrbyr',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'torch',
        'opencv-python',
        # Add other dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='OpenRBYR: Industrial CT Defect Detection Dashboard',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HussainAther/OpenRBYR',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

