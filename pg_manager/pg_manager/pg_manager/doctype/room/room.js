// Copyright (c) 2024, Athru Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Room", {
// 	refresh(frm) {

// 	},
// });




frappe.ui.form.on('Room', {
    refresh: function(frm) {
        // Check conditions before adding the button on page load
        addBookButton(frm);

        // Trigger the function when room_status or docstatus changes
        frm.fields_dict['room_status'].$input.on('change', function() {
            addBookButton(frm);
        });

        frm.fields_dict['docstatus'].$input.on('change', function() {
            addBookButton(frm);
        });
    }
});

function addBookButton(frm) {
    // Check conditions before adding the button
    if (frm.doc.room_status === 'Available' && frm.doc.docstatus === 1) {
        // Add a button below the room_type field
        frm.fields_dict['room_type'].$wrapper.find('#bookRoomBtn').remove(); // Remove existing button
        frm.fields_dict['room_type'].$wrapper.append(
            `<div class="row">
                <div class="col-md-12">
                    <button class="btn btn-default btn-xs" id="bookRoomBtn">Book Room</button>
                </div>
            </div>`
        );

        // Bind click event to the button using Frappe's client script
        frm.fields_dict['room_type'].$wrapper.find('#bookRoomBtn').on('click', function() {
            bookRoom(frm);
        });
    } else {
        // Remove the button if conditions are not met
        frm.fields_dict['room_type'].$wrapper.find('#bookRoomBtn').remove();
    }
}

function bookRoom(frm) {
    // Create a new "Room Booking" document
    frappe.new_doc('Room Booking').then(function(newDoc) {
        // Set the 'room' field in the 'room_table'
        newDoc.room_table = [{
            'room': frm.doc.name
            // Add other fields as needed
        }];

        // Save the new document
        newDoc.save().then(function() {
            frappe.msgprint('Room Booking created successfully.');
        });
    });
}