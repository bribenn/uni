from django.shortcuts import render, redirect
from .models import *
import re

# Create your views here.
def index(request):
	entries = Raw_data.objects.all()
	context = {
		'entries': entries
	}
	return render(request, 'app/index.html', context)

def clean_data(request):
	new_addresses = []
	new_sq_feet = []
	new_prices = []

	new_entries = Raw_data.objects.all()
	for entry in new_entries:
		# entry.sq_ft = float(entry.sq_ft)
		print "sqft", entry.sq_ft
		entry.price = float(string(re.sub(r'[$]?', '', entry.price)))
		print type(entry.price), entry.price
		


	# context = {
	# 	'new_entries': {
	# 		addresses = new_addresses
	# 		prices = new_prices
	# 		square_feets = new_sq_feet
	# 	}
	# }
	
	return redirect('/')