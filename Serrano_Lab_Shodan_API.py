"""
script: Serrano_Lab_Shodan_API.py
action: 
    a. Uses Shodan API to search for 'in-tank inventory' devices in Arizona
    b. Prints the data field from each matching device
Author: Franco Xavier Serrano
Date: 11/01/2025
"""
import shodan


def main() -> None:
    """
    Search Shodan for in-tank inventory devices and print data field.
    
    action: Query Shodan API and display results
    input: User enters Shodan API key
    output: Prints data field from each matching device
    return: None
    """
    # Prompt user for API key
    api_key = input("\nEnter your Shodan API key: ").strip()
    
    # Initialize Shodan API
    api = shodan.Shodan(api_key)
    
    # Define search query
    query = "'in-tank inventory' state:'AZ'"
    
    # Try-except block to handle potential API errors
    try:
        print(f"\nSearching Shodan for: {query}\n")
        result = api.search(query)
        
        # matches is already a list of dictionaries
        matches = result["matches"]
        
        # Print total number of results found for user feedback
        print(f"Found {len(matches)} result(s).\n")
        
        # Iterate through each item and print the search query returned data
        for item in matches:
            if "data" in item:
                print(item["data"])
            else:
                print("(No data field in this result)")
                
    # Handle Shodan API errors
    except shodan.APIError as e:
        print(f"Shodan API Error: {e}")
        print("Please check your API key and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()

