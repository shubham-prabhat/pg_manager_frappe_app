# Copyright (c) 2024, Athru Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Room(Document):
	pass




# import frappe
# from frappe.model.document import Document

# class Room(Document):
#     def on_submit(self):
#         # Check if the document is submitted
#         if self.docstatus == 1:
#             # Create a new ToDo document
#             new_todo = frappe.get_doc({
#                 "doctype": "ToDo",
#                 "reference_type": "Room",
#                 "reference_name": self.name,
#                 "assigned_by": self.modified_by,
#                 "description": self.notes,
#                 "allocated_to": self.custom_user_id,
#                 "date": self.maintenance_schedule,
#                 "color": "#2b2323"
#             })
#             new_todo.insert(ignore_permissions=True)
