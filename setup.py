from setuptools import setup, find_packages

setup(
    name="voxpass",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["click"],
    entry_points={"console_scripts": {"voxpass = voxpass.__main__:run"}},
)
