import os
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_itinerary(destination, days, interests, budget, dates):
    system_prompt = (
        "You are a professional travel planner who creates detailed, structured itineraries."
    )
    user_prompt = f"""
    Create a {days}-day travel itinerary for {destination}.
    Interests: {interests}.
    Budget: {budget}.
    Travel dates: {dates}.
    Include day-by-day activities, dining, and accommodation tips.
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    itinerary = response.choices[0].message.content
    return itinerary


if __name__ == "__main__":
    # Example input
    itinerary = generate_itinerary(
        destination="Kyoto, Japan",
        days=5,
        interests="culture, temples, food, and history",
        budget="mid-range",
        dates="April 10–15, 2025"
    )
    print("\nGenerated Itinerary:\n")
    print(itinerary)
