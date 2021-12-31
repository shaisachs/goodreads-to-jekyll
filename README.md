# Goodreads-to-Jekyll

This repo contains two scripts for migrating Goodreads book reviews into Jekyll.

* `goodreads-api-to-jekyll.php` - A PHP script which used the now-deprecated API to create Jekyll files.
* `goodreads-export-to-jekyll.py` - A Python 3 script which uses CSV exports from Goodreads to create Jekyll files.

The repo is highly customized to [my own personal website](https://shaisachs.com), and is probably not suitable (out of the box) for yours. However, it should not be very difficult to adjust for your own setup.

0. Login to Goodreads
1. Request an export of your Goodreads data from [https://www.goodreads.com/dsar/user](https://www.goodreads.com/dsar/user)
2. Do the email confirmation / waiting dance. The ETA is a month but I've seen it take shorter in practice.
3. Once you have the requested download, save it as `goodreads_library_export.csv` in the same folder as `goodreads-export-to-jekyll.py`.
4. Create a folder called `reviews` in the same folder as `goodreads_library_export.py`.
5. Run `python goodreads_library_export.py`
6. Move the generated reviews in `reviews/*.md` into your own website's Jekyll collection, in my case this command looks something like `mv reviews/*.md ~/website/_bookreviews`.
7. Push the new reviews up to your website! (In my case, this command is something like `cd ~/website ; git add . ; git commit -sm 'Add reviews`)

The code is pretty quick-and-dirty, and doesn't really obey typical SOLID principles. It gets the job done for me, but if you'd like to improve it, you're more than welcome! I'm happy to collaborate, contributions highly encouraged.