#!/usr/bin/env python

# This file is part of freenrgworkflows.
#
# Copyright 2016,2017 Julien Michel Lab, University of Edinburgh (UK)
#
# freenrgworkflows is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, Extension
import versioneer

setup(
    cmdclass=versioneer.get_cmdclass(),
    name='freenrgworkflows',
    version=versioneer.get_version(),
    description='python package for analysis relative free energy calculations with Sire',
    url='https://github.com/michelllab/freenrgworkflows',
    maintainer='Antonia Mey',
    maintainer_email='antonia.mey@ed.ac.uk',
    license='LGPLv3+',
    packages=['networkanalysis'],
    scripts=[]
)
