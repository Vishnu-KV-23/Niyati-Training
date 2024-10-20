import pandas as pd

# Function to calculate probabilities
def calculate_probabilities(data):
    # Calculate total number of events
    total_events = len(data)

    # Count occurrences of 'yes' and 'no'
    yes_count = len(data[data['output'] == 'yes'])
    no_count = len(data[data['output'] == 'no'])

    # Calculate probabilities of "yes" and "no"
    prob_yes = yes_count / total_events
    prob_no = no_count / total_events

    # Calculate weather counts (sunny, rainy, mist)
    weather_counts = data['weather'].value_counts()

    # Calculate weather probabilities
    weather_probs = weather_counts / total_events

    # Calculate conditional probabilities P(weather | yes) and P(weather | no)
    weather_given_yes = data[data['output'] == 'yes']['weather'].value_counts()
    weather_given_no = data[data['output'] == 'no']['weather'].value_counts()

    prob_sunny_given_yes = weather_given_yes.get('sunny', 0) / yes_count
    prob_rainy_given_yes = weather_given_yes.get('rainy', 0) / yes_count
    prob_mist_given_yes = weather_given_yes.get('mist', 0) / yes_count

    prob_sunny_given_no = weather_given_no.get('sunny', 0) / no_count
    prob_rainy_given_no = weather_given_no.get('rainy', 0) / no_count
    prob_mist_given_no = weather_given_no.get('mist', 0) / no_count

    return {
        "Total Events": total_events,
        "Probability of Yes": prob_yes,
        "Probability of No": prob_no,
        "Weather Probabilities": weather_probs.to_dict(),
        "P(sunny | yes)": prob_sunny_given_yes,
        "P(rainy | yes)": prob_rainy_given_yes,
        "P(mist | yes)": prob_mist_given_yes,
        "P(sunny | no)": prob_sunny_given_no,
        "P(rainy | no)": prob_rainy_given_no,
        "P(mist | no)": prob_mist_given_no
    }

# Load the CSV file (change the path as needed)
file_path = 'your_file_path.csv'
data = pd.read_csv(file_path)

# Clean the data (assuming weather and output columns are in positions 1 and 2)
data_cleaned = data[['sunny', 'no']].rename(columns={'sunny': 'weather', 'no': 'output'}).dropna()

# Calculate probabilities
result = calculate_probabilities(data_cleaned)

# Print the results
for key, value in result.items():
    print(f"{key}: {value}")
