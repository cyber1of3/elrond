#!/usr/bin/env python3 -tt
def create_nav_menu(defaultnav):
    defaultnav.write('<collection label="MITRE">\n		')
    defaultnav.write('<view name="mitre" default="true" />\n		')
    defaultnav.write(
        '<a href="http://127.0.0.1:4200" target="_blank">ATT&amp;CK® Navigator Mapping</a>\n		'
    )
    defaultnav.write('<view name="info" />\n	')
    defaultnav.write("</collection>\n	")
    defaultnav.write('<collection label="ATT&amp;CK® Techniques">\n		')
    defaultnav.write('<collection label="Initial Access">\n			')
    defaultnav.write('<view name="t1189" />\n			')
    defaultnav.write('<view name="t1190" />\n			')
    defaultnav.write('<view name="t1133" />\n			')
    defaultnav.write('<view name="t1200" />\n			')
    defaultnav.write('<view name="t1566" />\n			')
    defaultnav.write('<view name="t1091" />\n			')
    defaultnav.write('<view name="t1195" />\n			')
    defaultnav.write('<view name="t1199" />\n			')
    defaultnav.write('<view name="t1078" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Execution">\n			')
    defaultnav.write('<view name="t1059" />\n			')
    defaultnav.write('<view name="t1609" />\n			')
    defaultnav.write('<view name="t1610" />\n			')
    defaultnav.write('<view name="t1203" />\n			')
    defaultnav.write('<view name="t1559" />\n			')
    defaultnav.write('<view name="t1106" />\n			')
    defaultnav.write('<view name="t1053" />\n			')
    defaultnav.write('<view name="t1129" />\n			')
    defaultnav.write('<view name="t1072" />\n			')
    defaultnav.write('<view name="t1569" />\n			')
    defaultnav.write('<view name="t1204" />\n			')
    defaultnav.write('<view name="t1047" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Persistence">\n			')
    defaultnav.write('<view name="t1098" />\n			')
    defaultnav.write('<view name="t1197" />\n			')
    defaultnav.write('<view name="t1547" />\n			')
    defaultnav.write('<view name="t1037" />\n			')
    defaultnav.write('<view name="t1176" />\n			')
    defaultnav.write('<view name="t1554" />\n			')
    defaultnav.write('<view name="t1136" />\n			')
    defaultnav.write('<view name="t1543" />\n			')
    defaultnav.write('<view name="t1546" />\n			')
    defaultnav.write('<view name="t1133" />\n			')
    defaultnav.write('<view name="t1574" />\n			')
    defaultnav.write('<view name="t1525" />\n			')
    defaultnav.write('<view name="t1556" />\n			')
    defaultnav.write('<view name="t1137" />\n			')
    defaultnav.write('<view name="t1542" />\n			')
    defaultnav.write('<view name="t1053" />\n			')
    defaultnav.write('<view name="t1505" />\n			')
    defaultnav.write('<view name="t1205" />\n			')
    defaultnav.write('<view name="t1078" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Privilege Escalation">\n			')
    defaultnav.write('<view name="t1548" />\n			')
    defaultnav.write('<view name="t1134" />\n			')
    defaultnav.write('<view name="t1547" />\n			')
    defaultnav.write('<view name="t1037" />\n			')
    defaultnav.write('<view name="t1543" />\n			')
    defaultnav.write('<view name="t1484" />\n			')
    defaultnav.write('<view name="t1611" />\n			')
    defaultnav.write('<view name="t1546" />\n			')
    defaultnav.write('<view name="t1068" />\n			')
    defaultnav.write('<view name="t1574" />\n			')
    defaultnav.write('<view name="t1055" />\n			')
    defaultnav.write('<view name="t1053" />\n			')
    defaultnav.write('<view name="t1078" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Defense Evasion">\n			')
    defaultnav.write('<view name="t1548" />\n			')
    defaultnav.write('<view name="t1134" />\n			')
    defaultnav.write('<view name="t1197" />\n			')
    defaultnav.write('<view name="t1612" />\n			')
    defaultnav.write('<view name="t1622" />\n			')
    defaultnav.write('<view name="t1140" />\n			')
    defaultnav.write('<view name="t1642" />\n			')
    defaultnav.write('<view name="t1610" />\n			')
    defaultnav.write('<view name="t1006" />\n			')
    defaultnav.write('<view name="t1480" />\n			')
    defaultnav.write('<view name="t1211" />\n			')
    defaultnav.write('<view name="t1222" />\n			')
    defaultnav.write('<view name="t1484" />\n			')
    defaultnav.write('<view name="t1564" />\n			')
    defaultnav.write('<view name="t1574" />\n			')
    defaultnav.write('<view name="t1562" />\n			')
    defaultnav.write('<view name="t1070" />\n			')
    defaultnav.write('<view name="t1202" />\n			')
    defaultnav.write('<view name="t1036" />\n			')
    defaultnav.write('<view name="t1556" />\n			')
    defaultnav.write('<view name="t1578" />\n			')
    defaultnav.write('<view name="t1112" />\n			')
    defaultnav.write('<view name="t1601" />\n			')
    defaultnav.write('<view name="t1599" />\n			')
    defaultnav.write('<view name="t1027" />\n			')
    defaultnav.write('<view name="t1647" />\n			')
    defaultnav.write('<view name="t1542" />\n			')
    defaultnav.write('<view name="t1055" />\n			')
    defaultnav.write('<view name="t1620" />\n			')
    defaultnav.write('<view name="t1207" />\n			')
    defaultnav.write('<view name="t1014" />\n			')
    defaultnav.write('<view name="t1218" />\n			')
    defaultnav.write('<view name="t1216" />\n			')
    defaultnav.write('<view name="t1553" />\n			')
    defaultnav.write('<view name="t1221" />\n			')
    defaultnav.write('<view name="t1205" />\n			')
    defaultnav.write('<view name="t1127" />\n			')
    defaultnav.write('<view name="t1535" />\n			')
    defaultnav.write('<view name="t1550" />\n			')
    defaultnav.write('<view name="t1078" />\n			')
    defaultnav.write('<view name="t1497" />\n			')
    defaultnav.write('<view name="t1600" />\n			')
    defaultnav.write('<view name="t1220" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Credential Access">\n			')
    defaultnav.write('<view name="t1110" />\n			')
    defaultnav.write('<view name="t1555" />\n			')
    defaultnav.write('<view name="t1212" />\n			')
    defaultnav.write('<view name="t1187" />\n			')
    defaultnav.write('<view name="t1606" />\n			')
    defaultnav.write('<view name="t1056" />\n			')
    defaultnav.write('<view name="t1557" />\n			')
    defaultnav.write('<view name="t1556" />\n			')
    defaultnav.write('<view name="t1040" />\n			')
    defaultnav.write('<view name="t1003" />\n			')
    defaultnav.write('<view name="t1528" />\n			')
    defaultnav.write('<view name="t1539" />\n			')
    defaultnav.write('<view name="t1111" />\n			')
    defaultnav.write('<view name="t1621" />\n			')
    defaultnav.write('<view name="t1552" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Discovery">\n			')
    defaultnav.write('<view name="t1087" />\n			')
    defaultnav.write('<view name="t1010" />\n			')
    defaultnav.write('<view name="t1217" />\n			')
    defaultnav.write('<view name="t1580" />\n			')
    defaultnav.write('<view name="t1538" />\n			')
    defaultnav.write('<view name="t1526" />\n			')
    defaultnav.write('<view name="t1613" />\n			')
    defaultnav.write('<view name="t1622" />\n			')
    defaultnav.write('<view name="t1642" />\n			')
    defaultnav.write('<view name="t1482" />\n			')
    defaultnav.write('<view name="t1083" />\n			')
    defaultnav.write('<view name="t1615" />\n			')
    defaultnav.write('<view name="t1046" />\n			')
    defaultnav.write('<view name="t1135" />\n			')
    defaultnav.write('<view name="t1040" />\n			')
    defaultnav.write('<view name="t1201" />\n			')
    defaultnav.write('<view name="t1120" />\n			')
    defaultnav.write('<view name="t1069" />\n			')
    defaultnav.write('<view name="t1057" />\n			')
    defaultnav.write('<view name="t1012" />\n			')
    defaultnav.write('<view name="t1018" />\n			')
    defaultnav.write('<view name="t1518" />\n			')
    defaultnav.write('<view name="t1082" />\n			')
    defaultnav.write('<view name="t1614" />\n			')
    defaultnav.write('<view name="t1016" />\n			')
    defaultnav.write('<view name="t1049" />\n			')
    defaultnav.write('<view name="t1033" />\n			')
    defaultnav.write('<view name="t1007" />\n			')
    defaultnav.write('<view name="t1124" />\n			')
    defaultnav.write('<view name="t1497" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Lateral Movement">\n			')
    defaultnav.write('<view name="t1210" />\n			')
    defaultnav.write('<view name="t1534" />\n			')
    defaultnav.write('<view name="t1570" />\n			')
    defaultnav.write('<view name="t1563" />\n			')
    defaultnav.write('<view name="t1021" />\n			')
    defaultnav.write('<view name="t1091" />\n			')
    defaultnav.write('<view name="t1072" />\n			')
    defaultnav.write('<view name="t1080" />\n			')
    defaultnav.write('<view name="t1550" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Collection">\n			')
    defaultnav.write('<view name="t1560" />\n			')
    defaultnav.write('<view name="t1123" />\n			')
    defaultnav.write('<view name="t1119" />\n			')
    defaultnav.write('<view name="t1115" />\n			')
    defaultnav.write('<view name="t1530" />\n			')
    defaultnav.write('<view name="t1602" />\n			')
    defaultnav.write('<view name="t1213" />\n			')
    defaultnav.write('<view name="t1005" />\n			')
    defaultnav.write('<view name="t1039" />\n			')
    defaultnav.write('<view name="t1025" />\n			')
    defaultnav.write('<view name="t1074" />\n			')
    defaultnav.write('<view name="t1114" />\n			')
    defaultnav.write('<view name="t1056" />\n			')
    defaultnav.write('<view name="t1185" />\n			')
    defaultnav.write('<view name="t1557" />\n			')
    defaultnav.write('<view name="t1113" />\n			')
    defaultnav.write('<view name="t1125" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Command &amp; Control">\n			')
    defaultnav.write('<view name="t1071" />\n			')
    defaultnav.write('<view name="t1092" />\n			')
    defaultnav.write('<view name="t1132" />\n			')
    defaultnav.write('<view name="t1001" />\n			')
    defaultnav.write('<view name="t1568" />\n			')
    defaultnav.write('<view name="t1573" />\n			')
    defaultnav.write('<view name="t1008" />\n			')
    defaultnav.write('<view name="t1105" />\n			')
    defaultnav.write('<view name="t1104" />\n			')
    defaultnav.write('<view name="t1095" />\n			')
    defaultnav.write('<view name="t1571" />\n			')
    defaultnav.write('<view name="t1572" />\n			')
    defaultnav.write('<view name="t1090" />\n			')
    defaultnav.write('<view name="t1219" />\n			')
    defaultnav.write('<view name="t1205" />\n			')
    defaultnav.write('<view name="t1102" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Exfiltration">\n			')
    defaultnav.write('<view name="t1020" />\n			')
    defaultnav.write('<view name="t1030" />\n			')
    defaultnav.write('<view name="t1048" />\n			')
    defaultnav.write('<view name="t1041" />\n			')
    defaultnav.write('<view name="t1011" />\n			')
    defaultnav.write('<view name="t1052" />\n			')
    defaultnav.write('<view name="t1567" />\n			')
    defaultnav.write('<view name="t1029" />\n			')
    defaultnav.write('<view name="t1537" />\n			')
    defaultnav.write("</collection>\n		")
    defaultnav.write('<collection label="Impact">\n			')
    defaultnav.write('<view name="t1531" />\n			')
    defaultnav.write('<view name="t1485" />\n			')
    defaultnav.write('<view name="t1486" />\n			')
    defaultnav.write('<view name="t1565" />\n			')
    defaultnav.write('<view name="t1491" />\n			')
    defaultnav.write('<view name="t1561" />\n			')
    defaultnav.write('<view name="t1499" />\n			')
    defaultnav.write('<view name="t1495" />\n			')
    defaultnav.write('<view name="t1490" />\n			')
    defaultnav.write('<view name="t1498" />\n			')
    defaultnav.write('<view name="t1496" />\n			')
    defaultnav.write('<view name="t1489" />\n			')
    defaultnav.write('<view name="t1529" />\n			')
    defaultnav.write("</collection>\n	</collection>\n	")
