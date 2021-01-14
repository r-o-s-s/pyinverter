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
from pyinverter.interface import GenericInterface


class GenericProtocol:
    """ A generic protocol class with the framework and commonly used functions. """

    def __init__(self, line_ending: str = "\n"):
        self._interface = None
        self._line_ending = line_ending
        self.name = self.__class__.__name__

    # These methods are expected to be implemented differently for each protocol
    def calculate_crc(self, message: bytearray) -> bytearray:
        """ Calculates the CRC of the given message. """
        # Our default is to do nothing
        return b""

    # Common methods that all protocols support.
    def attach_interface(self, interface: GenericInterface):
        """ Connect the protocol to the outside world through an interface. """
        self._interface = interface

    def add_crc(self, message: str) -> bytearray:
        """ Calculates the CRC of the message and appends it to the message. """
        response = bytearray(message, "utf-8")
        return response + self.calculate_crc(response)

    # Internal methods that are not expected to change
    def _send(self, message: str):
        """Sends a message to the inverter using the interface.
        It will add the line_ending and an optional CRC.
        """
        self._interface.send(self.add_crc(message) + self._line_ending)

    def _recv(self) -> str:
        """Reads a message from the inverter using the interface.
        It will remove the line_ending and and optional CRC.
        """
        # Fetch the next response from the buffer
        data = self._interface.read()
        # Remove the line ending
        data = data[: -len(self._line_ending)]
        # Calculate the CRC
        crc = self.calculate_crc(data)
        # The CRC it should be zero or nothing if correct
        if crc != bytearray(len(crc)):
            return None
        # remove the CRC and return the data
        data = data[: -len(crc)]
        return data.decode()


class GenericCommand:
    """ A generic command class with the basic framework of a command. """

    def __init__(self, protocol: GenericProtocol):
        self._str_help = ""
        self._str_description = ""
        self._protocol = protocol

    @property
    def get(self):
        """ Get the response of this command from the inverter """
        raise NotImplementedError

    @property
    def help(self):
        """ Return the help string for this command """
        return self._str_help

    @property
    def description(self):
        """ Return a short description of this command """
        return self._str_description
