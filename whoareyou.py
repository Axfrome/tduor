import streamlit as st
from exif import Image


st.title('whoareyou') #le titre de l'app



with open ('.\Staline.jpg', 'rb') as imageisfile:
    itismyimage = Image(imageisfile)


st.image('.\Staline.jpg', width = 200,  caption='staline et non stallone')


auteur = st.text_input("Auteur de l'image", key="Auteur")
make = st.text_input("Fabriquant de l'appareil photo", key="Make")
model = st.text_input("Model de l'appareil photo", key="Model")
expose =  st.text_input("Temps d'exposition de l'obturateur", key="ExposureTime")
fnumber = st.text_input("Indique le reglage de l'ouverture de l'objectif", key="FNumber")
isospeedrating = st.text_input("Sensibilité ISO", key="ISOSpeedRatings")
datetimeoriginalimage = st.text_input("Indique l'heure et la date exacte de la prise de vue", key="DateTimeOriginal")
gpsaltitude = st.text_input("GPS Altitude", key="GPSAltitude")
gpslatitude = st.text_input("GPS Latitude", key="GPSLatitude")
gpslongitude = st.text_input("GPS Longitude", key="GPSLongitude")
orientation = st.text_input("Orientation de la photo paysage ou portrait", key="Orientationne")
pixelxdimension = st.text_input("Dimension Pixel X", key="Pixxdim")
pixelydimension = st.text_input("Dimension Pixel y", key="Pixydim")



#print(dir(itismyimage))


# You can access the value at any point with:
#st.session_state.Orientation

#itismyimage.set('artist', 'saloperie')
if st.button('test'):
    print("test")
    print(itismyimage.list_all())#savoir la list

if st.button('test2'):
    print("test")
    with open ('.\Staline_modified.jpg', 'rb') as imageisfile:
        Coucou = Image(imageisfile)
        print(Coucou.list_all())
        
if st.button('test3'):
    print("test3")
    with open ('.\Staline_modified.jpg', 'rb') as imageisfile:
        Coucou = Image(imageisfile)
        print(Coucou.Artist)#imprime l'attribut
        print(Coucou.Make)#imprime l'attribut
        print(Coucou.Model)#imprime l'attribut
        print(Coucou.exposure_time)#imprime l'attribut
        print(Coucou.f_number)#imprime l'attribut
        print(Coucou.iso_speed)#imprime l'attribut
        print(Coucou.datetime)#imprime l'attribut
        print(Coucou.gps_altitude)#imprime l'attribut
        print(Coucou.gps_latitude)#imprime l'attribut
        print(Coucou.gps_longitude)#imprime l'attribut
        print(Coucou.orientation)#imprime l'attribut
        print(Coucou.pixel_x_dimension)#imprime l'attribut
        print(Coucou.pixel_y_dimension)#imprime l'attribut

if st.button('enregistrer dans staline_modified.jpg'):
    itismyimage.Artist = str(auteur) #ok
    print(itismyimage.Artist)
    itismyimage.Make = str(make) #ok
    print(itismyimage.Make)
    itismyimage.Model = str(model) #ok
    print(itismyimage.Model)
    itismyimage.exposure_time = int(expose) #ok
    print(itismyimage.exposure_time)
    itismyimage.f_number = float(fnumber)#ok
    print(itismyimage.f_number)
    itismyimage.iso_speed = float(isospeedrating)#ok
    print(itismyimage.iso_speed)
    itismyimage.datetime = str(datetimeoriginalimage)#ok
    print(itismyimage.datetime)
    itismyimage.gps_altitude = int(gpsaltitude)#ok
    print(itismyimage.gps_altitude)
    itismyimage.gps_latitude = int(gpslatitude)#ok
    print(itismyimage.gps_latitude)
    itismyimage.gps_longitude = int(gpslongitude)#ok
    print(itismyimage.gps_Longitude)
    itismyimage.orientation = int(orientation)#ok
    print(itismyimage.orientation)
    itismyimage.pixel_x_dimension = int(pixelxdimension)#ok
    print(itismyimage.pixel_x_dimension)
    itismyimage.pixel_y_dimension = int(pixelydimension)#ok
    print(itismyimage.pixel_y_dimension)


    print("enregistré")
    with open('.\staline_modified.jpg', 'wb') as new_image_file:
        new_image_file.write(itismyimage.get_file())