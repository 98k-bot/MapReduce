# MapReduce

run with 
"cat NYPD2.csv | python mapper.py |sort| python reducer.py"

We can get:

ADMINISTRATIVE CODE	BRONX	722
most of the crime happening in BRONX for 722 times, the type is ADMINISTRATIVE CODE
ADMINISTRATIVE CODES	QUEENS	1
ADMINISTRATIVE CODE	STATEN ISLAND	37
AGRICULTURE & MRKTS LAW-UNCLASSIFIED	BRONX	108
ALCOHOLIC BEVERAGE CONTROL LAW	BRONX	75
ANTICIPATORY OFFENSES	MANHATTAN	2
ARSON	BRONX	613
ASSAULT 3 & RELATED OFFENSES	BRONX	39977
most of the crime happening in BRONX for 39977 times, the type is ASSAULT 3 & RELATED OFFENSES
BURGLAR'S TOOLS	BRONX	205
BURGLARY	BRONX	9635
CHILD ABANDONMENT/NON SUPPORT	BRONX	16
CRIMINAL MISCHIEF & RELATED OF	BRONX	37618
CRIMINAL TRESPASS	BRONX	3001
DANGEROUS DRUGS	BRONX	17188
DANGEROUS WEAPONS	BRONX	8058
DISORDERLY CONDUCT	BRONX	66
DISRUPTION OF A RELIGIOUS SERV	BROOKLYN	3
ENDAN WELFARE INCOMP	BRONX	25
ESCAPE 3	BRONX	7
FELONY ASSAULT	BRONX	15869
FORGERY	BRONX	4585
FRAUDS	BRONX	2626
FRAUDULENT ACCOSTING	BRONX	179
GAMBLING	BRONX	224
GRAND LARCENY	BRONX	25358
GRAND LARCENY OF MOTOR VEHICLE	BRONX	4767
GRAND LARCENY	QUEENS	7203
HARRASSMENT 2	BRONX	49907
most of the crime happening in BRONX for 49907 times, the type is HARRASSMENT 2
HOMICIDE-NEGLIGENT UNCLASSIFIE	BRONX	3
HOMICIDE-NEGLIGENT-VEHICLE	BROOKLYN	1
INTOXICATED & IMPAIRED DRIVING	BRONX	4423
JOSTLING	BRONX	35
KIDNAPPING	BROOKLYN	4
KIDNAPPING & RELATED OFFENSES	BRONX	107
LOITERING/GAMBLING (CARDS  DIC	BROOKLYN	7
MISCELLANEOUS PENAL LAW	BRONX	10560
MURDER & NON-NEGL. MANSLAUGHTER	BRONX	263
NEW YORK CITY HEALTH CODE	BROOKLYN	4
NYS LAWS-UNCLASSIFIED FELONY	BRONX	528
NYS LAWS-UNCLASSIFIED VIOLATION	BRONX	14
OFF. AGNST PUB ORD SENSBLTY &	BRONX	17401
OFFENSES AGAINST PUBLIC ADMINI	BRONX	6911
OFFENSES AGAINST PUBLIC SAFETY	BRONX	48
OFFENSES AGAINST THE PERSON	BRONX	945
OFFENSES INVOLVING FRAUD	BRONX	947
OFFENSES RELATED TO CHILDREN	BRONX	76
OFNS_DESC	BORO_NM	1
OTHER OFFENSES RELATED TO THEF	BRONX	1275
OTHER STATE LAWS	BRONX	8
OTHER STATE LAWS (NON PENAL LA	BRONX	176
OTHER STATE LAWS (NON PENAL LAW)	BROOKLYN	3
OTHER STATE LAWS	QUEENS	6
PETIT LARCENY	BRONX	46937
PETIT LARCENY OF MOTOR VEHICLE	BRONX	27
PETIT LARCENY	QUEENS	13913
POSSESSION OF STOLEN PROPERTY	BRONX	1265
PROSTITUTION & RELATED OFFENSES	BRONX	102
RAPE	BRONX	1107
ROBBERY	BRONX	11472
SEX CRIMES	BRONX	4739
THEFT-FRAUD	BRONX	3703
THEFT OF SERVICES	BRONX	327
UNAUTHORIZED USE OF A VEHICLE	BRONX	1338
UNLAWFUL POSS. WEAP. ON SCHOOL	BROOKLYN	2
VEHICLE AND TRAFFIC LAWS	BRONX	4950


"cat NYPD2.csv | python mapper2.py |sort| python reducer2.py"
We can get:
"
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1486]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1490]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1492]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1497]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1497]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1497]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1499]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1532]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1532]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1549]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1551]
MURDER & NON-NEGL. MANSLAUGHTER	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1551]
NYS LAWS-UNCLASSIFIED FELONY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1551]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1564]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1600]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1600]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1601]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1609]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1611]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1612]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1612]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1612]
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1612]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1614]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1618]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1623]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1626]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1628]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1656]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1656]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1669]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1670]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1680]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1680]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1707]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1707]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1711]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
THEFT OF SERVICES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
ADMINISTRATIVE CODE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
AGRICULTURE & MRKTS LAW-UNCLASSIFIED	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1712]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1716]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1718]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1727]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1729]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1731]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1740]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1754]
INTOXICATED & IMPAIRED DRIVING	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1754]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1755]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1765]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1769]
OTHER OFFENSES RELATED TO THEF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1769]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1789]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1789]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
ADMINISTRATIVE CODE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1794]
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1795]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1797]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1799]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1804]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1805]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1808]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1808]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1824]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1830]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1831]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1845]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1846]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1869]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1871]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1877]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1877]
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1877]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1879]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1881]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1887]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1889]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1891]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1909]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1911]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1918]
INTOXICATED & IMPAIRED DRIVING	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1918]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1918]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1922]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1951]
ROBBERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1951]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1951]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1958]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1961]
VEHICLE AND TRAFFIC LAWS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1961]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1961]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1961]
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1961]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1963]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1965]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1969]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1970]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1971]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 1975]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2016]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2018]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2028]
KIDNAPPING & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2028]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2032]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2042]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2044]
OTHER OFFENSES RELATED TO THEF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2044]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2070]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2070]
ROBBERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2070]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2071]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2085]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2088]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2088]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2089]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2089]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2092]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2097]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2104]
CRIMINAL TRESPASS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2104]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2105]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2105]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2107]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2134]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2136]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2150]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2153]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2159]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2161]
OTHER OFFENSES RELATED TO THEF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2161]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2194]
POSSESSION OF STOLEN PROPERTY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2194]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2195]
ROBBERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2195]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2196]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2200]
VEHICLE AND TRAFFIC LAWS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2200]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2200]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2200]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2200]
ARSON	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2200]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2201]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2207]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2223]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2228]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2231]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2235]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2272]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2279]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2296]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2304]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2322]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2325]
OTHER OFFENSES RELATED TO THEF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2326]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2373]
POSSESSION OF STOLEN PROPERTY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2373]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2374]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2385]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2390]
ASSAULT 3 & RELATED OFFENSES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2424]
BURGLARY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2451]
CRIMINAL MISCHIEF & RELATED OF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2498]
CRIMINAL TRESPASS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2498]
DANGEROUS DRUGS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2498]
DANGEROUS WEAPONS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2501]
FELONY ASSAULT	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2509]
FORGERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2510]
FRAUDS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2513]
GRAND LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2586]
GRAND LARCENY OF MOTOR VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2599]
HARRASSMENT 2	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2634]
INTOXICATED & IMPAIRED DRIVING	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2634]
MISCELLANEOUS PENAL LAW	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2643]
NYS LAWS-UNCLASSIFIED FELONY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2643]
OFF. AGNST PUB ORD SENSBLTY &	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2667]
OFFENSES AGAINST PUBLIC ADMINI	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2675]
OTHER OFFENSES RELATED TO THEF	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2675]
PETIT LARCENY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2743]
RAPE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2744]
ROBBERY	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2746]
SEX CRIMES	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2750]
THEFT-FRAUD	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2755]
UNAUTHORIZED USE OF A VEHICLE	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2757]
VEHICLE AND TRAFFIC LAWS	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2759]
OFNS_DESC	[36934, 33524, 38401, 38268, 40537, 40278, 39993, 40534, 35721, 473, 757, 2759] 

"
