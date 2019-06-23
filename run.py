from flask import Flask, render_template, request, redirect, url_for
import folium
import project
from backend.box import getaddresses, daate
from backend.constant import ville_list,  a,b, me, road_type
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'resources'
ALLOWED_EXTENSIONS = set(['csv'])
db1=a
db2=b
def uploadfile(req):
	print("files req : ", req)
	if 'file' not in req:
		print('No file part')
		return redirect(request.url)

	file = req['file']
	if file.filename == '':
		print('No selected file')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		file.stream.seek(0) 
		myfile = file.file
		db1=myfile
		db2=myfile
		return 'file uploaded successfully'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER






def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'GET':
		project.mapbuid(me())
		return render_template('index.html', villes =ville_list, roads = road_type)
	elif request.method == 'POST':
		print('in?')
		if  request.form['action'] == 'Upload':
			print("files req : ", request.files)
			print('request.method : %s',  request.method)
			print('request.files : %s', request.files)
			print('request.args : %s', request.args)
			print('request.form : %s', request.form)
			print('request.values : %s', request.values)
			uploadfile(request.files)
		#if request.form['action']=='Statistique':
		if request.form.get('date'):
			print(request.form['startday'].split('-'))
			print(request.form['endday'].split('-'))
			if request.form.get('stats'):
				print('sts')
				project.mapp(request.form['ville'],1,daate(getaddresses(request.form['ville'],db1,db2),request.form['startday'],request.form['endday']))
			elif request.form.get('stat'):
				print('st')
				project.mapp(request.form['ville'],2,daate(getaddresses(request.form['ville'],db1,db2),request.form['startday'],request.form['endday']))
			elif request.form.get('info'):
				print('if')
				project.mappp(request.form['ville'],daate(getaddresses(request.form['ville'],db1,db2),request.form['startday'],request.form['endday']))
			elif request.form['action'] == 'Search':
				project.mapp(request.form['ville'],0,daate(getaddresses(request.form['ville'],db1,db2),request.form['startday'],request.form['endday']))
		else:
			if request.form.get('stats'):
				project.mapp(request.form['ville'],1,getaddresses(request.form['ville'],db1,db2))
			elif request.form.get('stat'):
				project.mapp(request.form['ville'],2,getaddresses(request.form['ville'],db1,db2))
			elif request.form.get('info'):
				project.mappp(request.form['ville'],getaddresses(request.form['ville'],db1,db2))
			elif request.form['action'] == 'Search':
				project.mapp(request.form['ville'],0,getaddresses(request.form['ville'],db1,db2))
#	elif  request.form['action']=='Prediction':
		#	project.prediction(request.form['preday'])
		
	return render_template('index.html',villes =ville_list,roads = road_type)

if __name__ == '__main__':
    app.run(debug=True)
