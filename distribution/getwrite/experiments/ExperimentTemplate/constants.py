# -*- coding: utf-8 -*-
#
# This file is part of the OpenHandWrite project software.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
### Misc. constants or general settings that may want to be changed if
### modifying the example python experiment template.
#

import os

EXP_NAME =  u'OpenHW Template'
EXP_VERSION = "0.2"

DEFAULT_SESSION_CODE = u's1234'

# RGB255 color to use for the experiment window background color. Must be a
# list or tuple of the form [r,g,b], where r,g, and b are values between 0
# (black) and 255 (white).
DEFAULT_SCREEN_COLOR = [128,128,128]

# The height of any text that is displayed during experiment trials. The value
# is in norm units, with a maximum value of 1.0.
DEFAULT_TEXT_STIM_HEIGHT = 0.05

# List of file extensions that should be used to determine if a _VIS column
# value should be treated as the image name for an Image stim or as a string
# literal for a Text stimulus.
ACCEPTED_IMAGE_FORMATS = ['bmp', 'png']

# List of key values that will cause the experiment to end if detected by a
# keyboard key press event.
TERMINATE_EXP_KEYS = ['escape',]

# Constants for the absolute paths to various experiment subfolders
AUDIO_FOLDER = os.path.join(os.path.dirname(__file__),u'resources',u'audio')
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__),u'resources',u'image')
CONDITIONS_FOLDER =  os.path.join(os.path.dirname(__file__),u'conditions')

# Defaults for PenPositionStim
PEN_POS_HOVER_COLOR = (0, 0, 255)
PEN_POS_TOUCHING_COLOR = (0, 255, 0)
PEN_POS_ANGLE_COLOR = (255, 255, 0) 
PEN_POS_ANGLE_WIDTH = 1
PEN_POS_GFX_MIN_OPACITY = 0.0
PEN_POS_GFX_MIN_SIZE = 0.033
PEN_POS_GFX_SIZE_RANGE = 0.1666

#Defaults for PenTracesStim
PEN_TRACE_LINE_WIDTH = 2
PEN_TRACE_LINE_COLOR=(0, 0, 0)
PEN_TRACE_LINE_OPACITY=1.0

