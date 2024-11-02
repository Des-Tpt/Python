from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement


employees = collection.getElementsByTagName("employee")

print("ID\tName")
for employee in employees:
    tag_id = employee.getElementsByTagName('id')[0]
    emp_id = tag_id.childNodes[0].data 

    tag_name = employee.getElementsByTagName('name')[0]
    name = tag_name.childNodes[0].data  

    print(emp_id, '\t', name)
