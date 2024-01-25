import requests
import urllib.parse

natural_language_filter = "a 3 bedroom apartment in kitsilano"

query_string = urllib.parse.quote(natural_language_filter)


def print_listings(listings):
    for listing in listings:
        print(f"Address: { listing['address'] }")
        print(f"Bedrooms: { listing['bedrooms'] }")
        print(f"Bathrooms: { listing['bathrooms'] }")
        print(f"Size: { listing['size'] } sqft")
        print(f"Type: { listing['type'] }")
        print(f"Neighbourhood: { listing['neighbourhood'] }")
        print(f"Description: { listing['description'] }")
        print(f"Price: ${ listing['price'] } / month")
        print("\n")

    if (len(listings) == 0):
        print('❌ No listings found.')


request = requests.get('http://127.0.0.1:8000/listings',
                       params={'filter': query_string})
print('\n\nSearching for your new home... ⏳\n')
print_listings(request.json())
