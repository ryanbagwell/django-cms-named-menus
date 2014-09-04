#/usr/bin/env python
import codecs
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


def build(target_dir):

    build_commands = ' && '.join([
        'cd %s' % os.path.dirname(os.path.realpath(__file__)),
        'npm install',
        './node_modules/.bin/bower install',
        './node_modules/.bin/grunt build',
        'cp -r cms_named_menus/static/cmsnamedmenus/* %s' % os.path.join(target_dir, 'cms_named_menus/static/cmsnamedmenus/')
    ])

    print "Running %s" % build_commands

    os.system(build_commands)

class Install(_install):

    def run(self):

        _install.run(self)

        self.execute(build, (self.install_lib,), msg="Building static files ...")


setup(
    name='django-cms-named-menus',
    version='0.1',
    description='Allows you to add named menus like Wordpress',
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.rst')),
    author='Ryan Bagwell',
    author_email='ryan@ryanbagwell.com',
    license='BSD',
    url='https://github.com/hzdg/django-cms-named-menus/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Django>=1.4',
    ],
    cmdclass={
        'install': Install
    },
)