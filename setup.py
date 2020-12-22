from setuptools import setup, find_packages


def requirements():
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


packages = find_packages()

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='depix',
    version='1.0.1',
    author='beurtschipper',
    license='CC BY 4.0',
    url='https://github.com/beurtschipper/Depix',
    description='Depix is a tool for recovering passwords from pixelized screenshots.',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=packages,
    install_requires=requirements(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
    ],
)
