# coding=utf-8


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

"""
这里这么写的目的时防止setup导入出错，安装出现异常。但一般不会出错
"""


config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)