def get_word_count(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		words = file_contents.split()
		return f"Found {len(words)} total words"

def get_char_count(filepath):
	chr_count = {}
	with open(filepath) as f:
		file_contents = f.read()
		for chr in file_contents:
			if chr.lower() in chr_count:
				chr_count[chr.lower()] += 1
			else:
				chr_count[chr.lower()] = 1
	return chr_count

def sort_on(d):
	return d["num"]

def sort_chars(chr_count):
	new_list = []
	for key in chr_count:
		new_list.append({"char": key, "num": chr_count[key]})
	new_list.sort(reverse=True, key=sort_on)
	return new_list