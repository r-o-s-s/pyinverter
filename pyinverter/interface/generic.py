""""pyinverter - Python interface to most common inverters
    Copyright (C) 2021  Ross Hogan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class GenericInterface:
    """ A generic interface class with the framwork for talking to physical devices. """

    def __init__(self):

        pass

    def send(self, message: bytearray):
        """ Send message contence to interface device. """
        raise NotImplementedError

    def read(self) -> bytearray:
        """ Read from the interface device. """
        raise NotImplementedError

    def connect(self):
        """ Perform set up and connect to the interface device. """
        raise NotImplementedError

    def disconnect(self):
        """ Perform clean up and disconnect from the interface device. """
        raise

    def __enter__(self):
        """ Define an enter method to perform setup when using context manager. """
        self.connect()
        return self

    def __exit__(self):
        """ Define an exit method to perform clean up when using context manager. """
        self.disconnect()
