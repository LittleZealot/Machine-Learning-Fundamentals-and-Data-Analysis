import matplotlib.pyplot as plt

# Problem 1: Number of grains of rice on the 100th day
def compute_sorori_shinzaemon(n_days=100):
    # Calculate the number of grains on each day and the total grains by the day
    list_n_grains = [2**i for i in range(n_days)]
    list_total_grains = [sum(list_n_grains[:i+1]) for i in range(n_days)]
    return list_n_grains, list_total_grains

# Plotting for the 100-day scenario
list_n_grains, list_total_grains = compute_sorori_shinzaemon(n_days=100)
plt.plot(range(1, 101), list_n_grains, label='Rice grains on the day')
plt.plot(range(1, 101), list_total_grains, label='Total rice grains by the day')
plt.xlabel('Number of days')
plt.ylabel('Number of rice grains')
plt.legend()
plt.title('Problem 1: Number of Rice Grains on the 100th Day')
plt.show()

# Problem 2: Number of rice grains outside of the 100th day
# Example usage for a specific number of days (e.g., the duration of the course)
course_duration = 30
list_n_grains_course, list_total_grains_course = compute_sorori_shinzaemon(n_days=course_duration)

# Plotting for the course duration
plt.plot(range(1, course_duration+1), list_n_grains_course, label='Rice grains on the day')
plt.plot(range(1, course_duration+1), list_total_grains_course, label='Total rice grains by the day')
plt.xlabel('Number of days')
plt.ylabel('Number of rice grains')
plt.legend()
plt.title(f'Problem 2: Number of Rice Grains for {course_duration} Days')
plt.show()

# Problem 3: How many people can live for how many days with the rice we get?
def calculate_days_to_live(num_rice_grains, num_people):
    # Calculate the days people can live with the given rice
    grains_per_day = 6000  # Assuming an average person needs around 6000 grains per day
    days_to_live = num_rice_grains / (num_people * grains_per_day)
    return int(days_to_live)

# Example usage
num_people_in_class = 30
days_to_live = calculate_days_to_live(list_total_grains_course[-1], num_people_in_class)

print(f'Problem 3: With the rice received, {num_people_in_class} people can live for approximately {days_to_live} days.')
