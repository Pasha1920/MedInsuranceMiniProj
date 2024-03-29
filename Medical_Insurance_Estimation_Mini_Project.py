# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name="Maria", age=31, sex=0, bmi=23.1, num_of_children=1, smoker=0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name=
                                               "Rohan", age=25, sex=1, bmi=28.5, num_of_children=3, smoker=0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name="Valentina", age=53, sex=0, bmi=31.4, num_of_children=0,
                                                   smoker=1)

names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = list(zip(names, insurance_costs))
print("The actual insurance cost data: ", insurance_data)

estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
print("The estimated insurance cost data:", estimated_insurance_data)

# Finding difference between actual and estimated insurance cost data for each individual
insurance_cost_difference = []
n = len(estimated_insurance_data)
for i in range(0, n):
    current_name = estimated_insurance_data[i][0]
    actual = insurance_data[i][1]
    estimated = estimated_insurance_data[i][1]
    difference = actual - estimated
    insurance_cost_difference.append((current_name, difference))

print("The insurance cost difference by name:", insurance_cost_difference)





