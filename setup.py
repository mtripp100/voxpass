from setuptools import setup, find_packages
setup(
    name="voxpass",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'voxpass = voxpass.voxpass:cli'
        ]
    },
    install_requires=['click'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
