data = {
    'No': [1,2,3,4,5],
    'Customer':['Intersection', 'Magnet' , 'Perspective corp.', 'Driveway', 'Near'],
    'Country':['USA' ,'Belarus', 'Canada', 'USA' , 'USA'],
    'City':['New York', 'Los Angeles', 'Chicago', 'Austin', 'Miami'],
    'Contact Manager':['Aaron', 'Alex', 'Ashley', 'Blake', 'Daniel'],
    'Contract Number':['56486','68425','364875','12345','88534'],
}

import pandas as pd 
customers = pd.DataFrame(data)
print(customers)