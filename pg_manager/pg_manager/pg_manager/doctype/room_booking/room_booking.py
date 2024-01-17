# Copyright (c) 2024, Athru Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class RoomBooking(Document):
# 	pass








from frappe.model.document import Document
import frappe

class RoomBooking(Document):
    pass



import frappe

# Function to update the room status in Room doctype on update
def on_submit(doc, method):
    # Check if the document has been submitted
    if doc.docstatus == 1:
        # List to store occupied rooms
        occupied_rooms = []

        # Iterate through the rows in the room_table
        for room_entry in doc.room_table:
            # Check if the room is already occupied
            current_status = frappe.get_value("Room", room_entry.room, "room_status")
            if current_status == "Occupied":
                occupied_rooms.append(room_entry.room)

        if occupied_rooms:
            # Throw a message with occupied rooms in bold
            occupied_rooms_str = ", ".join(f'<strong>{room}</strong>' for room in occupied_rooms)
            frappe.throw(f"The following rooms are already occupied: {occupied_rooms_str}")

        # Continue with the rest of the update logic...
        for room_entry in doc.room_table:
            # Check if the room is already occupied (optional)
            current_status = frappe.get_value("Room", room_entry.room, "room_status")
            if current_status != "Occupied":
                # Use frappe.db.set_value to update the 'Room' document directly
                frappe.db.set_value("Room", room_entry.room, "room_status", "Occupied")

                # Update additional fields
                frappe.db.set_value("Room", room_entry.room, "occupant_name", doc.customer_name)
                frappe.db.set_value("Room", room_entry.room, "custom_check_in_date", doc.check_in_date)
                frappe.db.set_value("Room", room_entry.room, "custom_check_out_date", doc.check_out_date)
                frappe.db.set_value("Room", room_entry.room, "customer_address", doc.customer_address)
                frappe.db.set_value("Room", room_entry.room, "customer_contact_number", doc.customer_contact_number)
                frappe.db.set_value("Room", room_entry.room, "customer_advance_paid", doc.customer_advance_paid)

# # # Above code is prevent the Room Booking doctype when room_status is already "Occupied" with showing Room names, working propoerly








# Function to handle actions on cancellation of the document
def on_cancel(doc, method):
    # Check if the document has been cancelled
    if doc.docstatus == 2:
        # Iterate through the rows in the room_table
        for room_entry in doc.room_table:
            # Check if the room status is Occupied
            room_status = frappe.get_value("Room", room_entry.room, "room_status")
            if room_status == "Occupied":
                # Update 'Room' document when room status is Occupied
                frappe.db.set_value("Room", room_entry.room, "room_status", "Available")
                
                # Update additional fields to null
                frappe.db.set_value("Room", room_entry.room, "occupant_name", None)
                frappe.db.set_value("Room", room_entry.room, "custom_check_in_date", None)
                frappe.db.set_value("Room", room_entry.room, "custom_check_out_date", None)
                frappe.db.set_value("Room", room_entry.room, "customer_address", None)
                frappe.db.set_value("Room", room_entry.room, "customer_contact_number", None)
                frappe.db.set_value("Room", room_entry.room, "customer_advance_paid", '0.00')
            else:
                frappe.throw("Cancellation not allowed. Room is not currently occupied.")

# # # Above code is prevent the Room Cancelling, if doctype room_status is already "Available" with showing Room names, working propoerly







# # Script Name: Update Booking Status on docstatus
# # # Doctype: Room Booking

# def booking_status_on_update(doc, method):
#     # Set the booking status to 'Confirm'
#     doc.booking_status = 'Confirm'

#     # Check if the room table is linked and has rows
#     if doc.room_table:
#         # Create a list to store room names
#         room_names = [row.get('room') for row in doc.room_table]

#         # Check the 'room_status' of each room
#         for room_name in room_names:
#             # Get the room document for each room
#             room_doc = frappe.get_doc('Room', room_name)

#             # Check if the room document is found and the status is 'Occupied'
#             if  room_doc and room_doc.room_status == 'Occupied':
#                 # Throw an error if any room is 'Occupied'
#                 frappe.throw(f'Error: Room "{room_name}" is occupied. Booking cannot be set to Confirmed.')

#     else:
#         # Throw an error if the room table is not linked
#         frappe.throw('Error: Room table must be linked to set the booking status to Confirm.')
  



# # Define your on_cancel method
# def booking_status_on_cancel(doc, method):
#     # Check if the room table is linked and has rows
#     if doc.room_table:
#         # Create a list to store room names
#         room_names = [row.get('room') for row in doc.room_table]

#         # Check the 'room_status' and 'room_booking' of each room
#         for room_name in room_names:
#             # Get the room document for each room
#             room_doc = frappe.get_doc('Room', room_name)

#             # Check if the room document is found and the status is 'Available' or 'room_booking' is 'Available'
#             if room_doc and (room_doc.room_status == 'Available' or room_doc.room_booking == 'Available'):
#                 # Throw an error if any room is 'Available'
#                 frappe.throw(f'Error: Room "{room_name}" is available. Booking cannot be cancelled.')

#         # If no room has 'Available' status, update the booking status to 'Cancelled'
#         doc.booking_status = 'Cancelled'
#     else:
#         # Throw an error if the room table is not linked
#         frappe.throw('Error: Room table must be linked to cancel the booking.')



















# # Define the function to be executed on document submission
# def create_customer_on_submit(doc, method):
#     if doc.docstatus == 1:
#         # Check if the customer with the given name already exists
#         existing_customer = frappe.get_all("Customer", filters={"customer_name": doc.customer_name}, limit=1)

#         if not existing_customer:
#             # If the customer doesn't exist, create a new Customer document
#             new_customer = frappe.new_doc("Customer")
#             new_customer.customer_name = doc.customer_name
#             # Add other fields you want to set for the new customer
#             # new_customer.field_name = value
#             new_customer.save()

# # # # # Above code is working properly, creating new customer if new, on submit Room Booking form









# # # # # Below Script is working properly, creating new customer if new, on submit Room Booking form with all details in the "customer_details field"

# Define the function to be executed on document submission
def create_customer_on_submit(doc, method):
    if doc.docstatus == 1:
        # Check if the customer with the given name already exists
        existing_customer = frappe.get_all("Customer", filters={"customer_name": doc.customer_name}, limit=1)

        if not existing_customer:
            # If the customer doesn't exist, create a new Customer document
            new_customer = frappe.new_doc("Customer")
            new_customer.customer_name = doc.customer_name
            
            # Set the 'customer_details' field using information from the Room Booking document
            new_customer.customer_details = f"{doc.customer_address}\n{doc.customer_name}\n{doc.customer_contact_number}"

            # Add other fields you want to set for the new customer
            # new_customer.field_name = value

            new_customer.save()















# Import the required modules
from frappe import _

# Hook function to validate the "customer_identity_number" field
def validate_customer_identity_number(doc, method):
    # Set the minimum length requirement
    min_length = 12

    # Get the value of the "customer_identity_number" field
    customer_identity_number = doc.customer_identity_number

    # Check if the length is less than the minimum required length
    if len(customer_identity_number) < min_length:
        frappe.throw(_("Customer Identity Number must be at least {} characters long.").format(min_length), title=_("Validation Error"))
