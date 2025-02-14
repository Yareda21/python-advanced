with open("file.txt", "a") as file:
    # this execution handles opening and closing files without memory leak
    print(f"File content: \n{file}")

# creating the above code as an example 
class FileManager:
    """
    A context manager for handling file operations.

    This class provides a way to open and close files safely, ensuring that
    resources are managed properly and exceptions are handled gracefully.
    """

    def __init__(self, filename: str, mode: str) -> None:
        """
        Initialize the FileManager with a filename and mode.

        Args:
            filename (str): The name of the file to manage.
            mode (str): The mode in which to open the file (e.g., 'r', 'w', 'a').
        """
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """
        Open the file and return the file object.

        Returns:
            file object: The opened file object.
        """
        # open the file
        self.file = open(self.filename, self.mode)
        print(f"Opening file {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the file and handle any exceptions that occurred.

        Args:
            exc_type: The exception type.
            exc_val: The exception value.
            exc_tb: The traceback object.

        Returns:
            bool: True to suppress the exception, False to propagate it.
        """
        self.file.close()
        print(f"Closing file {self.filename}")

        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True  # Suppress the exception

if __name__ == "__main__":
    # Writing to a file using the FileManager context manager
    with FileManager("example.txt", "w") as file:
        file.write("Hello World!")
        print("File written successfully!")

    # Reading from a file using the FileManager context manager
    with FileManager("example.txt", "r") as file:
        content = file.read()
        print(f"File content: {content}")