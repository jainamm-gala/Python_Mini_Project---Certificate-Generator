from setuptools import setup, find_packages

setup(
    name='certificate-gen',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
        'Pillow>=8.0',
        'certifi>=2020.6.20',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
