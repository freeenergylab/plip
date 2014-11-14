# coding=utf-8
"""
Protein-Ligand Interaction Profiler - Analyze and visualize protein-ligand interactions in PDB files.
Module for testing the predictions with interactions from literature.
Copyright (C) 2014  Sebastian Salentin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""


import unittest
import subprocess


class SpecialCasesTest(unittest.TestCase):
    """Checks special and extreme cases for input files."""

    def test_empty_input_file(self):
        """Input file is empty."""
        exitcode = subprocess.call('python ../plip-cmd.py -f ./special/empty.pdb', shell=True)
        self.assertEqual(exitcode, 2)  # Specific exitcode 2

    def test_invalid_pdb_id(self):
        """A PDB ID with no valid PDB record is provided."""
        exitcode = subprocess.call('python ../plip-cmd.py -i xx1x', shell=True)
        self.assertEqual(exitcode, 3)  # Specific exitcode 3

    def test_invalid_input_file(self):
        """A file is provided which is not a PDB file."""
        exitcode = subprocess.call('python ../plip-cmd.py -f ./special/non-pdb.pdb', shell=True)
        self.assertEqual(exitcode, 4)  # Specific exitcode 4


#@todo Implement other unit tests below, also check if output files exists and exit code is 0
# Other ideas #
# 4pth (largest PDB file with > 100 MB size)
# 1EVE with no interactions for e.g. NAG-A-3003
# 2PF1 with no ligands
# 3wu2 with most ligands

