def create_kst_xml(output_path, path):
    file_name_kst = output_path + '\\PlotEM.kst'
    file_name_dat = path + '\\kst.dat'
    file_name_csv = output_path.replace("\\", "/") + "/VTEMExtracted.csv"

    import xml.etree.ElementTree as ET

    tree = ET.parse(file_name_dat)
    root = tree.getroot()

    # for child in root:
    #     print(child.tag, child.attrib)

    # print(ET.tostring(root, encoding='utf8').decode('utf8'))    # Print file as is

    for data in root.iter('source'):
        # print(data.attrib)
        # print(data.attrib['file'])
        data.attrib['file'] = file_name_csv
        # print(data.attrib['file'])

    for data in root.iter('datavector'):
        # print(data.attrib)
        # print(data.attrib['file'])
        data.attrib['file'] = file_name_csv
        # print(data.attrib['file'])

    tree.write(file_name_kst)
