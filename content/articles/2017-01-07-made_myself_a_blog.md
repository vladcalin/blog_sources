Title: Finally I made myself a blog
Date: 2017-01-07 20:21
Modified: 2017-01-07 22:37
Category: Misc
Tags: blog, python
Authors: Vlad Calin

There is no secret that having a blog is no big deal. Nowdays, everybody can create and host
a blog with ease. So I though... why shouldn't I have a blog?

I always wanted to write about different things that bug or incite me, write a couple
of words about some interesting things I do or see other people do, offer some tips
about the problems that every programmer once had, etc.

Over the past few days, I searched a method to create a free blog without any major
complications and drama. I researched a little and I tried some of the most popular
choices:

- using Blogger (Google's platform for blogging)
- using Wordpress
- using Jekyll
- using Pelican

Each of these tools have their strengths and weaknesses. 

### Blogger

My first choice was blogger. Why? Because Google owns us, of course.

Joking aside, it came very easy to start a blog using their platform, as I use Google Chrome as
my main browser and I am logged in with my GMail account. 

The main advantage was that it was easy to start a blog from scratch and publish the first post.
But that was not enough for me. The lack of customization for my blog made me reconsider my choice 
and look further for alternatives. More precisely, they have just a bunch of available themes
and they all look ...  let's just say, not appealing. I had to find something that could be easily 
customizable without loosing its functionality.

### Wordpress

After the Blogger dissapointment, I moved on to Wordpress, the great platform for blogging.
I created an account, I created a blog, I created a new post, published it... but I knew something
was missing... It was all so complicated, everything was so customizable with so many options that 
I was losing myself in those details. 

The next day when I wanted to check out how everything is going, the browser started to crash when I
was accessing their site with an "Out of memory" error. That was unpleasant and frustrating as I was
unable to access the platform. I had to find something else.

### Jekyll

After a while, I heard about some static site generators. I knew, in essence, what they were because I
used Sphinx to convert RST markup to Python documentation, but I never actually got in touch with 
other static site generators other than that. With one search on Google, I found this little tool
named Jekyll (an odd name, to be honest). I followed all their steps in the tutorial and I was
able to generate a mini-blog with a hello world. But I didn't like it because I had to install 
a bunch of useless packages (ruby, gem, some other packages that I had to install because
of some weird errors) just to run Jekyll and generate some HTML pages. Being a Python developer, I said
that there has to be something similar for Python.

### Pelican

After searching for a few minutes, I stumbled upon **Pelican** - a static site generator written in
Python. After the usual ``pip install ...`` thingy, everything was ready. I followed their tutorial
and found out that everything was so easy... and free... and from the comfort of my own hardware, 
not on the platform of some corporation. It felt right, it was easy, it was fast.

And now, I am using this method of writing a blog and I sincerely recommend it!