import frappe

@frappe.whitelist()
def get_item_details(name=None):
    return frappe.db.sql(f"""select item_name from `tabItem` where owner='Administrator';""", as_dict=True)
