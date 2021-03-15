def create_kst_xml(file_name, path):
    file_name_csv = file_name.rsplit("\\", 1)[0] + "\\VTEMExtracted.csv"
    file_name_dat = path + '\\kst.dat'
    file_name_kst = file_name.rsplit("\\", 1)[0] + "\\PlotEM.kst"

    import xml.etree.ElementTree as ET

    tree = ET.parse(file_name_dat)
    root = tree.getroot()

    for data in root.iter('source'):
        data.attrib['file'] = file_name_csv

    for data in root.iter('datavector'):
        data.attrib['file'] = file_name_csv

    tree.write(file_name_kst)
