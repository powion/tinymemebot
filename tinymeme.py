import praw
import urllib, cStringIO

reddit = praw.Reddit(client_id='my client id',
                     client_secret='my client secret',
                     user_agent='my user agent',
                     username='my username',
                     password='my password')                
r_tinymemes = reddit.subreddit('tinymemes')

def iterate_subs(subreddits):
  for sub in subreddits:
    subreddit = reddit.subreddit(sub)
      for submission in subreddit.top(limit=10):
        tiny_meme = shrink_meme(submission.url)
        post_meme(tiny_meme, submission.title)  
    
def shrink_meme(url):
  file = cStringIO.StringIO(urllib.urlopen(url).read())
  img = Image.open(file)
  size = 128, 128
  try:
      im = Image.open(infile)
      im.thumbnail(size)
      return im
  except IOError:
      print "cannot create thumbnail for '%s'" % infile
      return
      
def post_meme(meme, title):
  # nullcheck
  # Upload to imgur
  r_tinymemes.submit(title, url='')
  