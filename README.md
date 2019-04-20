# python_graph_drawing
Python drawing a simple graph and saving as a png file.

This is a simple drawing graph and Hexahedron based on the result of plus and minus operation between two numbers.
mainLine.py is for line graph.
mainSquare.py is for Hexahedron.

Input:
  2 ; number of inputs
  120 ; 120  
  79 ;  120+79
  199 
  
  This will show you the line graph and Hexahedron.
  
Saving:

    nameSav = "1" + '.png'
    tmpdir = tempfile.mkdtemp() 
    tmpfile = os.path.join(tmpdir, 'tmp.svg') 
    ts = turtle.getcanvas()
    canvasvg.saveall(tmpfile, ts)
    with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
        cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
    shutil.rmtree(tmpdir)
    
    I saved canvas a svg file first and then convert svg file to png file using cairosvg.svg2png.
    And it worked well.
    
  Thanks.
