r1 = ('Customer', 'City', 'Contract Number', 'Date', 'Contact Manager')
l1 = ('Intersection', 'Magnet', 'Perspective Korp.', 'Driveway', 'near', 'Nori', 'Nevsky comp.', 'Perspective korp.', 'in touch', 'Nardis')
l2 = ('New York', 'New York', 'Minsk', 'New York', 'Los Angeles', 'Tokyo', 'Moscow', 'Minsk', 'San Francisco', 'Tokyo')
l3 = ('2314589', '2432656', '2456983', '2408570', '2481553', '2506369', '2337735', '236112', '2384723', '2531433')
l4 = ('12.12.2012', '27.08.2014', '31.12.2014', '24.04.2014', '06.05.2015', '09.09.2015', '15.04.2013', '17.08.2013', '20.12.2013','14.01.2016')
l5 = ('Aaron', 'Alex', 'Ashley', 'Aaron', 'Ashley', 'Blake', 'Caroline', 'Daniel', 'Alex', 'Blake')

zipped_lists = zip(l1,l2,l3,l4,l5)

for row in zipped_lists:print(row)