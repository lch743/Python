#! /usr/bin/env python
import pycurl
class get_page:
	def _init_(self,url):
		self.contents=''
		self.url=url
	def read_page(self,buf):
		self.contents+=buf
	def show_page(self):
		print self.contents
words=get_page("http://robotexp.blogspot.com/")
words.show_page()
