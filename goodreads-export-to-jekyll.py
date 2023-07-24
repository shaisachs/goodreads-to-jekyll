import csv
import re

def cut_out_parens(title):
	return re.sub(r'\(.*\)', '', title)

def cut_out_subtitle(title):
	return re.sub(r':.*$', '', title)

def cut_out_nonalphanum(title):
	return re.sub(r'[^A-Za-z0-9\s]', '', title)

def dash_for_space(title):
	return re.sub(r'\s+', '-', title)

def title_slug(title):
	answer = title

	answer = cut_out_parens(answer)
	answer = cut_out_subtitle(answer)
	answer = cut_out_nonalphanum(answer)
	answer = answer.lower().strip()
	answer = dash_for_space(answer)

	return answer

# expects date in Y/m/d format, responds with date in Y-m-d format
def format_date(date):
	return date.replace('/', '-')

def html_to_md(html):
	answer = html
	answer = answer.replace("<br />", "\n\n")
	answer = answer.replace("<br/>", "\n\n")
	answer = answer.replace("<i>", "_")
	answer = answer.replace("</i>", "_")
	answer = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>', r'[\\2](\\1)', answer);
	answer = answer.strip()
	return answer

def get_filename(title_slug, dateread):
	return filename

def create_file(title, dateread, rating, review):
	slug = title_slug(title)
	date_formatted = format_date(dateread)

	filename = "/src/reviews/{dateread}-{title_slug}.md".format(title_slug=slug, dateread=date_formatted)
	file = open(filename, "a", encoding='utf8')

	file.write("---\n")
	file.write("layout: bookreview\n")
	file.write('title: "{title}"\n'.format(title=title))
	file.write('date: {dateread} 13:00\n'.format(dateread=date_formatted))
	file.write("bookfinished: {dateread}\n".format(dateread=date_formatted))
	file.write("rating: {rating}\n".format(rating=rating))
	# wishlist: book cover image
	# wishlist: review url on goodreads
	file.write("---\n\n")

	file.write(html_to_md(review))
	file.close()

with open('/src/goodreads_library_export.csv', encoding='utf8') as csvfile:
	bookreader = csv.reader(csvfile)
	for row in bookreader:
		title = row[1]
		dateread = row[14]
		rating = row[7]
		review = row[19]

		# first row
		if (title == 'Title'):
			continue

		# unread books
		if (not dateread):
			continue

		create_file(title, dateread, rating, review)

		print(title_slug(title))