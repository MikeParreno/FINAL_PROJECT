def convert_mm_to_cm(value):
#   """Converts millimeters to centimeters."""
  return value / 10

def convert_cm_to_mm(value):
#   """Converts centimeters to millimeters."""
  return value * 10

def convert_in_to_cm(value):
#   """Converts inches to centimeters."""
  return value * 2.54

def convert_cm_to_in(value):
#   """Converts centimeters to inches."""
  return value / 2.54

def convert_ft_to_m(value):
#   """Converts feet to meters."""
  return value * 0.3048

def convert_m_to_ft(value):
#   """Converts meters to feet."""
  return value / 0.3048

def main():
#   """Displays the menu and handles user input for conversions."""
  while True:
    print("\n--- Measurement Converter ---")
    print("1. Millimeters (mm) to Centimeters (cm)")
    print("2. Centimeters (cm) to Millimeters (mm)")
    print("3. Inches (in) to Centimeters (cm)")
    print("4. Centimeters (cm) to Inches (in)")
    print("5. Feet (ft) to Meters (m)")
    print("6. Meters (m) to Feet (ft)")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
      print("Exiting program.")
      break

    try:
      value = float(input("Enter the value to convert: "))
      if choice == '1':
        converted_value = convert_mm_to_cm(value)
        print(f"{value} mm is equal to {converted_value:.2f} cm")
      elif choice == '2':
        converted_value = convert_cm_to_mm(value)
        print(f"{value} cm is equal to {converted_value:.2f} mm")
      elif choice == '3':
        converted_value = convert_in_to_cm(value)
        print(f"{value} in is equal to {converted_value:.2f} cm")
      elif choice == '4':
        converted_value = convert_cm_to_in(value)
        print(f"{value} cm is equal to {converted_value:.2f} in")
      elif choice == '5':
        converted_value = convert_ft_to_m(value)
        print(f"{value} ft is equal to {converted_value:.2f} m")
      elif choice == '6':
        converted_value = convert_m_to_ft(value)
        print(f"{value} m is equal to {converted_value:.2f} ft")
      else:
        print("Invalid choice.")
    except ValueError:
      print("Please enter a valid number.")

if __name__ == "__main__":
  main()
