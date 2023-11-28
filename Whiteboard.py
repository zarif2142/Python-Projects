import tkinter as tk
from tkinter import ttk

class PaintApp:
    #initialize the paint application
    def __init__(self, root):
        self.root = root
        #canvas dimensions
        self.canvas_width = 800
        self.canvas_height = 600
        #create canvas widget
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='white', bd=3, relief=tk.SUNKEN)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #setup methods
        self.setup_navbar()
        self.setup_tools()
        self.setup_events()
        #coordinates for drawing
        self.prev_x = None
        self.prev_y = None

    #setup the navigation bar
    def setup_navbar(self):
        self.navbar = tk.Menu(self.root)
        self.root.config(menu=self.navbar)

        #file menu with snapshot save and exit
        self.file_menu = tk.Menu(self.navbar, tearoff=0)
        self.navbar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Save Snapshot', command=self.take_snapshot)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.root.quit)

        #edit menu with undo functionality
        self.edit_menu = tk.Menu(self.navbar, tearoff=0)
        self.navbar.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo', command=self.undo)

    #setup the drawing tools
    def setup_tools(self):
        #default selections
        self.selected_tool = 'pen'
        self.colors = ['black', 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white']
        self.selected_color = self.colors[0]
        self.brush_sizes = [2, 4, 6, 8,10,25,50,100]
        self.selected_size = self.brush_sizes[0]
        self.pen_types = ['line', 'round', 'square', 'arrow', 'diamond']
        self.selected_pen_type = self.pen_types[0]

        #tool frame setup
        self.tool_frame = ttk.LabelFrame(self.root, text='Tools')
        self.tool_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.Y)

        #pen and eraser buttons
        self.pen_button = ttk.Button(self.tool_frame, text='Pen', command=self.select_pen_tool)
        self.pen_button.pack(side=tk.TOP, padx=5, pady=5)

        self.eraser_button = ttk.Button(self.tool_frame, text='Eraser', command=self.select_eraser_tool)
        self.eraser_button.pack(side=tk.TOP, padx=5, pady=5)

        #brush size selection
        self.brush_size_label = ttk.Label(self.tool_frame, text='Brush Size:')
        self.brush_size_label.pack(side=tk.TOP, padx=5, pady=5)

        self.brush_size_combobox = ttk.Combobox(self.tool_frame, values=self.brush_sizes, state='readonly')
        self.brush_size_combobox.current(0)
        self.brush_size_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.brush_size_combobox.bind('<<ComboboxSelected>>', lambda event: self.select_size(int(self.brush_size_combobox.get())))

        #color selection
        self.color_label = ttk.Label(self.tool_frame, text='Color:')
        self.color_label.pack(side=tk.TOP, padx=5, pady=5)

        self.color_combobox = ttk.Combobox(self.tool_frame, values=self.colors, state='readonly')
        self.color_combobox.current(0)
        self.color_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.color_combobox.bind('<<ComboboxSelected>>', lambda event: self.select_color(self.color_combobox.get()))

        #pen type selection
        self.pen_type_label = ttk.Label(self.tool_frame, text='Pen Type:')
        self.pen_type_label.pack(side=tk.TOP, padx=5, pady=5)

        self.pen_type_combobox = ttk.Combobox(self.tool_frame, values=self.pen_types, state='readonly')
        self.pen_type_combobox.current(0)
        self.pen_type_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.pen_type_combobox.bind('<<ComboboxSelected>>', lambda event: self.select_pen_type(self.pen_type_combobox.get()))

        #clear canvas button
        self.clear_button = ttk.Button(self.tool_frame, text='Clear Canvas', command=self.clear_canvas)
        self.clear_button.pack(side=tk.TOP, padx=5, pady=5)

        #button to change background color
        self.bg_button = ttk.Button(self.tool_frame, text='Black Background', command=self.change_bg)
        self.bg_button.pack(side=tk.TOP, padx=5, pady=5)

    #setup drawing events
    def setup_events(self):
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.release)

    #select pen tool
    def select_pen_tool(self):
        self.selected_tool = 'pen'

    #select eraser tool
    def select_eraser_tool(self):
        self.selected_tool = 'eraser'

    #select brush size
    def select_size(self, size):
        self.selected_size = size

    #select color
    def select_color(self, color):
        self.selected_color = color

    #select pen type
    def select_pen_type(self, pen_type):
        self.selected_pen_type = pen_type


    #drawing method
    def draw(self, event):
        if self.selected_tool == 'pen':
            if self.prev_x is not None and self.prev_y is not None:
                #line drawing
                if self.selected_pen_type == 'line':
                    self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill=self.selected_color,
                                            width=self.selected_size, smooth=True, capstyle=tk.ROUND)
                #round drawing
                elif self.selected_pen_type == 'round':
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    self.canvas.create_oval(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                #square drawing
                elif self.selected_pen_type == 'square':
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                #arrow drawing
                elif self.selected_pen_type == 'arrow':
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    self.canvas.create_polygon(x1, y1, x1, y2, event.x, y2, fill=self.selected_color,
                                               outline=self.selected_color)
                #diamond drawing
                elif self.selected_pen_type == 'diamond':
                    x1 = event.x - self.selected_size
                    y1 = event.y
                    x2 = event.x
                    y2 = event.y - self.selected_size
                    x3 = event.x + self.selected_size
                    y3 = event.y
                    x4 = event.x
                    y4 = event.y + self.selected_size
                    self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=self.selected_color,
                                               outline=self.selected_color)
            self.prev_x = event.x
            self.prev_y = event.y
        elif self.selected_tool == 'eraser':
            #eraser functionality
            if self.prev_x is not None and self.prev_y is not None:
                self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill=self.canvas['bg'],
                                        width=self.selected_size, capstyle=tk.ROUND)
            self.prev_x = event.x
            self.prev_y = event.y

    #reset coordinates on release
    def release(self, event):
        self.prev_x = None
        self.prev_y = None

    #clear the canvas
    def clear_canvas(self):
        self.canvas.delete('all')

    #save the canvas as a snapshot
    def take_snapshot(self):
        self.canvas.postscript(file='snapshot.eps')

    #undo the last action
    def undo(self):
        items = self.canvas.find_all()
        if items:
            self.canvas.delete(items[-1])

    #change the background color of the canvas
    def change_bg(self):
        #toggle the background color between white and black
        new_bg = 'white' if self.canvas['bg'] == 'black' else 'black'
        self.canvas['bg'] = new_bg
        #update the button text accordingly
        self.bg_button['text'] = 'White Background' if new_bg == 'black' else 'Black Background'

#run the application
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Paint Application')
    app = PaintApp(root)
    root.mainloop()
