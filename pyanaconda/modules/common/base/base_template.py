#
# Interface templates for Anaconda modules.
#
# Copyright (C) 2018 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
from pyanaconda.dbus.template import AdvancedInterfaceTemplate


class ModuleInterfaceTemplate(AdvancedInterfaceTemplate):
    """The DBus interface template for a module.

    The template should be used to create DBus interfaces
    for instances of BaseModule.
    """

    def connect_signals(self):
        """Connect the signals."""
        self.implementation.module_properties_changed.connect(self.flush_changes)


class KickstartModuleInterfaceTemplate(ModuleInterfaceTemplate):
    """The DBus interface template for a kickstart module.

    The template should be used to create DBus interfaces
    for instances of KickstartBaseModule.
    """
    pass