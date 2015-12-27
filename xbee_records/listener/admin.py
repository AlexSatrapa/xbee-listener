from django.contrib import admin
from models import *

class NodeRegistrationAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'source_addr_long', 'node_id')

class RfDataAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'source_addr_long', 'rf_data')

admin.site.register(NodeRegistration, NodeRegistrationAdmin)
admin.site.register(RfData, RfDataAdmin)
