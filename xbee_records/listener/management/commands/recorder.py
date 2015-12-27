from django.core.management.base import BaseCommand, CommandError
from listener.models import *
from xbee import XBee, ZigBee
import serial
import json
import binascii
import re
from datetime import datetime

strip_leading_nonprintables = re.compile("^[^\w]+")
strip_trailing_nonprintables = re.compile("[^!\w]+$")

class Command(BaseCommand):
	help = 'Listens to the specified serial port for XBee API messages and records them in the listener database.'
	
	def add_arguments(self, parser):
		parser.add_argument('port', help='The serial device to listen to')
		parser.add_argument('--speed', help='The bit rate of the serial port.', type=int, default=115200)

	def interpretFrame(self, frame):
		interpreted_frame = {}
		current_time = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
		non_hex_items = ['id', 'rf_data', 'node_id']
		for item in frame.keys():
			if item in non_hex_items:
				interpreted_frame[item] = frame[item]
			else:
				interpreted_frame[item] = binascii.hexlify(frame[item])
		interpreted_frame['timestamp'] = current_time
		return interpreted_frame

	def handle(self, *args, **options):
		port_string = options['port']
		port_speed = options['speed']
		
		serial_port = serial.Serial(port_string, port_speed)
		xbee = ZigBee(serial_port)
		while True:
			try:
				escaped_frame = {}
				frame = xbee.wait_read_frame()
				interpreted = self.interpretFrame(frame)
				if (interpreted.has_key('rf_data')):
					interpreted['rf_data'] = strip_leading_nonprintables.sub('', interpreted['rf_data'])
					interpreted['rf_data'] = strip_trailing_nonprintables.sub('', interpreted['rf_data'])
				print json.dumps(interpreted, encoding="utf8")
				if interpreted['id'] == 'rx':
					RfData.create_from_frame(interpreted)
				if interpreted['id'] == 'node_id_indicator':
					NodeRegistration.create_from_frame(interpreted)
			except KeyboardInterrupt:
				break
			except UnicodeDecodeError:
				print "Could not decode {stuff} as UTF-8.\n".format(stuff=interpreted)
		serial_port.close()
