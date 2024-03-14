
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
import requests
from flask import request

def send_api_request(path):
    url = 'https://jsonplaceholder.typicode.com/'+ path
    
    # Definer eventuelle nødvendige parametre eller headers


    # Sendeanmodning
    response = requests.get(url)
    
    # Hvis du vil sende en POST-anmodning, kan du bruge følgende linje i stedet:
    # response = requests.post(url, json=payload, headers=headers)
# godadag
    # Håndter svar
    if response.status_code == 200:
        # Succes, behandle data
        data = response.json()
        return data
    else:
        # Hvis der opstod en fejl, udskriv fejlmeddelelse
        print("Fejl ved anmodning til API'en. Statuskode:", response.status_code)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/album')
# ‘/’ URL is bound with hello_world() function.
def album():

    data = send_api_request(path='albums')
    return data
@app.route('/comments')
def comments():
     data = send_api_request(path='comments')
     return data
@app.route('/posts')
def posts():
     data = send_api_request(path='posts')
     return data
@app.route('/comments/postid')
def comments_postid():
     postid = request.args.get('postid')
     data = send_api_request(path = '/comments?postId='+ postid)
     return data

@app.route('/posts/<postid>/comments')
def show_user_profile(postid):
     data = send_api_request(path='/posts/'+ postid + '/comments')
     return data

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()

