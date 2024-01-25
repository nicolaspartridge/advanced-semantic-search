import pandas as pd
import random

# This file simply generates fake real estate data
# Define the number of rows in the dataset
num_rows = 100  # You can change this to the desired number of rows

# Lists of possible values for each column
addresses = [
    '123 Main St', '456 Elm St', '789 Oak St', '101 Maple Ave', '202 Cedar Ave',
    '303 Pine St', '404 Birch Ave', '505 Oakwood Dr', '606 Maplewood Ln', '707 Elmwood Rd',
    '808 Cedarwood Pl', '909 Redwood Ct', '1010 Spruce St', '1111 Pine Ave', '1212 Oak Ave',
    '1313 Maple Rd', '1414 Birch Dr', '1515 Elmwood Ln', '1616 Oakwood Pl', '1717 Cedarwood Ct',
    '1818 Pine Rd', '1919 Maplewood Dr', '2020 Birchwood Ave', '2121 Elmwood Rd', '2222 Oakwood Ln',
    '2323 Cedar Ave', '2424 Redwood Pl', '2525 Spruce Ct', '2626 Pine St', '2727 Maple Ave',
    '2828 Oakwood Dr', '2929 Birch Rd', '3030 Elmwood Pl', '3131 Cedarwood Ct', '3232 Pinewood Rd',
    '3333 Oakwood Ln', '3434 Redwood Ave', '3535 Spruce St', '3636 Maplewood Dr', '3737 Elm St',
    '3838 Cedar Ave', '3939 Oakwood Rd', '4040 Pine Pl', '4141 Birchwood Ct', '4242 Elmwood Ave',
    '4343 Maple St', '4444 Oakwood Dr', '4545 Cedarwood Ln', '4646 Redwood Rd', '4747 Spruce Ave',
    '4848 Pine Rd', '4949 Maple Ave', '5050 Oak St', '5151 Birch Ave', '5252 Elmwood Dr',
    '5353 Cedarwood Pl', '5454 Oakwood Ct', '5555 Redwood Ln', '5656 Spruce Rd', '5757 Pinewood Ave',
    '5858 Maplewood Ln', '5959 Oakwood Rd', '6060 Cedar St', '6161 Elmwood Dr', '6262 Pine Ave',
    '6363 Birchwood Pl', '6464 Oakwood Ct', '6565 Redwood Ave', '6666 Spruce Ln', '6767 Cedar Ave',
    '6868 Elm St', '6969 Maplewood Ct', '7070 Oakwood Ln', '7171 Pinewood Rd', '7272 Birchwood Ave',
    '7373 Cedarwood Dr', '7474 Elmwood Pl', '7575 Oak Ave', '7676 Maple Rd', '7777 Redwood Ln',
    '7878 Spruce Ave', '7979 Pine Ave', '8080 Cedarwood Rd', '8181 Elmwood St', '8282 Oakwood Ave',
    '8383 Birch Rd', '8484 Maplewood Dr', '8585 Pine St', '8686 Cedarwood Pl', '8787 Elmwood Rd',
    '8888 Oakwood Dr', '8989 Redwood Ave', '9090 Spruce Ln', '9191 Cedar Ln', '9292 Birchwood Ave',
    '9393 Elmwood Ct', '9494 Oakwood St', '9595 Pine Rd', '9696 Maplewood Ln', '9797 Cedar Ave'
]
bedrooms = [1, 2, 3, 4, 5]
bathrooms = [1, 1.5, 2, 2.5, 3]
sizes = [600, 800, 1000, 1200, 1500]
pets = [True, False]
property_types = ['Apartment', 'House', 'Condo', 'Townhouse']
neighbourhoods = ['Downtown', 'Kitsilano',
                  'Yaletown', 'West End', 'Mount Pleasant']
descriptions = ['Cozy apartment with a view.',
                'Spacious house with a backyard.', 'Modern condo in the heart of the city.']
sponsored_values = [True, False]

# Create an empty DataFrame
df = pd.DataFrame(columns=['id', 'address', 'bedrooms', 'bathrooms', 'size',
                  'pets', 'type', 'neighbourhood', 'description', 'sponsored', 'image', 'price'])

# Calculate price


def calculate_price(row):
    base_price = 800  # Minimum price
    price_per_bedroom = 300  # Price increase per bedroom
    price_per_sqft = 5      # Price increase per square foot

    # Calculate the price based on bedrooms and size
    price = (base_price +
             row['bedrooms'] * price_per_bedroom +
             row['size'] * price_per_sqft)

    # Add randomness to the price
    price += random.randint(-50, 50)

    return price


# Populate the DataFrame with random data and unique addresses
for i in range(num_rows):
    address = addresses[i % len(addresses)]
    bedroom = random.choice(bedrooms)
    bathroom = random.choice(bathrooms)
    size = random.choice(sizes)
    pet = random.choice(pets)
    property_type = random.choice(property_types)
    neighbourhood = random.choice(neighbourhoods)
    description = random.choice(descriptions)
    sponsored = random.choice(sponsored_values)
    image = '/images/rental-2.png' if sponsored else '/images/rental-1.png'
    price = calculate_price({'bedrooms': bedroom, 'size': size})

    df.loc[i] = [i, address, bedroom, bathroom, size, pet,
                 property_type, neighbourhood, description, sponsored, image, price]

# Save the DataFrame to a CSV file
df.to_csv('fake_properties_dataset.csv', index=True)
