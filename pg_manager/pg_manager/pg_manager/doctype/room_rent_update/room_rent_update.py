# Copyright (c) 2024, Athru Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RoomRentUpdate(Document):
	pass





# # # Script in Room Rent Update doctype

# room_doc = frappe.get_doc("Room", frappe.db.get_value("Room Rent Update", doc.name, "room"))

# if room_doc:
#     # Update the room_pricing field in the Room document with the new_price from Room Rent Update
#     room_doc.set("room_pricing", doc.new_price)

#     # Save the changes to the Room document
#     room_doc.save()
# else:
#     frappe.throw("Room document not found for room: {}".format(doc.room))






# # Import frappe library
# import frappe

# # Function to update the room price in Room doctype
# def update_room_price(doc, method):
#     # Check if the 'Room Rent Update' document is submitted
#     if doc.docstatus == 1:
#         # Get the Room document linked to the Room Rent Update
#         room = frappe.get_doc("Room", doc.room)

#         # Update the room_price field in the Room document
#         room.room_pricing = doc.new_price  # Change to 'new_price'

#         # Save the changes to the Room document
#         room.save()









# # Import frappe library
# import frappe

# # Function to update the room price in Room doctype
# def update_room_price(doc, method):
#     # Execute raw SQL query to update the 'Room' document
#     frappe.db.sql("""
#         UPDATE `tabRoom`
#         SET `room_pricing` = %s
#         WHERE `name` = %s
#     """, (doc.new_price, doc.room))










# # Import frappe library
# import frappe

# # Function to update the room price in Room doctype
# def update_room_price(doc, method):
#     # Execute raw SQL query to update the 'Room' document
#     frappe.db.sql("""
#         UPDATE `tabRoom`
#         SET
#             `room_pricing` = %s,
#             `modified` = NOW()  -- Update modified field with the current timestamp
#         WHERE `name` = %s
#     """, (doc.new_price, doc.room))







# # Import frappe library
# import frappe

# # Function to update the room price in Room doctype on submit
# def on_submit(doc, method):
#     # Use frappe.db.set_value to update the 'Room' document directly
#     frappe.db.set_value("Room", doc.room, "room_pricing", doc.new_price)




# # # Import frappe library
# import frappe

# Function to update the room price in Room doctype on submit
def on_submit(doc, method):
    # Use frappe.db.set_value to update the 'Room' document directly
    frappe.db.set_value("Room", doc.room, "room_pricing", doc.new_price)
    












# import frappe

# # Function to update the room status in Room doctype on update
# def on_update(doc, method):
#     # Check if the document has been submitted
#     if doc.docstatus == 1:
#             frappe.db.set_value("Room", doc.room, "room_pricing", doc.new_price)