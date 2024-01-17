# Copyright (c) 2024, Athru Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RoomBookingTable(Document):
	pass








# Import frappe library
import frappe

@frappe.whitelist()
def get_room_details(room):
    room_details = frappe.get_value('Room', room, ['room_type', 'custom_room_number', 'floor_no', 'room_pricing'], as_dict=True)
    return room_details

# Add a new method for fetching room details for the 'Room Booking' doctype
@frappe.whitelist()
def get_room_booking_details(room_booking_name):
    room_booking_details = frappe.get_value('Room Booking Table',
                                            {'parent': room_booking_name},
                                            ['room_type', 'room_no', 'floor_no'],
                                            as_dict=True)
    return room_booking_details

# Add a new method to fetch the room_pricing value
@frappe.whitelist()
def get_room_pricing(room):
    room_pricing = frappe.get_value('Room', room, 'room_pricing')
    return room_pricing













# # # # # # Script for update Room doctype once Room booking is confirm or Submitted
