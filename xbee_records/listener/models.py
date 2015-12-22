from __future__ import unicode_literals

from django.db import models

class NodeRegistration(models.Model):
	device_type = models.CharField(max_length=2, help_text="Is the device a Node, Relay or Coordinator?", verbose_name="Device Type") # FIXME: find reference
	digi_profile_id = models.CharField(max_length=4, help_text="A number representing a particular communication type, see Digi documentation", verbose_name="Digi Profile ID") # FIXME: find reference to cite
	manufacturer_id = models.CharField(max_length=4, help_text="The number identifying the device manufacturer", verbose_name="Manufacturer")
	node_id = models.CharField(max_length=60, help_text="The name given to the node", verbose_name="Node ID")
	options = models.CharField(max_length=2, help_text="Bit-coded field of options for packet delivery #FIXME find reference", verbose_name="Options")
	packet_type = models.CharField(max_length=60, help_text="The purpose of this packet", verbose_name="Packet Type")
	parent_source_addr = models.CharField(max_length=4, help_text="#FIXME", verbose_name="Parent Soruce Address")
	sender_addr = models.CharField(max_length=4, help_text="Short version of sender's address (node which relayed packet to coordinator)", verbose_name="Sender Address")
	sender_addr_long = models.CharField(max_length=16, help_text="Long form address of the node which relayed the packet to coordinator", verbose_name="Sender Address (Long)")
	source_addr = models.CharField(max_length=4, help_text="Short version of source address (original source)", verbose_name="Source Address")
	source_addr_long = models.CharField(max_length=16, help_text="Long form address of original source of packet", verbose_name="Source Address (Long)")
	source_event = models.CharField(max_length=2, help_text="TODO: what is source event?", verbose_name="Source Event")
	timestamp = models.CharField(max_length=15, help_text="The time at which this packet was received from the coordinator node", verbose_name="Received")
	stuff = models.CharField(max_length=8, help_text="#FIXME", verbose_name="FIXME")

class RfData(models.Model):
	options = models.CharField(max_length=2, help_text="Bit-coded field of options for packet delivery #FIXME find reference", verbose_name="Options")
	rf_data = models.CharField(max_length=255, help_text="The data sent from the source", verbose_name="RF Data")
	source_addr = models.CharField(max_length=4, help_text="Short version of source address", verbose_name="Source Address")
	source_addr_long = models.CharField(max_length=16, help_text="Long form address of original source of packet", verbose_name="Source Address (Long)")
	timestamp = models.CharField(max_length=15, help_text="The time at which this packet was received from the coordinator node", verbose_name="Received")
