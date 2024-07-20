# Question 1 

# Task 1


def format_itineraries(itineraries):
    formatted_itineraries = []
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        formatted_itinerary = f"Itinerary {i}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(formatted_itinerary)
    return "\n".join(formatted_itineraries)

# Test the function
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(itineraries))