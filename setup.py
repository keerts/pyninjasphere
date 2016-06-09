from codecs import open as codecs_open
from setuptools import setup, find_packages

setup(name='pyninjasphere',
      version='0.0.1',
      description=u"NinjaSphere client",
      long_description="Long description",
      classifiers=[],
      keywords='',
      author=u"Gert-Jan van de Streek",
      author_email='g.j.streek@avisi.nl',
      url='https://github.com/keerts/pyninjasphere',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      install_requires=[
          'click',
          'jsonmodels',
          'paho-mqtt',
          'requests',
          'requests_mock',
          'mock',
          'httpretty', 'testfixtures'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      pyninjasphere=pyninjasphere.scripts.cli:cli
      """
      )
