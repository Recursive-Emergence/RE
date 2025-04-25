from setuptools import setup, find_packages

setup(
    name='life_origins',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simulation of realistic chemistry for studying the origins of life.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/life_origins',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'pandas',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)