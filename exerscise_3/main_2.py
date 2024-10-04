from lxml import etree
from pathlib import Path

data_dir = Path.cwd() / 'data'

output_file = data_dir / 'sample_5.xml'

root = etree.Element("Patients")

to = etree.SubElement(root, "patient", attrib={"id": "001"})

firstname_ = etree.SubElement(to, "firstname")
firstname_.text = "John"

lastname_ = etree.SubElement(to, "lastname")
lastname_.text = "Doe"

age_ = etree.SubElement(to, "age")
age_.text = "45"

gender_ = etree.SubElement(to, "gender")
gender_.text = "Male"

diagnosis_ = etree.SubElement(to, "diagnosis")
diagnosis_.text = "Hypertension"


medications_ = etree.SubElement(to, "medications")
med1_ = etree.SubElement(medications_, "medication")
med1_.text = "Lisinopril"
med2_ = etree.SubElement(medications_, "medication")
med2_.text = "Amlodipine"

to = etree.SubElement(root, "patient", attrib={"id": "002"})

# Add first name, last name, and other details for the second patient
firstname_ = etree.SubElement(to, "first_name")
firstname_.text = "Jane"

lastname_ = etree.SubElement(to, "last_name")
lastname_.text = "Smith"

age_ = etree.SubElement(to, "age")
age_.text = "37"

gender_ = etree.SubElement(to, "gender")
gender_.text = "Female"

diagnosis_ = etree.SubElement(to, "diagnosis")
diagnosis_.text = "Diabetes"


medications_ = etree.SubElement(to, "medications")
med1_ = etree.SubElement(medications_, "medication")
med1_.text = "Metformin"
med2_ = etree.SubElement(medications_, "medication")
med2_.text = "Insulin"

tree = etree.ElementTree(root)


with open(output_file, "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))