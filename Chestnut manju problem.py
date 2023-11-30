import matplotlib.pyplot as plt
import math

# [Problem] The day when chestnut buns cover the solar system
# Initial values
chestnut_bun_volume = 523.6  # centimeters
solar_system_volume = 1.41e27  # kilometers
number_of_chestnut_buns = solar_system_volume / chestnut_bun_volume
byvine_doubling_time = 5  # minutes

# Variables for tracking time and number of chestnut buns
time_to_cover_solar_system = 0
number_of_chestnut_buns_list = []
time_list = []

# Loop to simulate the chestnut buns covering the solar system
for _ in range(int(math.log2(number_of_chestnut_buns))):
    # Update time and number of chestnut buns
    time_to_cover_solar_system += byvine_doubling_time
    number_of_chestnut_buns_list.append(number_of_chestnut_buns)
    time_list.append(time_to_cover_solar_system)
    number_of_chestnut_buns *= 2

# Plotting the results
plt.plot(time_list, number_of_chestnut_buns_list)
plt.xlabel("Time (minutes)")
plt.ylabel("Number of chestnut buns")
plt.title("Problem: Number of Chestnut Buns vs. Time to Cover the Solar System")
plt.show()
