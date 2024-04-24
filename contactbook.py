import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added successfully")
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_term = search_entry.get()
    search_results = [contact for contact in contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]
    contact_list.delete(0, tk.END)
    for contact in search_results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to update")
        return
    index = selected_contact[0]
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", "Contact updated successfully")
    clear_entries()
    view_contacts()

def delete_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to delete")
        return
    index = selected_contact[0]
    del contacts[index]
    messagebox.showinfo("Success", "Contact deleted successfully")
    view_contacts()

root = tk.Tk()
root.title("Contact Information")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()
tk.Button(root, text="View Contacts", command=view_contacts).pack()
tk.Button(root, text="Search Contact", command=search_contact).pack()
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()

tk.Label(root, text="Search:").pack()
search_entry = tk.Entry(root)
search_entry.pack()

contact_list = tk.Listbox(root)
contact_list.pack()

root.mainloop()
