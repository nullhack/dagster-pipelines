import setuptools

setuptools.setup(
    name="myd",
    packages=setuptools.find_packages(exclude=["myd_tests"]),
    install_requires=[
        "dagster==0.11.9",
        "dagit==0.11.9",
        "pytest",
    ],
)
