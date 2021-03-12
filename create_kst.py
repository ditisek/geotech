def create_kst(file_name):
    file_name_kst = file_name.rsplit("\\", 1)[0] + '\\PlotEM.kst'
    file_name = file_name.replace("\\", "/")
    fout = open(file_name_kst, 'w')
    fout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fout.write('<kst version="2.0">\n')
    fout.write('    <data>\n')
    fout.write('        <source reader="ASCII file" updateType="0" file="'
               + file_name + '">\n')
    fout.write('            <properties vector="INDEX" interpretation="1" '
               'delimiters="#" columntype="2" columndelimiter="," '
               'headerstart="1" fields="0" readfields="true" usedot="true" '
               'columnwidthisconst="false" readunits="false" units="0" '
               'limitFileBuffer="false" limitFileBufferSize="0" useThreads="0" '
               'asciiTimeFormat="hh:mm:ss.zzz" dataRate="1" '
               'offsetDateTime="false" offsetFileDate="false" '
               'offsetRelavive="true" dateTimeOffset="2017-12-13T07:10:24Z" '
               'relativeOffset="0" nanValue="0" updateType="0"/>\n')
    fout.write('        </source>\n')
    fout.write('    </data>\n')
    fout.write('    <variables>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="INDEX" start="1" '
                'count="-1" skip="-1" doAve="false" startUnits="" '
                'rangeUnits="" initialVNum="1" initialXNum="1"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="lno" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="2" initialXNum="13"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="height" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="3" initialXNum="25"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="nosats" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="4" initialXNum="37"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="ralt" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="5" initialXNum="49"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pkir" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="6" initialXNum="61"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pkbx" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="7" initialXNum="73"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pkbz" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="8" initialXNum="85"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pkvr" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="9" initialXNum="97"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pksx" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="10" initialXNum="109"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pksz" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="11" initialXNum="121"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srz15" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="12" initialXNum="133"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srz24" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="13" initialXNum="145"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srz33" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="14" initialXNum="157"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srz44" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="15" initialXNum="169"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="brz15" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="16" initialXNum="181"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="brz24" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="17" initialXNum="193"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="brz33" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="18" initialXNum="205"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="brz44" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="19" initialXNum="217"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srx15" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="20" initialXNum="229"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srx24" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="21" initialXNum="241"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srx33" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="22" initialXNum="253"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="srx44" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="23" initialXNum="265"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="rf15" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="24" initialXNum="277"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="rf24" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="25" initialXNum="289"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="rf33" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="26" initialXNum="301"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="rf44" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="27" initialXNum="313"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="pwline" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="28" initialXNum="325"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="mag1" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="29" initialXNum="337"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="mag2" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="30" initialXNum="349"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="speed" start="1" '
                 'count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="31" initialXNum="361"/>\n')
    fout.write('        <datavector file="' + file_name
               + '" fileRelative="VTEMExtracted.csv" field="climbrate" '
                 'start="1" count="-1" skip="-1" doAve="false" startUnits="" '
                 'rangeUnits="" initialVNum="32" initialXNum="373"/>\n')
    fout.write('        <scalar orphan="true" hidden="true" value="0.001" '
               'initialXNum="385"/>\n')
    fout.write('        <scalar orphan="true" hidden="true" value="4" '
               'initialXNum="386"/>\n')
    fout.write('        <scalar orphan="true" hidden="true" value="0.01" '
               'initialXNum="409"/>\n')
    fout.write('        <scalar orphan="true" hidden="true" value="0.005" '
               'initialXNum="410"/>\n')
    fout.write('    </variables>\n')
    fout.close()
    fadd = open('kst.dat', 'r')

    data = []

    for line in fadd:
        data.append(line)

    print()
    fadd.close()
    fout = open(file_name_kst, 'a')
    for line in data:
        fout.write(line)
    fout.close()
