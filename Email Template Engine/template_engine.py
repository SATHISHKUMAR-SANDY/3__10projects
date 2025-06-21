# from string import Template

# def load_template():
#     # Directly assign template string (no file needed)
#     template_string = """
#     Hi $name,

#     Your order $order_id has been shipped on $ship_date.

#     Thanks,
#     $company
#     """
#     return Template(template_string)

# def generate_email(template, values_dict):
#     return template.safe_substitute(values_dict)

# if __name__ == "__main__":
#     # Load the email template (now it's hardcoded in the function)
#     template = load_template()

#     # Example data for one recipient
#     data = {
#         "name": "Alice",
#         "order_id": "12345",
#         "ship_date": "2025-06-20",
#         "company": "SuperStore"
#     }

#     # Inject values into the template
#     final_email = generate_email(template, data)

#     # Print the final generated email
#     print("\n📧 Final Email:\n")
#     print(final_email)
