import http.client
from http.client import HTTPSConnection, HTTPResponse
from pathlib import Path


def get_puzzle_input(year: int, day: int):
    # The project root dir
    base_dir: Path = Path(__file__).parent.parent
    # Pad with leading zero if day is a single digit
    puzzle_input_file: Path = base_dir / 'puzzle_input' / f'year_{year}_day_{day:02}.txt'
    session_cookie_file: Path = base_dir / 'cookie.txt'

    # If the puzzle input is already cached, return it
    if puzzle_input_file.exists():
        return puzzle_input_file.read_text(encoding='utf-8')

    # Puzzle input isn't cached, retrieve it and cache it in a file

    # Ensure the session cookie file exists
    if not session_cookie_file.exists():
        print(f"Error: {session_cookie_file.name} file not found.")
        return

    # Read the session cookie from the file
    session_cookie: str = session_cookie_file.read_text(encoding='utf-8').strip()

    # Retrieve the puzzle input from the website
    connection: HTTPSConnection = http.client.HTTPSConnection('adventofcode.com')
    url_path: str = f'/{year}/day/{day}/input'
    headers: dict[str, str] = {
        'Cookie': f'session={session_cookie}',
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        connection.request('GET', url_path, headers=headers)
        response: HTTPResponse = connection.getresponse()

        # Check if the response status is 200 (OK)
        if response.status != 200:
            print(f"Error: Failed to download puzzle input, {response.status}: {response.reason}")
            return

        # Remove any trailing new lines characters
        puzzle_input: str = response.read().decode("utf-8").rstrip('\r\n')

    finally:
        # Ensure the connection is closed even if an error occurs
        connection.close()

    # Ensure the 'puzzle_input' directory exists
    puzzle_input_file.parent.mkdir(parents=True, exist_ok=True)

    # Cache the puzzle input in the file
    puzzle_input_file.write_text(puzzle_input, encoding='utf-8')

    return puzzle_input
