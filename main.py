import sys
from stats import get_word_count, get_char_count, sort_chars

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	filepath = sys.argv[1]
	word_count = get_word_count(filepath)
	char_count = get_char_count(filepath)
	sorted_chars = sort_chars(char_count)
	formatted_chars = []
	for item in sorted_chars:
		if item['char'].isalpha():
			formatted_chars.append(f"{item['char']}: {item['num']}")

	print(
		f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{'\n'.join(formatted_chars)}
============= END ===============
	"""
	)

if __name__ == "__main__":
	main()
