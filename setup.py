import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="tabular-rat-zimfv",
    version="0.0.2",
    author="Fedor Zimin",
    author_email='zimfv@yandex.ru',
    description='RAT - Restoring Aggregated Tables',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zimfv/rat',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "rat"},
    packages=setuptools.find_packages(where="rat"),
    python_requires=">=3.6",
    install_requires=[
        "numpy >= 1.15",
        "scipy >= 1.1.0",
        "pandas >= 1.3.5",
        "cvxpy >= 1.1.18",
    ],
    setup_requires=[
        "numpy >= 1.15",
        "scipy >= 1.1.0",
        "pandas >= 1.3.5",
        "cvxpy >= 1.1.18",
    ],
)
