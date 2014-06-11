from distutils.core import setup

setup(name='dataset_owners',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Dataset owners from Socrata Open Data Catalog',
      url='https://github.com/tlevine/dataset-owners',
      packages=['pluplusch'],
      install_requires = [
          'pluplusch>=0.0.7',
      ],
      scripts = ['owners.py'],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
