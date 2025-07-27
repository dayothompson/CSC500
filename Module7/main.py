def main():
    # Dictionary containing course numbers and room numbers
    course_rooms = {
        'CSC101': '3004',
        'CSC102': '4501', 
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }
    
    # Dictionary containing course numbers and instructors
    course_instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }
    
    # Dictionary containing course numbers and meeting times
    course_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }
    
    print("\nCourse Information Lookup System")
    print("=" * 40)
    
    while True:
        # Get course number from user
        course_number = input("\nEnter a course number (or 'quit' to exit): ").upper()
        
        # Check if user wants to quit
        if course_number.lower() == 'quit':
            print("Thank you for using the Course Information Lookup System!")
            break
        
        # Check if course exists in our dictionaries
        if course_number in course_rooms:
            print(f"\nCourse Information for {course_number}:")
            print(f"Room Number: {course_rooms[course_number]}")
            print(f"Instructor: {course_instructors[course_number]}")
            print(f"Meeting Time: {course_times[course_number]}")
        else:
            print(f"Course {course_number} not found. Please enter a valid course number.")
            print("Available courses:", ', '.join(course_rooms.keys()))

if __name__ == "__main__":
    main()

