from django.db import models
from django.utils import timezone


class Post(models.Model):
	작성자 = models.ForeignKey('auth.User')
	제목 = models.CharField(max_length=200)
	내용 = models.TextField()
	작성일자 = models.DateTimeField(
		default=timezone.now)
	Published_Date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title