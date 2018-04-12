from django.db import models
from django.contrib.auth.models import User

class User(User):
	pass

class Poll(models.Model):
	date_created 	= models.DateTimeField(auto_now_add=True)
	host 			= models.ForeignKey('User', on_delete=models.CASCADE)
	Name			= models.TextField()

class Question(models.Model):
	poll 	= models.ForeignKey('Poll', on_delete=models.CASCADE)
	text 	= models.TextField()
	order 	= models.SmallIntegerField()

class Answer(models.Model):
	question 	= models.ForeignKey('Question', on_delete=models.CASCADE)
	text 		= models.TextField()
	is_correct	= models.BooleanField()
	order		= models.SmallIntegerField()

class Result(models.Model):
	poll 			= models.ForeignKey('Poll', on_delete=models.CASCADE)
	date_created 	= models.DateTimeField(auto_now_add=True)
	date_closed 	= models.DateTimeField(auto_now_add=False)
	code 			= models.CharField(max_length=5)
	active_question = models.SmallIntegerField()
