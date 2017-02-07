# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2017 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This plugin applies a bunch of patches on the code using
    git am --signoff < [patch]

    taking as source all .patch files found in folder specified by using 'patches' property

    Also replaces SUBDIRS at the beginning of Makefile.am for including loleaflet subdir
"""

import os
import logging
import shutil
import sys

import subprocess

from snapcraft.plugins import autotools
from tempfile import mkstemp

logger = logging.getLogger(__name__)

class LoolwsdPlugin(autotools.AutotoolsPlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()

        schema['properties']['patches'] = {
            'type': 'string',
            'default': '',
        }

        return schema

    def pull(self):
        super().pull()
        # Apply patches if found in patches folder after pulling sources from repo
        project_dir = os.getcwd()
        patches_path = os.path.join(project_dir, self.options.patches)

        if os.path.exists(patches_path):
            os.chdir(self.sourcedir)
            for file in os.listdir(patches_path):
                if file.endswith('.patch'):
                    logger.info('applying patch ' + file)
                    #os.system('git apply ' + os.path.join(patches_path, file))
                    subprocess.check_call(['git', 'apply', os.path.join(patches_path, file)])
                    #os.system('git am --signoff < ' + os.path.join(patches_path, file))

            os.chdir(project_dir)
   