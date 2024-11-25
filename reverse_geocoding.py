import boto3

def reverse_geocode(latitude, longitude, index_name):
    """
    Perform reverse geocoding using AWS Location Service.

    Parameters:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        index_name (str): Name of the Place Index resource in AWS Location Service.
        
    Returns:
        dict: Address details from the reverse geocoding result.
    """
    # Initialize the client
    client = boto3.client('location', region_name='us-east-2')

    try:
        # Perform reverse geocoding
        response = client.search_place_index_for_position(
            IndexName=index_name,
            Position=[longitude, latitude]
        )
        
        # Extract and return the first result
        if 'Results' in response and len(response['Results']) > 0:
            place = response['Results'][0]
            return place
        else:
            print("No results found for the given coordinates.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Coordinates for the reverse geocoding
    lat = 37.7749  # Latitude of San Francisco
    lon = -122.4194  # Longitude of San Francisco
    
    # Replace with your Place Index resource name
    place_index_name = "place_index_demo"
    
    result = reverse_geocode(lat, lon, place_index_name)
    if result:
        print("Reverse Geocoding Result:")
        print(result)
