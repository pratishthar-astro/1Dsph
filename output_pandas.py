
import numpy as np
import datetime

def output_particles(particles, filename, include_ghosts):
    print(particles)
    # Exclude ghost particles if the flag is set to False
    if include_ghosts == False:
        particles = particles[particles['Is_Ghost'] == False]
    print(particles)
    data = particles
    # Save the DataFrame to a CSV file
    data.to_csv(filename, index=False)


def print_header():
    """
    Prints a header with additional information.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Get the current date
    header1 = f"""
     -----------------------------------------------------------------------------------------
     -----------------------------------------------------------------------------------------
                                1 Dimensional SPH Code
     -----------------------------------------------------------------------------------------
     Starting date: November 2023
     Last edit date: {current_date}
     Author: Pratishtha Rawat (University of Warwick)
     -----------------------------------------------------------------------------------------
     -----------------------------------------------------------------------------------------"""
    
    print(header1)


def print_execution_time(start_time, end_time):
    """
    Prints the execution time based on the given start and end times.
    """
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")


