from tkinter import filedialog
import glob
file_path = filedialog.askdirectory(initialdir = "/", title = "Wybierz Folder z koordynatami")
roi = layer('ROI')
directory = glob.glob( f'{file_path}*.txt' )
for item in directory:
    with open( item, "r" ) as f :
        svg_data = f.read()
        new = svg_data.replace("(","").replace(")","")
        coordinates = tuple(map(int,new.split(',')))
        (x, y, w, h) = coordinates
        z_ROI = rect( (x, y), (w, h), stroke_width = 0, fill = '#ffcc00', opacity = 0.5)
        roi.append( z_ROI )

