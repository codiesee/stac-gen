from setuptools import setup

setup(name='stac-gen',
      version='0.1',
      description='Python tool for creating a STAC catalog for NAIP and other imagery sources',
      url='https://github.com/syncarto/stac-gen',
      author='Michael Hiley',
      author_email='hiley@syncarto.com',
      license='MIT',
      packages=['stac_gen'],
      install_requires=[
                'boto3',
                'rasterio',
                'sat-stac',
                'shapely',
                'stac-validator',
          ],
      )