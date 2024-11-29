# Python Journal Template Scripts

# Part 1: Defining Your Problem
# Example: A simple temperature conversion program

def convert_temperature():
    """
    Program to convert temperatures between Celsius and Fahrenheit
    
    Problem Definition:
    - Solve temperature unit conversion
    - Input: Temperature value and current unit (C or F)
    - Process: Convert temperature to the other unit
    - Output: Converted temperature with unit
    """
    print("Temperature Conversion Program")
    
    # Input data
    temp = float(input("Enter temperature value: "))
    unit = input("Enter current unit (C/F): ").upper()
    
    # Temperature conversion logic
    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid temperature unit. Please enter C or F.")

# Part 2: Working Through Specific Examples
def validate_convert_temperature():
    """
    Enhanced temperature conversion with error handling
    
    Example Scenarios:
    1. Normal temperature conversion
    2. Edge case with zero degrees
    3. Invalid input handling
    """
    try:
        temp = float(input("Enter temperature value: "))
        unit = input("Enter current unit (C/F): ").upper()
        
        if unit not in ['C', 'F']:
            raise ValueError("Invalid temperature unit")
        
        if unit == 'C':
            converted_temp = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {converted_temp:.2f}°F")
        else:
            converted_temp = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number and unit.")

# Part 3: Pseudocode Implementation
def advanced_temperature_converter():
    """
    Advanced temperature conversion with multiple features
    
    Pseudocode Elements:
    - User input validation
    - Multiple unit conversions (C, F, K)
    - Detailed error handling
    - Continuous conversion option
    """
    def celsius_to_fahrenheit(temp):
        return (temp * 9/5) + 32
    
    def fahrenheit_to_celsius(temp):
        return (temp - 32) * 5/9
    
    def celsius_to_kelvin(temp):
        return temp + 273.15
    
    def fahrenheit_to_kelvin(temp):
        return (temp - 32) * 5/9 + 273.15
    
    while True:
        try:
            temp = float(input("Enter temperature value: "))
            from_unit = input("Enter current unit (C/F/K): ").upper()
            to_unit = input("Enter target unit (C/F/K): ").upper()
            
            # Conversion matrix
            if from_unit == 'C':
                if to_unit == 'F':
                    result = celsius_to_fahrenheit(temp)
                elif to_unit == 'K':
                    result = celsius_to_kelvin(temp)
                else:
                    result = temp
            
            elif from_unit == 'F':
                if to_unit == 'C':
                    result = fahrenheit_to_celsius(temp)
                elif to_unit == 'K':
                    result = fahrenheit_to_kelvin(temp)
                else:
                    result = temp
            
            print(f"{temp}°{from_unit} is equal to {result:.2f}°{to_unit}")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        cont = input("Convert another temperature? (yes/no): ").lower()
        if cont != 'yes':
            break

# Part 4: Testing Function
def test_temperature_converter():
    """
    Testing function with various scenarios
    """
    # Test normal conversions
    assert round(celsius_to_fahrenheit(0), 2) == 32.00
    assert round(fahrenheit_to_celsius(32), 2) == 0.00
    
    # Test edge cases
    assert round(celsius_to_kelvin(0), 2) == 273.15
    
    print("All tests passed successfully!")

# Part 5: Fully Commented Program
def comprehensive_temperature_converter():
    """
    Comprehensive temperature conversion program with detailed comments
    
    This program allows users to convert temperatures between Celsius, 
    Fahrenheit, and Kelvin units with robust error handling.
    """
    
    # Function to convert Celsius to Fahrenheit
    def celsius_to_fahrenheit(temp):
        """Convert temperature from Celsius to Fahrenheit"""
        return (temp * 9/5) + 32
    
    # Function to convert Fahrenheit to Celsius
    def fahrenheit_to_celsius(temp):
        """Convert temperature from Fahrenheit to Celsius"""
        return (temp - 32) * 5/9
    
    # Main conversion logic
    def convert_temperature(temp, from_unit, to_unit):
        """
        Main conversion function with comprehensive unit handling
        
        Args:
            temp (float): Temperature value to convert
            from_unit (str): Source temperature unit
            to_unit (str): Target temperature unit
        
        Returns:
            float: Converted temperature
        """
        # Conversion logic using a nested dictionary
        conversion_table = {
            'C': {'F': celsius_to_fahrenheit, 'K': lambda x: x + 273.15, 'C': lambda x: x},
            'F': {'C': fahrenheit_to_celsius, 'K': fahrenheit_to_kelvin, 'F': lambda x: x},
            'K': {'C': lambda x: x - 273.15, 'F': kelvin_to_fahrenheit, 'K': lambda x: x}
        }
        
        return conversion_table[from_unit][to_unit](temp)

    # Execution code with error handling
    try:
        temperature = float(input("Enter temperature: "))
        from_unit = input("Enter source unit (C/F/K): ").upper()
        to_unit = input("Enter target unit (C/F/K): ").upper()
        
        result = convert_temperature(temperature, from_unit, to_unit)
        print(f"{temperature}°{from_unit} = {result:.2f}°{to_unit}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values and valid units.")

# Part 6: Final Executable Function
def main():
    """
    Main function to demonstrate all temperature conversion capabilities
    """
    print("Temperature Conversion Program")
    comprehensive_temperature_converter()

if __name__ == "__main__":
    main()
