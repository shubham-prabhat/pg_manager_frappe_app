// Copyright (c) 2024, Athru Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Room Booking", {
// 	refresh(frm) {

// 	},
// });

// // //  Below Script is populatin the Room details in the "room_table" perfectly

frappe.ui.form.on('Room Booking Table', {
    room: function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        var selectedRoom = row.room;

        // Fetch details from the 'Room' document based on the selected room
        frappe.call({
            method: 'pg_manager.pg_manager.doctype.room_booking_table.room_booking_table.get_room_details',
            args: { room: selectedRoom },
            callback: function(response) {
                var roomDetails = response.message;

                // Update fields in the 'Room Booking Table' child table
                frappe.model.set_value(cdt, cdn, 'room_type', roomDetails.room_type);
                frappe.model.set_value(cdt, cdn, 'room_no', roomDetails.custom_room_number);
                frappe.model.set_value(cdt, cdn, 'floor_no', roomDetails.floor_no);

                // Fetch the room_pricing value
                frappe.call({
                    method: 'pg_manager.pg_manager.doctype.room_booking_table.room_booking_table.get_room_pricing',
                    args: { room: selectedRoom },
                    callback: function(response) {
                        var roomPricing = response.message;
                        frappe.model.set_value(cdt, cdn, 'room_rent', roomPricing);
                    }
                });
            }
        });
    }
});









frappe.ui.form.on('Room Booking', {
    refresh: function(frm) {
        frm.fields_dict['room_table'].grid.get_field('room').get_query = function(doc, cdt, cdn) {
            // Restrict 'room' options if it's already selected in any row
            var selected_rooms = frm.doc.room_table.map(row => row.room);
            return {
                filters: {
                    name: ['not in', selected_rooms],
                    room_status: ['not in', "Occupied"]
                }
            };
        };
    }
});





//  // // setting the field value to  'Select' and '0.00' on localin respective fields 'booking_status' and 'total_room_rent'

frappe.ui.form.on('Room Booking', {
    refresh: function(frm) {
        // Check if the form is in insert mode or if it's a local document
        if (frm.doc.__islocal || frm.doc.__unsaved) {
            // Set the "room_status" field to "Select"
            frm.set_value('booking_status', 'Select');
            frm.set_value('total_room_rent', '0.00');
        }
    }
});




//  // Updating the 'total_rent_field' with 'room_rent' field value on adding and deleting the room 

frappe.ui.form.on('Room Booking', {
    refresh: function(frm) {
        // Tri/apps/bench/frappe/apps/pg_manager/pg_manager/pg_manager/doctype/room_bookinggger the function whenever the form is refreshed
        frm.fields_dict['room_table'].grid.on('after_table_render', function(doc) {
            // Calculate total_room_rent and update the field in real-time
            updateTotalRoomRent(frm);
        });
    }
});


frappe.ui.form.on('Room Booking Table', {
    room_rent: function(frm, cdt, cdn) {
        // Trigger the function whenever the room_rent field is changed
        updateTotalRoomRent(frm);
    },
    room_table_remove: function(frm, cdt, cdn) {
        // Trigger the function whenever a row is deleted
        updateTotalRoomRent(frm);
    }
});

function updateTotalRoomRent(frm) {
    // Calculate total_room_rent based on the sum of room_rent in each row
    let totalRoomRent = 0;
    $.each(frm.doc.room_table || [], function(index, row) {
        totalRoomRent += row.room_rent || 0;
    });

    // Update the total_room_rent field in real-time
    frm.set_value('total_room_rent', totalRoomRent);
    frm.refresh_field('total_room_rent');
}


// // // End the script here for 'toatl_roo_rent' field value








// // validating the 'customer_identity_number' field value
frappe.ui.form.on('Room Booking', {
    validate: function(frm) {
        var d = frm.doc;

        if (d.customer_identity == "Aadhar No." && d.customer_identity_number.length !== 12) {
            frappe.msgprint(("For 'Aadhar No.', the 'customer_identity_number' should be 12 characters long"));
            frappe.validated = false;
        } else if (d.customer_identity == "Voter ID No." && d.customer_identity_number.length !== 16) {
            frappe.msgprint(("For 'Voter ID No.', the 'customer_identity_number' should be 16 characters long"));
            frappe.validated = false;
        } else if (d.customer_identity == "Driving Licence No." && d.customer_identity_number.length !== 14) {
            frappe.msgprint(("For 'Driving Licence No.', the 'customer_identity_number' should be 14 characters long"));
            frappe.validated = false;
        }
    }
});







// // validating the 'customer_email' field value

frappe.ui.form.on('Room Booking', {
    validate: function(frm) {
        var email = frm.doc.customer_email;

        if (email && !validateEmail(email)) {
            frappe.msgprint(__('Please enter a valid email address for Customer Email.'));
            frappe.validated = false;
        }
    }
});

function validateEmail(email) {
    // Basic email validation using a regular expression
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}


