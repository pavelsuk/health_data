from datetime import datetime
from xml.dom import minidom


dat = minidom.parse("P:\\dev\\_projects\\github\\health_data\\export_20210725\\apple_health_export\\export.xml")
records = dat.getElementsByTagName('Record')
oneDay = endDate = None
walkingInDay = 0.0

# print(records)
for record in records:
    if record.getAttribute('type') == "HKQuantityTypeIdentifierDistanceWalkingRunning":
        endDateTime = datetime.strptime(record.getAttribute('endDate'), "%Y-%m-%d %H:%M:%S %z")
        endDate = endDateTime.date()
        value = float(record.getAttribute('value'))
        unit = record.getAttribute('unit')
        if (not oneDay):
            oneDay = endDate

        if oneDay == endDate:
            walkingInDay += value
        else:
            print('{date}\t {value}{unit}'.format(date=oneDay, value=walkingInDay, unit=unit))
            walkingInDay = 0
            oneDay = endDate


if oneDay == endDate:
    print('{date}\t {value}{unit}'.format(date=oneDay, value=walkingInDay, unit=unit))


