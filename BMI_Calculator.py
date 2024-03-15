def calculate_bmi(weight, height):
  """Calculates the Body Mass Index (BMI) based on weight and height.

  Args:
      weight: User's weight in kilograms (kg).
      height: User's height in meters (m).

  Returns:
      The calculated BMI value.
  """
  return weight / (height * height)

def categorize_bmi(bmi):
  """Categorizes the BMI value into health categories.

  Args:
      bmi: The calculated Body Mass Index (BMI).

  Returns:
      A string representing the BMI category and potential health suggestions.
  """
  if bmi <= 18.5:
    return "Underweight. You may want to consult a healthcare professional to ensure you're getting enough nutrients."
  elif 18.5 < bmi <= 24.9:
    return "Normal weight. Keep up the healthy lifestyle!"
  elif 25 <= bmi <= 29.9:
    return "Overweight. Consider incorporating more exercise or consulting a nutritionist for healthy weight management plans."
  else:
    return ("Obese. This category may be associated with increased health risks. "
            "Consult a healthcare professional for personalized guidance on improving your health.")

def main():
  """Prompts the user for weight and height, calculates BMI, and displays results."""
  while True:
    try:
      weight = float(input("Enter your weight in kilograms (kg): "))
      if weight <= 0:
        raise ValueError("Weight cannot be zero or negative.")
      height = float(input("Enter your height in meters (m): "))
      if height <= 0:
        raise ValueError("Height cannot be zero or negative.")
      break
    except ValueError as e:
      print("Invalid input:", e)
      print("Please enter positive values for weight and height.")

  bmi = calculate_bmi(weight, height)
  category = categorize_bmi(bmi)

  print(f"Your BMI is: {bmi:.2f}")  # Format BMI to two decimal places
  print(category)

if __name__ == "__main__":
  main()
