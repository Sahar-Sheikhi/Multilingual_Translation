import pandas as pd
import random

# Set random seed for reproducibility
random.seed(42)

def reduce_dataset():
    # Ask for input file
    input_file = input("Enter the path to your CSV file: ")
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        total_rows = len(df)
        
        # Ask for number of rows
        while True:
            try:
                num_rows = int(input(f"Enter number of rows to keep (max {total_rows}): "))
                if 0 < num_rows <= total_rows:
                    break
                print(f"Please enter a number between 1 and {total_rows}")
            except ValueError:
                print("Please enter a valid number")
        
        # Sample random rows
        reduced_df = df.sample(n=num_rows, random_state=42)
        
        # Create output filename
        output_file = input_file.rsplit('.', 1)[0] + f'_reduced_{num_rows}.csv'
        
        # Save to new CSV file
        reduced_df.to_csv(output_file, index=False)
        print(f"Reduced dataset saved to: {output_file}")
        
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    reduce_dataset()