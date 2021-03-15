def create_kml(input_file):
    import csv
    data = []

    with open(input_file, newline='') as csvfile:
        data_file = csv.reader(csvfile, delimiter=' ')
        # data_file = csv.reader(csvfile)
        for row in data_file:
            data += row

    # Skip the 1st header row.
    data = data[1:]

    file_out = input_file.rsplit("\\", 1)[0] + "\\Flightpath.kml"

    f = open(file_out, 'w')

    # Writing the kml file.
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
    f.write("<Placemark>\n")
    f.write("	<name>Flightpath</name>\n")
    f.write("	<open>1</open>\n")
    f.write("	<Style>\n")
    f.write("		<LineStyle>\n")
    f.write("			<color>ffffff00</color>\n")
    f.write("			<width>4</width>\n")
    f.write("		</LineStyle>\n")
    f.write("	</Style>\n")
    f.write("	<MultiGeometry>\n")
    f.write("		<altitudeMode>absolute</altitudeMode>\n")
    f.write("		<LineString>\n")
    f.write("			<altitudeMode>absolute</altitudeMode>\n")
    f.write("			<coordinates>\n")

    space = " " * 24

    for row in data:
        f.write(space + str(row.split(",")[3]) + "," + str(row.split(",")[2])
                + "," + str(row.split(",")[4]) + "\n")

    f.write("\n")
    f.write("			</coordinates>\n")
    f.write("		</LineString>\n")
    f.write("	</MultiGeometry>\n")
    f.write("</Placemark>\n")
    f.write("</kml>")

    print("KML File Created. from {} line".format(str(len(data))))
    f.close()
