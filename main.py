# this is using the creat_app method from flash to create a flask app
from website import create_app

app = create_app()

# this line says only if we run the main file and not if we import the main file will it begin
if __name__ == '__main__':
    # this runs the server and anytime we make a change debug==True will re run the server
    app.run(debug=True)
