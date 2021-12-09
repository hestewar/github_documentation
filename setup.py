from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Github Documentation Package'
LONG_DESCRIPTION = 'Method for tracking inputs, outputs, dependencies in a markdown format that can be easily navigated in Github'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="github_documentation",
    version=VERSION,
    author="Harper Stewart",
    author_email="<harperestewart7@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'documentation', 'github', 'links'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)