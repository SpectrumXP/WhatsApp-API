import mysql.connector
import webbrowser

DANGEROUS_LINKS = [
    "https://youtube.com",
    "http://forbes.com",
    "www.twitter.com",
    # Add more dangerous links here
]

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="",  # Replace with your MySQL host
    user="",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database=""  # Replace with your MySQL database name
)

def check_link_exists():
    userLink = input("Enter a full link: ")
    
    # Create a cursor object
    cursor = connection.cursor()
    chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    try:
        # Execute the query
        cursor.execute("SELECT * FROM whatsapp")

        # Fetch all rows from the result set
        links = cursor.fetchall() 
        for _, link in links:
           
            if str(userLink.lower()) == str(link.lower()):
                print("The link is not safe.")
              
            elif userLink != link:
                webbrowser.get(chromedriver_path).open(userLink)

    except mysql.connector.Error as error:
        print("Failed to execute query:", error)

    # Close the cursor
    cursor.close()

# Check if the connection is successful
if connection.is_connected():
    print("Connection to MySQL database successful!")
    check_link_exists()

# Close the connection
connection.close()
  
