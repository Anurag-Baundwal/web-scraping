import requests
from bs4 import BeautifulSoup

# URL of the main page containing the sections and lessons
base_url = "https://realpython.com/courses/python-tic-tac-toe-ai/"

# Send a GET request to the main page
print("Sending GET request to the main page...")
response = requests.get(base_url)

# Create a BeautifulSoup object to parse the HTML content
print("Parsing the HTML content...")
soup = BeautifulSoup(response.content, "html.parser")

# Find all the sections on the page
print("Finding sections on the page...")
sections = soup.find_all("div", class_="mb-5 p-3 bg-white rounded border shadow-sm small")

# Open a file to write the transcript in Markdown format
with open("transcript.md", "w") as file:
    # Iterate over each section
    for section in sections:
        # Extract the section title
        section_title = section.find("h2").text.strip()
        print(f"Processing section: {section_title}")
        file.write(f"## {section_title}\n\n")

        # Find all the lessons within the section
        lesson_elements = section.find_all("div", class_="media")

        # Collect the lesson details
        lessons = []
        for lesson_element in lesson_elements:
            lesson_title = lesson_element.find("p", class_="h5 mb-0").text.strip()
            lesson_url = lesson_element.find("a")["href"]
            lessons.append((lesson_title, lesson_url))

        # Process the lessons in the correct order
        for lesson_title, lesson_url in lessons:
            print(f"Processing lesson: {lesson_title}")
            file.write(f"### {lesson_title}\n\n")

            # Send a GET request to the lesson URL
            lesson_response = requests.get(f"https://realpython.com{lesson_url}")
            lesson_soup = BeautifulSoup(lesson_response.content, "html.parser")

            # Find the transcript div and extract its text
            transcript_div = lesson_soup.find("div", id="transcript")
            if transcript_div:
                transcript_text = transcript_div.get_text(separator="\n", strip=True)
                file.write(f"{transcript_text}\n\n")
            else:
                file.write("Transcript not available.\n\n")

print("Transcript saved in transcript.md")