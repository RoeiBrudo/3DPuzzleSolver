import setuptools


setuptools.setup(
    name='CubeSolver',
    version='1.00',

    author='Roei Brudo',
    description='Private Package',

    packages=['CubeSolver'],
    package_data={'': ['CubeSolver/**']},
    include_package_data=True,

    install_requires=[
        'numpy',
    ],
)
