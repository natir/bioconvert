# -*- coding: utf-8 -*-

###########################################################################
# Bioconvert is a project to facilitate the interconversion               #
# of life science data from one format to another.                        #
#                                                                         #
# Authors: see CONTRIBUTORS.rst                                           #
# Copyright © 2018  Institut Pasteur, Paris and CNRS.                     #
# See the COPYRIGHT file for details                                      #
#                                                                         #
# bioconvert is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by    #
# the Free Software Foundation, either version 3 of the License, or       #
# (at your option) any later version.                                     #
#                                                                         #
# bioconvert is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# GNU General Public License for more details.                            #
#                                                                         #
# You should have received a copy of the GNU General Public License       #
# along with this program (COPYING file).                                 #
# If not, see <http://www.gnu.org/licenses/>.                             #
###########################################################################

##############################################################################
""" Converts Genbank format to GFF3 using biocode
https://github.com/jorvis/biocode/

We may want to do it directly in python in the future,
without calling the external script
"""

from bioconvert import ConvBase

__all__ = ["GENBANK2GFF"]


class GENBANK2GFF(ConvBase):
    """Convert :term:`GENBANK` file to :term:`GFF` file

    Some description.

    """
    _default_method = "biocode"

    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input GENBANK file
        :param str outfile: output GFF filename

        """
        super().__init__(infile, outfile)


    def _method_biocode(self, *args, **kwargs):
        """Uses scripts from biocode
        See: https://github.com/jorvis/biocode/
        https://github.com/jorvis/biocode/blob/master/gff/convert_genbank_to_gff3.py
        """
        cmd = "convert_genbank_to_gff3.py -i {} -o {} --no_fasta".format(
            self.infile, self.outfile)
        self.execute(cmd)
