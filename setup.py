#!/usr/bin/env python
'''
Please be aware, that `setup.py.in` is just a template.
Strings between `@` will be replaced with variables from
Makefile, see target `setup.py`

RELEASE will be replaced with `git describe`
SETUPLIB by default is `distutils.core`

To use `setuptools`, run `make ... setuplib=setuptools`
'''
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

config = configparser.ConfigParser()
config.read('setup.ini')

module = __import__(config.get('setup', 'setuplib'),
                    globals(),
                    locals(),
                    ['setup'], 0)
setup = getattr(module, 'setup')

readme = open("README.md", "r")


setup(name='pyroute2',
      version=config.get('setup', 'release'),
      description='Python Netlink library',
      author='Peter V. Saveliev',
      author_email='peter@svinota.eu',
      url='https://github.com/svinota/pyroute2',
      license='dual license GPLv2+ and Apache v2',
      packages=['pyroute2',
                'pyroute2.config',
                'pyroute2.dhcp',
                'pyroute2.ipdb',
                'pyroute2.netns',
                'pyroute2.netns.process',
                'pyroute2.netlink',
                'pyroute2.netlink.generic',
                'pyroute2.netlink.ipq',
                'pyroute2.netlink.nfnetlink',
                'pyroute2.netlink.rtnl',
                'pyroute2.netlink.rtnl.tcmsg',
                'pyroute2.netlink.taskstats',
                'pyroute2.netlink.nl80211',
                'pyroute2.protocols',
                'pyroute2.remote'],
      classifiers=['License :: OSI Approved :: GNU General Public ' +
                   'License v2 or later (GPLv2+)',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: ' +
                   'Python Modules',
                   'Operating System :: POSIX',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 4 - Beta'],
      long_description=readme.read())
