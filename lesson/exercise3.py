def step_calculator(step_length_cm, distance_m):
    step_length_cm /= 100
    return distance_m/step_length_cm

step_length_cm_input = int(input("How long is your average step in centimeters? "))
distance_m_input = int(input("What distance did you walk (in meters)? "))

print(step_calculator(step_length_cm_input, distance_m_input))