from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView,FileChooserIconView
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.switch import Switch
from kivy.uix.videoplayer import VideoPlayer
from kivy.animation import Animation
from kivy.graphics import*
new_project_flag = ['none']
load_project_flag = ['none']
edit_project_flag = ['none']
user_interface_flag = ['none']
save_project_flag = ['none']
load_example_flag = ['none']
code_panel_flag = ['none']
help_flag = ['none']
undo_flag = ['none']
widget_flag = ['none']
properties = ['none']
view_type = ['smartphone']
example_flag = ['none']
about_flag = ['none']
file_name = ['code/MyApp.py']
kivy_code = []
widget_added = []
x_coor = []
y_coor = []
project_path = [] 
source_code = []
#class MyPos(Widget):
#    def on_touch_down(self, touch):
#        x_coor.append(touch.x)
#        y_coor.append(touch.y)
class KivyLite(App):
    def build(self):
        #RESTORE INITIAL VALUES
        def clear_app(clear_button):
            win_h.clear_widgets()
            win_c.clear_widgets()
            win_p.clear_widgets()
            win_r.clear_widgets()
            win_undo.clear_widgets()
            new_project_flag.append('none')
            load_project_flag.append('none')
            edit_project_flag.append('none')
            user_interface_flag.append('none')
            save_project_flag.append('none')
            load_example_flag.append('none')
            code_panel_flag.append('none')
            about_flag.append('none')
            help_flag.append('none')
            undo_flag.append('none')
            widget_flag.append('none')
            properties.append('none')
            example_flag.append('none')
            view_type.append('smartphone')
            del(file_name[1:len(file_name)])            
            del(kivy_code[0:len(kivy_code)])
            del(widget_added[0:len(widget_added)])
        #OPEN SAVED PROJECTS AND EXAMPLES
        def open_project():
            win_r.clear_widgets()
            del(kivy_code[0:len(kivy_code)-1])
            try:
                infile = open(file_name[len(file_name)-1],'r')
            except:
                def quit_warning(btn):
                    win_c.remove_widget(pop)
                btn = Button (text='wrong project name', font_size = 16)
                btn.bind(on_press = quit_warning)
                pop = Popup (title='Warning', content=btn, size=(200,200), pos=(300,200))
                win_c.add_widget(pop)
                infile = open('code/MyApp.py','r')
                file_name.append('code/MyApp.py')
            content = infile.readlines()
            try:
                for i in range (0,len(content),1):
                    ########################
                    #READ LABEL PROPERTIES
                    ########################
                    if content[i].count('=Label') >= 1 or content[i].count('= Label') >= 1:
                        if content[i].count('text=') == 1:
                            pos_a = content[i].find('text=')
                            pos_b = content[i].find(',', pos_a + 1)
                            texto = content[i][pos_a + 6:pos_b -1]
                        if content[i].count('font_size=') == 1:
                            pos_a = content[i].find('font_size=')
                            pos_b = content[i].find(',', pos_a + 1)
                            size = int(content[i][pos_a + 10:pos_b])
                        if content[i].count('bold') == 1:
                            tipo = 'bold'
                        if content[i].count('italic') == 1:
                            tipo = 'italic'
                        if content[i].count('bold') == 0 and content[i].count('italic') == 0:
                            tipo = 'normal'
                        if content[i].find('pos=') > 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        if tipo == 'normal': 
                            lbl = Label(text=texto, font_size=size, pos = (int(pos[0]),int(pos[1])))
                        if tipo == 'bold': 
                            lbl = Label(text=texto, font_size=size, bold=True, pos = (int(pos[0]),int(pos[1])))
                        if tipo == 'italic': 
                            lbl = Label(text=texto, font_size=size, italic=True,pos = (int(pos[0]),int(pos[1])))
                        win_r.add_widget(lbl)
                    ########################
                    #READ BUTTON PROPERTIES
                    ########################
                    if content[i].count('=Button') >= 1 or content[i].count('= Button') >= 1:
                        if content[i].count('text=') == 1:
                            pos_a = content[i].find('text=')
                            pos_b = content[i].find(',', pos_a + 1)
                            texto = content[i][pos_a + 6:pos_b -1]
                        if content[i].count('font_size=') == 1:
                            pos_a = content[i].find('font_size=')
                            pos_b = content[i].find(',', pos_a + 1)
                            size = int(content[i][pos_a + 10:pos_b])
                        if content[i].count('bold') == 1:
                            tipo = 'bold'
                        if content[i].count('italic') == 1:
                            tipo = 'italic'
                        if content[i].count('bold') == 0 and content[i].count('italic') == 0:
                            tipo = 'normal'
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        if tipo == 'normal': 
                            btn = Button(text=texto, font_size=size, width = 100, height = 25, pos = (int(pos[0]),int(pos[1])))
                        if tipo == 'bold': 
                            btn = Button(text=texto, font_size=size, width = 100, height = 25, bold=True, pos = (int(pos[0]),int(pos[1])))
                        if tipo == 'italic': 
                           btn = Button(text=texto, font_size=size, width = 100, height = 25, italic=True,pos = (int(pos[0]),int(pos[1])))
                        win_r.add_widget(btn)
                    ###########################
                    #READ TEXTINPUT PROPERTIES
                    ###########################
                    if content[i].count('=TextInput') >= 1 or content[i].count('= TextInput') >= 1:
                        if content[i].count('font_size=') == 1:
                            pos_a = content[i].find('font_size=')
                            pos_b = content[i].find(',', pos_a + 1)
                            size = int(content[i][pos_a + 10:pos_b])
                        if content[i].count('width=') == 1:
                            pos_a = content[i].find('width=')
                            pos_b = content[i].find(',', pos_a + 1)
                            wide = int(content[i][pos_a + 6:pos_b])
                        if content[i].count('height=') == 1:
                            pos_a = content[i].find('height=')
                            pos_b = content[i].find(',', pos_a + 1)
                            high = int(content[i][pos_a + 7:pos_b])
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        txti = TextInput (font_size=size, width=wide, height=high, pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(txti)
                    ##########################
                    #READ CHECKBOX PROPERTIES
                    ##########################
                    if content[i].count('=CheckBox') >= 1 or content[i].count('= CheckBox') >= 1:
                        if content[i].count('group=') == 1:
                            pos_a = content[i].find('group=')
                            pos_b = content[i].find(',', pos_a + 1)
                            group = content[i][pos_a + 7:pos_b -1]
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        if len(group) == 0:
                            chkb = CheckBox(pos=(int(pos[0]), int(pos[1])))
                        if len(group) > 0:
                            chkb = CheckBox(group = group, pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(chkb)
                    #############################
                    #READ TOGGLEBUTTON PROPERTIES
                    #############################
                    if content[i].count('=ToggleButton') >= 1 or content[i].count('= ToggleButton') >= 1:
                        if content[i].count('text=') == 1:
                            pos_a = content[i].find('text=')
                            pos_b = content[i].find(',', pos_a + 1)
                            texto = content[i][pos_a + 6:pos_b -1]
                        if content[i].count('font_size=') == 1:
                            pos_a = content[i].find('font_size=')
                            pos_b = content[i].find(',', pos_a + 1)
                            size = int(content[i][pos_a + 10:pos_b])
                        if content[i].count('bold') == 1:
                            tipo = 'bold'
                        if content[i].count('italic') == 1:
                            tipo = 'italic'
                        if content[i].count('bold') == 0 and content[i].count('italic') == 0:
                            tipo = 'normal'
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        if tipo == 'normal': 
                            btn = ToggleButton(text=texto, font_size=size, width = 100, height = 25, pos = (int(pos[0]),int(pos[1])))
                        if tipo == 'bold': 
                            btn = ToggleButton(text=texto, font_size=size, width = 100, height = 25, bold=True, pos = (int(pos[0]),int(pos[1])))
                        if tipo == 'italic': 
                            btn = ToggleButton(text=texto, font_size=size, width = 100, height = 25, italic=True,pos = (int(pos[0]),int(pos[1])))
                        win_r.add_widget(btn)
                    #######################
                    #READ IMAGE PROPERTIES
                    #######################
                    if content[i].count('=Image') >= 1 or content[i].count('= Image') >= 1:
                        if content[i].count('source=') == 1:
                            pos_a = content[i].find('source=')
                            pos_b = content[i].find(',', pos_a + 1)
                            path = content[i][pos_a + 8:pos_b-1]
                        if content[i].count('size=') == 1:
                            pos_a = content[i].find('size=')
                            pos_b = content[i].find(')', pos_a + 1)
                            size = content[i][pos_a + 6:pos_b]
                            size = size.strip().split(',')
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        img = Image (source=path, size=(int(size[0]), int(size[1])), pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(img)
                    #############################
                    #READ FILECHOOSER PROPERTIES
                    #############################
                    if content[i].count('=FileChooser') >= 1 or content[i].count('= FileChooser') >= 1:
                        if content[i].count('size=') == 1:
                            pos_a = content[i].find('size=')
                            pos_b = content[i].find(')', pos_a + 1)
                            size = content[i][pos_a + 6:pos_b]
                            size = size.strip().split(',')
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        if content[i].count('ListView') == 1:
                            fc = FileChooserListView (size=(int(size[0]),int(size[1])), pos=(int(pos[0]), int(pos[1])))
                        if content[i].count('IconView') == 1:
                            fc = FileChooserIconView (size=(int(size[0]),int(size[1])), pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(fc)
                    ########################
                    #READ SPINNER PROPERTIES
                    ########################
                    if content[i].count('=Spinner') >= 1 or content[i].count('= Spinner') >= 1:
                        if content[i].count('text=') == 1:
                            pos_a = content[i].find('text=')
                            pos_b = content[i].find(',', pos_a + 1)
                            texto = content[i][pos_a + 6:pos_b -1]
                        if content[i].count('values=') == 1:
                            pos_a = content[i].find('values=')
                            pos_b = content[i].find(')', pos_a + 1)
                            values = content[i][pos_a + 8:pos_b]. replace("'","")
                            values = values.strip().split(',')
                        if content[i].count('size=') == 1:
                            pos_a = content[i].find('size=')
                            pos_b = content[i].find(')', pos_a + 1)
                            size = content[i][pos_a + 6:pos_b]
                            size = size.strip().split(',')
                            print(size)
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                            print(pos)
                        sp = Spinner(text = texto, font_size = 15, values = (values[0], values[1], values[2]), size = (int(size[0]),int(size[1])), pos=(int(pos[0]),int(pos[1])))
                        win_r.add_widget(sp)
                    ########################
                    #READ SLIDER PROPERTIES
                    ########################
                    if content[i].count('=Slider') >= 1 or content[i].count('= Slider') >= 1:
                        if content[i].count('orientation=') == 1:
                            pos_a = content[i].find('orientation=')
                            pos_b = content[i].find(',', pos_a + 1)
                            orient = content[i][pos_a + 13:pos_b-1]
                        if content[i].count('width=') == 1:
                            pos_a = content[i].find('width=')
                            pos_b = content[i].find(',', pos_a + 1)
                            wide = int(content[i][pos_a + 6:pos_b])
                        if content[i].count('height=') == 1:
                            pos_a = content[i].find('height=')
                            pos_b = content[i].find(',', pos_a + 1)
                            high = int(content[i][pos_a + 7:pos_b])
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        sl = Slider (width=wide, height=high, max = 100, value = 25, orientation= orient, pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(sl)
                    #############################
                    #READ PROGRESSBAR PROPERTIES
                    #############################
                    if content[i].count('=ProgressBar') >= 1 or content[i].count('= ProgressBar') >= 1:
                        if content[i].count('value=') == 1:
                            pos_a = content[i].find('value=')
                            pos_b = content[i].find(',', pos_a + 1)
                            value = int(content[i][pos_a + 6:pos_b])
                        if content[i].count('width=') == 1:
                            pos_a = content[i].find('width=')
                            pos_b = content[i].find(',', pos_a + 1)
                            wide = int(content[i][pos_a + 6:pos_b])
                        if content[i].count('max=') == 1:
                            pos_a = content[i].find('max=')
                            pos_b = content[i].find(',', pos_a + 1)
                            max_value = int(content[i][pos_a + 4:pos_b])
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        pb = ProgressBar(value = value, max = max_value, width=wide, pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(pb)
                    ########################
                    #READ SWITCH PROPERTIES
                    ########################
                    if content[i].count('=Switch') >= 1 or content[i].count('= Switch') >= 1:
                        if content[i].count('active=') == 1:
                            pos_a = content[i].find('active=')
                            pos_b = content[i].find(',', pos_a + 1)
                            active = content[i][pos_a + 7:pos_b]
                        if content[i].count('size=') == 1:
                            pos_a = content[i].find('size=')
                            pos_b = content[i].find(')', pos_a + 1)
                            size = content[i][pos_a + 6:pos_b]
                            size = size.strip().split(',')
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        if active == 'True':
                            sw = Switch (size=(int(size[0]), int(size[1])), active= True, pos=(int(pos[0]), int(pos[1])))
                        if active == 'False':
                            sw = Switch (size=(int(size[0]), int(size[1])), active= False, pos=(int(pos[0]), int(pos[1])))
                        win_r.add_widget(sw)
                     #############################
                     #READ VIDEOPLAYER PROPERTIES
                     #############################
                    if content[i].count('=VideoPlayer') >= 1 or content[i].count('= VideoPlayer') >= 1:
                        if content[i].count('source=') == 1:
                            pos_a = content[i].find('source=')
                            pos_b = content[i].find(',', pos_a + 1)
                            path = content[i][pos_a + 8:pos_b-1]
                        if content[i].count('size=') == 1:
                            pos_a = content[i].find('size=')
                            pos_b = content[i].find(')', pos_a + 1)
                            size = content[i][pos_a + 6:pos_b]
                            size = size.strip().split(',')
                        if content[i].count('pos=') == 1:
                            pos_a = content[i].find('pos=')
                            pos_b = content[i].find(')', pos_a + 1)
                            pos = content[i][pos_a + 5:pos_b]
                            pos = pos.strip().split(',')
                        vp = VideoPlayer (source=path, size=(int(size[0]), int(size[1])), pos=(int(pos[0]), int(pos[1])))
                        vp.state = 'play'
                        win_r.add_widget(vp)
            except:
                pass    
#########################
##CREATE NEW PROJECT
#########################
        def create_project(start_project):
            new_project_flag.append('true')
            def save_project(save):
                if save_project_flag[len(save_project_flag)-1] == 'none' and user_interface_flag[len(user_interface_flag)-1] == 'none' and code_panel_flag[len(code_panel_flag)-1] == 'none':
                    def save_code(get_path):
                        if len(file_textinput.text) == 0:
                            def quit_warning(btn):
                                win_c.remove_widget(popup)
                            btn = Button (text='file name empty', font_size = 16)
                            btn.bind(on_press = quit_warning)
                            popup = Popup (title='Warning', content=btn, size=(200,200), pos=(300,100))
                            win_c.add_widget(popup)
                        if len(file_textinput.text) > 0 and len(source_code) > 0:
                            outfile = open(fc.path + '/' + file_textinput.text, 'w')
                            for i in range (0,len(source_code),1):
                                outfile.write(source_code[i])
                            outfile.close()
                            save_project_flag.append('none')
                            new_project_flag.append('none')
                            win_c.clear_widgets()
                            win_h.clear_widgets()
                            def quit_warning(btn):
                                win_c.remove_widget(pop)
                                win_undo.clear_widgets()
                            btn = Button (text='Project saved', font_size = 16)
                            btn.bind(on_press = quit_warning)
                            pop = Popup (title='Save', content=btn, size=(200,200), pos=(300,200))
                            win_c.add_widget(pop)
                        if len(source_code) == 0:
                            def quit_warning(btn):
                                win_c.remove_widget(pop)
                            btn = Button (text='Check code before saving', font_size = 14)
                            btn.bind(on_press = quit_warning)
                            pop = Popup (title='Warning', content=btn, size=(200,200), pos=(300,100))
                            win_c.add_widget(pop)
                    def quit_save_project(close_fc):
                        win_c.clear_widgets()
                        save_project_flag.append('none')
                    def file_selection(fc,selection):
                        file_path = str(fc.selection)
                        inver_path = file_path[::-1]
                        touse = inver_path.strip().split('/')
                        touse = touse[0].replace(']','') 
                        touse = touse.replace("'",'')
                        touse = touse[::-1]
                        file_textinput.scroll_y = 0
                        file_textinput.text = ''
                        file_textinput.insert_text(touse)
                    save_project_flag.append('true')
                    file_label = Label(text = '[b]File name:[/b]', markup = True, font_size = 18, pos = (250,250))
                    file_textinput = TextInput(font_size = 15, width = 200, height = 30, pos = (350, 285))
                    fc = FileChooserListView(path='projects',size = (320,140), pos = (250,120))
                    fc.bind(selection = file_selection)
                    get_path = Button(text='save', font_size = 15, width = 100, height = 25, pos = (230,70), background_color=(0,0,0.2,0))
                    get_path.bind(on_press = save_code)
                    close_fc = Button(text='close',font_size = 15, width = 100, height = 25, pos = (500,70), background_color = (0,0,0.2,0))
                    close_fc.bind(on_press = quit_save_project)
                    win_c.add_widget(file_label)
                    win_c.add_widget(file_textinput)
                    win_c.add_widget(fc)
                    win_c.add_widget(get_path)
                    win_c.add_widget(close_fc)
            def interface(gui):
                def close_interface(close_panel):
                    if properties[len(properties)-1] == 'none':
                        user_interface_flag.append('none')
                        win_c.clear_widgets()
                        win_p.clear_widgets()
                def widget_warning():
                    def quit_warning(btn):
                        win_c.remove_widget(pop)
                        widget_flag.append('none')
                    btn = Button (text='Missing field', font_size = 16)
                    btn.bind(on_press = quit_warning)
                    pop = Popup (title='Warning', content=btn, size=(200,200), pos=(300,200))
                    win_c.add_widget(pop)
                ###################
                ###LABEL PROPERTIES
                ###################
                def label_properties(label):
                    def set_label(put_widget):
                        def undo_label(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(label_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                texto = label_textinput.text
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 150:
                                    pos[0] = 150
                                if int(pos[1]) > 330:
                                    pos[1] = 330
                                if type_spinner.text == 'italic':
                                    label_object = Label(text=texto,font_size = int(fontsize_textinput.text), italic = True, pos =(630 + int(pos[0]), 350 - int(pos[1])))
                                    kivy_code.append('lbl=Label(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'italic=True' + ',' + 'pos=(' + str(630 + int(pos[0])) + ',' + str(350 - int(pos[1])) + '))')
                                if type_spinner.text == 'bold':
                                    label_object = Label(text=texto,font_size = int(fontsize_textinput.text), bold = True, pos =(630 + int(pos[0]), 350 - int(pos[1]))) 
                                    kivy_code.append('lbl=Label(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'bold=True' + ',' + 'pos=(' + str(630 + int(pos[0])) + ',' + str(350 - int(pos[1])) + '))')
                                if type_spinner.text == 'normal':
                                    label_object = Label(text=texto,font_size = int(fontsize_textinput.text), pos =(630 + int(pos[0]), 350 - int(pos[1])))
                                    kivy_code.append('lbl=Label(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'pos=(' + str(630 + int(pos[0])) + ',' + str(350 - int(pos[1])) + '))')
                                widget_added.append('label')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))
                                undo.bind(on_press = undo_label)
                                label_textinput.bind(text=label_object.setter('text'))
                                win_r.add_widget(label_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_label_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        label_title = Label(text = '[b]Label Properties[/b]', markup = True, font_size = 20, pos = (290,100))
                        label_text=Label(text='[b]text:[/b]',markup = True, font_size=15, pos = (20,50))
                        label_textinput=TextInput(text='Label', font_size=15, width=100, height=30, pos=(100,90))
                        fontsize_text = Label(text='[b]size:[/b]',markup = True, font_size=15, pos = (20,20))
                        fontsize_textinput=TextInput(text = '15', font_size=15, width=100, height=30, multiline = False, pos=(100,50))
                        type_text = Label(text='[b]type:[/b]',markup = True, font_size=15, pos = (200,50))
                        type_spinner = Spinner (text='normal',values = ('normal', 'bold', 'italic'), background_color = (0,0,0.2,0), fontsize = 15, size = (100,25), pos = (270,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_label)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_label_properties)
                        win_p.add_widget(label_textinput)
                        win_p.add_widget(label_text)
                        win_p.add_widget(fontsize_text)
                        win_p.add_widget(fontsize_textinput)
                        win_p.add_widget(type_text)
                        win_p.add_widget(type_spinner)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(label_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                ####################
                ###BUTTON PROPERTIES
                ####################
                def button_properties(button):
                    def set_button(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(button_object)
                            del(kivy_code[len(kivy_code)-1])
                            del (widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                texto = button_textinput.text
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 85:
                                    pos[0] = 85
                                if int(pos[1]) > 300:
                                    pos[1] = 300
                                if type_spinner.text == 'italic':
                                    button_object = Button(text=button_textinput.text,font_size = int(fontsize_textinput.text), width = 100, height = 25, italic = True, pos =(670 + int(pos[0]),370 - int(pos[1])))
                                    kivy_code.append('btn=Button(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'italic=True' + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                if type_spinner.text == 'bold':
                                    button_object = Button(text=button_textinput.text,font_size = int(fontsize_textinput.text), width = 100, height = 25, bold = True, pos =(670 + int(pos[0]),370 - int(pos[1])))
                                    kivy_code.append('btn=Button(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'bold=True' + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                if type_spinner.text == 'normal':
                                    button_object = Button(text=button_textinput.text,font_size = int(fontsize_textinput.text), width = 100, height = 25, pos =(670 + int(pos[0]),370 - int(pos[1])))           
                                    kivy_code.append('btn=Button(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                widget_added.append('button')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))
                                button_textinput.bind(text=button_object.setter('text'))                                                
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(button_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_button_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        button_title = Label(text = '[b]Button Properties[/b]', markup = True, font_size = 20, pos = (290,100))
                        button_text=Label(text='[b]text:[/b]',markup = True, font_size=15, pos = (20,50))
                        button_textinput=TextInput(text='Button', font_size=15, width=100, height=30, pos=(100,90))
                        fontsize_text = Label(text='[b]size:[/b]',markup = True, font_size=15, pos = (20,20))
                        fontsize_textinput=TextInput(text = '15', font_size=15, width=100, height=30, multiline = False, pos=(100,50))
                        type_text = Label(text='[b]type:[/b]',markup = True, font_size=15, pos = (200,50))
                        type_spinner = Spinner (text='normal',values = ('normal', 'bold', 'italic'), background_color = (0,0,0.2,0), fontsize = 15, size = (100,25), pos = (270,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_button)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_button_properties)
                        win_p.add_widget(button_textinput)
                        win_p.add_widget(button_text)
                        win_p.add_widget(fontsize_text)
                        win_p.add_widget(fontsize_textinput)
                        win_p.add_widget(type_text)
                        win_p.add_widget(type_spinner)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(button_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                #######################        
                ###TEXTINPUT PROPERTIES
                #######################
                def textinput_properties(textinput):
                    def set_textinput(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(textinput_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 85:
                                    pos[0] = 85
                                if int(pos[1]) > 300:
                                    pos[1] = 300
                                textinput_object=TextInput(font_size = int(fontsize_textinput.text), width = int(width_textinput.text), height = int(height_textinput.text), pos =(670 + int(pos[0]),370 - int(pos[1])))
                                kivy_code.append('txti=TextInput(font_size=' + str(int(fontsize_textinput.text)) + ',' + 'width=' + str(int(width_textinput.text)) + ',' + 'height=' + str(int(height_textinput.text)) + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                widget_added.append('textinput')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(textinput_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_textinput_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        textinput_title = Label(text = '[b]TextInput Properties[/b]', markup = True, font_size = 20, pos = (310,100))
                        fontsize_text = Label(text='[b]size:[/b]',markup = True, font_size=15, pos = (20,50))
                        fontsize_textinput=TextInput(text = '15', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        width_text = Label(text = '[b]width:[/b]', markup = True, font_size = 15, pos = (20,20))
                        width_textinput = TextInput(text = '100', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        height_text = Label(text = '[b]height:[/b]', markup = True, font_size = 15, pos = (200,50))
                        height_textinput = TextInput(text = '25', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_textinput)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_textinput_properties)
                        win_p.add_widget(fontsize_text)
                        win_p.add_widget(fontsize_textinput)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(height_text)
                        win_p.add_widget(height_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(textinput_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                ######################
                ###CHECKBOX PROPERTIES
                ######################
                def checkbox_properties(textinput):
                    def set_textinput(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(checkbox_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 150:
                                    pos[0] = 150
                                if int(pos[1]) > 330:
                                    pos[1] = 330
                                checkbox_object=CheckBox(group = group_textinput.text, pos =(670 + int(pos[0]),350 - int(pos[1])))
                                kivy_code.append('chkb=CheckBox(group=' + "'" + group_textinput.text + "'" + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(350 - int(pos[1])) + '))')
                                widget_added.append('checkbox')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(checkbox_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_checkbox_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        checkbox_title = Label(text = '[b]Checkbox Properties[/b]', markup = True, font_size = 20, pos = (310,100))
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (20,50))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        group_text = Label(text='[b]group:[/b]',markup = True, font_size=15, pos = (20,20))
                        group_textinput=TextInput(text = '', font_size=15, width=100, height=30, multiline = False, pos=(100,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_textinput)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_checkbox_properties)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(group_text)
                        win_p.add_widget(group_textinput)
                        win_p.add_widget(checkbox_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                ##########################
                ###TOGGLEBUTTON PROPERTIES
                ##########################
                def togglebutton_properties(button):
                    def set_button(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(button_object)
                            del(kivy_code[len(kivy_code)-1])
                            del (widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                texto = button_textinput.text
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 85:
                                    pos[0] = 85
                                if int(pos[1]) > 300:
                                    pos[1] = 300
                                if type_spinner.text == 'italic':
                                    button_object = ToggleButton(text=button_textinput.text,font_size = int(fontsize_textinput.text), width = 100, height = 25, italic = True, pos =(670 + int(pos[0]),370 - int(pos[1])))
                                    kivy_code.append('btn=ToggleButton(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'italic=True' + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                if type_spinner.text == 'bold':
                                    button_object = ToggleButton(text=button_textinput.text,font_size = int(fontsize_textinput.text), width = 100, height = 25, bold = True, pos =(670 + int(pos[0]),370 - int(pos[1])))
                                    kivy_code.append('btn=ToggleButton(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'bold=True' + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                if type_spinner.text == 'normal':
                                    button_object = ToggleButton(text=button_textinput.text,font_size = int(fontsize_textinput.text), width = 100, height = 25, pos =(670 + int(pos[0]),370 - int(pos[1])))           
                                    kivy_code.append('btn=ToggleButton(text=' + "'" + texto + "'" + ',' + 'font_size=' + str(int(fontsize_textinput.text)) + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                widget_added.append('togglebutton')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))
                                button_textinput.bind(text=button_object.setter('text'))                                                
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(button_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_button_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        button_title = Label(text = '[b]ToggleButton Properties[/b]', markup = True, font_size = 20, pos = (350,100))
                        button_text=Label(text='[b]text:[/b]',markup = True, font_size=15, pos = (20,50))
                        button_textinput=TextInput(text='ToggleButton', font_size=15, width=100, height=30, pos=(100,90))
                        fontsize_text = Label(text='[b]size:[/b]',markup = True, font_size=15, pos = (20,20))
                        fontsize_textinput=TextInput(text = '15', font_size=15, width=100, height=30, multiline = False, pos=(100,50))
                        type_text = Label(text='[b]type:[/b]',markup = True, font_size=15, pos = (200,50))
                        type_spinner = Spinner (text='normal',values = ('normal', 'bold', 'italic'), background_color = (0,0,0.2,0), fontsize = 15, size = (100,25), pos = (270,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_button)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_button_properties)
                        win_p.add_widget(button_textinput)
                        win_p.add_widget(button_text)
                        win_p.add_widget(fontsize_text)
                        win_p.add_widget(fontsize_textinput)
                        win_p.add_widget(type_text)
                        win_p.add_widget(type_spinner)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(button_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                ####################
                ###IMAGE PROPERTIES
                ####################
                def image_properties(image):
                    def set_image(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(image_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 130:
                                    pos[0] = 130
                                if int(pos[1]) > 260:
                                    pos[1] = 260
                                image_object = Image(source = source_textinput.text, size = (int(width_textinput.text), int(height_textinput.text)), pos =(670 + int(pos[0]),320 - int(pos[1])))
                                kivy_code.append('img=Image(source=' + "'" + source_textinput.text + "'" + ',' + 'size=(' + str(int(width_textinput.text)) + ',' +  str(int(height_textinput.text)) +'),' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(320 - int(pos[1])) + '))')
                                widget_added.append('image')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                      
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(image_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_image_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        image_title = Label(text = '[b]Image Properties[/b]', markup = True, font_size = 20, pos = (310,100))
                        source_text = Label(text='[b]source:[/b]',markup = True, font_size=15, pos = (20,50))
                        source_textinput=TextInput(text = '', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        width_text = Label(text = '[b]width:[/b]', markup = True, font_size = 15, pos = (20,20))
                        width_textinput = TextInput(text = '50', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        height_text = Label(text = '[b]height:[/b]', markup = True, font_size = 15, pos = (200,50))
                        height_textinput = TextInput(text = '50', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_image)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_image_properties)
                        win_p.add_widget(source_text)
                        win_p.add_widget(source_textinput)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(height_text)
                        win_p.add_widget(height_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(image_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                #########################
                ###FILECHOOSER PROPERTIES
                #########################
                def filechooser_properties(filechooser):
                    def set_filechooser(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(filechooser_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 75:
                                    pos[0] = 75
                                if int(pos[1]) > 260:
                                    pos[1] = 260
                                if type_textinput.text == 'ListView': 
                                    filechooser_object = FileChooserListView(size = (int(width_textinput.text), int(height_textinput.text)), pos =(670 + int(pos[0]),320 - int(pos[1])))
                                    kivy_code.append('fc=FileChooserListView(size=(' + str(int(width_textinput.text)) +',' + str(int(height_textinput.text)) + '),' +  'pos=(' + str(670 + int(pos[0])) + ',' + str(320 - int(pos[1])) + '))')
                                if type_textinput.text == 'IconView': 
                                    filechooser_object = FileChooserIconView(size = (int(width_textinput.text), int(height_textinput.text)), pos =(670 + int(pos[0]),320 - int(pos[1])))
                                    kivy_code.append('fc=FileChooserIconView(size=(' + str(int(width_textinput.text)) +',' + str(int(height_textinput.text)) + '),' +  'pos=(' + str(670 + int(pos[0])) + ',' + str(320 - int(pos[1])) + '))')
                                widget_added.append('filechooser')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                    
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(filechooser_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_filechooser_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        filechooser_title = Label(text = '[b]FileChooser Properties[/b]', markup = True, font_size = 20, pos = (320,100))
                        width_text = Label(text='[b]width:[/b]',markup = True, font_size=15, pos = (20,50))
                        width_textinput=TextInput(text = '100', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        height_text = Label(text = '[b]height:[/b]', markup = True, font_size = 15, pos = (20,20))
                        height_textinput = TextInput(text = '100', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        type_text = Label(text = '[b]type:[/b]', markup = True, font_size = 15, pos = (200,50))
                        type_textinput = TextInput(text = 'ListView', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_filechooser)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_filechooser_properties)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(height_text)
                        win_p.add_widget(height_textinput)
                        win_p.add_widget(type_text)
                        win_p.add_widget(type_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(filechooser_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                #####################
                ###SPINNER PROPERTIES
                #####################
                def spinner_properties(slider):
                    def set_spinner(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(spinner_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 85:
                                    pos[0] = 85
                                if int(pos[1]) > 300:
                                    pos[1] = 300
                                size = size_textinput.text
                                size = size.strip().split(',')
                                value = value_textinput.text
                                value = value.strip().split(',')
                                spinner_object = Spinner(text = spinner_textinput.text, values = (value[0],value[1],value[2]), size = (int(size[0]), int(size[1])), pos =(670 + int(pos[0]),370 - int(pos[1])))                  
                                kivy_code.append('sp=Spinner(text=' + "'" + spinner_textinput.text + "'" + ',' + 'values=(' + "'" + value[0] + "'" + ',' + "'" + value[1]+ "'" + ',' + "'" + value[2]+ "'" + '),'  + 'size=(' +str(int(size[0])) + ',' + str(int(size[1])) + '),' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                widget_added.append('spinner')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                  
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(spinner_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_spinner_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        spinner_title = Label(text = '[b]Spinner Properties[/b]', markup = True, font_size = 20, pos = (310,100))
                        spinner_text = Label(text='[b]text:[/b]',markup = True, font_size=15, pos = (20,50))
                        spinner_textinput=TextInput(text = 'home', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        value_text = Label(text = '[b]values:[/b]', markup = True, font_size = 15, pos = (20,20))
                        value_textinput = TextInput(text = 'home,file,edit', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        size_text = Label(text = '[b]size:[/b]', markup = True, font_size = 15, pos = (200,50))
                        size_textinput = TextInput(text = '100,25', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_spinner)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_spinner_properties)
                        win_p.add_widget(spinner_text)
                        win_p.add_widget(spinner_textinput)
                        win_p.add_widget(value_text)
                        win_p.add_widget(value_textinput)
                        win_p.add_widget(size_text)
                        win_p.add_widget(size_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(spinner_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                #################### 
                ###SLIDER PROPERTIES
                ####################
                def slider_properties(slider):
                    def set_slider(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(slider_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 170 and orient_textinput.text == 'vertical':
                                    pos[0] = 170
                                if int(pos[1]) > 250 and orient_textinput.text == 'vertical':
                                    pos[1] = 250
                                if int(pos[0]) > 85 and orient_textinput.text == 'horizontal':
                                    pos[0] = 85
                                if int(pos[1]) > 240 and orient_textinput.text == 'horizontal':
                                    pos[1] = 240
                                if orient_textinput.text == 'vertical':
                                    wide = 0
                                    high = int(height_textinput.text)
                                    if high > 370:
                                        high = 370
                                if orient_textinput.text == 'horizontal':
                                    wide = int(width_textinput.text)
                                    high = 0
                                    if wide > 180:
                                        wide = 180
                                slider_object = Slider(width = wide, height = high, min = 0, max = 100, value = 25, orientation = orient_textinput.text, pos =(670 + int(pos[0]),300 - int(pos[1])))
                                kivy_code.append('sl=Slider(width=' + str(wide) + ',' + 'height=' + str(high) + ',min=0,max=100,value=25,orientation=' + "'" + orient_textinput.text + "'" + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(300 - int(pos[1])) + '))')
                                widget_added.append('slider')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                      
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(slider_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_slider_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        slider_title = Label(text = '[b]Slider Properties[/b]', markup = True, font_size = 20, pos = (310,100))
                        width_text = Label(text='[b]width:[/b]',markup = True, font_size=15, pos = (20,50))
                        width_textinput=TextInput(text = '0', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        height_text = Label(text = '[b]height:[/b]', markup = True, font_size = 15, pos = (20,20))
                        height_textinput = TextInput(text = '100', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        orient_text = Label(text = '[b]orient:[/b]', markup = True, font_size = 15, pos = (200,50))
                        orient_textinput = TextInput(text = 'vertical', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_slider)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_slider_properties)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(height_text)
                        win_p.add_widget(height_textinput)
                        win_p.add_widget(orient_text)
                        win_p.add_widget(orient_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(slider_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                ##########################
                ###PROGRESSBAR PROPERTIES
                ##########################
                def progressbar_properties(progressbar):
                    def set_progressbar(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(progressbar_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 80:
                                    pos[0] = 80
                                if int(pos[1]) > 300:
                                    pos[1] = 300
                                wide = int(width_textinput.text)
                                if wide > 180:
                                    wide = 180
                                progressbar_object = ProgressBar(max = int(max_textinput.text), width = wide, value = int(value_textinput.text), pos =(670 + int(pos[0]),320 - int(pos[1])))
                                kivy_code.append('pb=ProgressBar(max=' + str(int(max_textinput.text)) + ',' + 'width=' + str(int(width_textinput.text)) + ',' + 'value=' + str(int(value_textinput.text)) + ',' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(320 - int(pos[1])) + '))')
                                widget_added.append('progressbar')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                        
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(progressbar_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_progressbar_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        progressbar_title = Label(text = '[b]ProgressBar Properties[/b]', markup = True, font_size = 20, pos = (320,100))
                        width_text = Label(text='[b]width:[/b]',markup = True, font_size=15, pos = (20,50))
                        width_textinput=TextInput(text = '100', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        max_text = Label(text = '[b]max:[/b]', markup = True, font_size = 15, pos = (20,20))
                        max_textinput = TextInput(text = '100', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        value_text = Label(text = '[b]value:[/b]', markup = True, font_size = 15, pos = (200,50))
                        value_textinput = TextInput(text = '25', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_progressbar)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press = close_progressbar_properties)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(max_text)
                        win_p.add_widget(max_textinput)
                        win_p.add_widget(value_text)
                        win_p.add_widget(value_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(progressbar_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                ####################
                ###SWITCH PROPERTIES
                ####################
                def switch_properties(switch):
                    def set_switch(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(switch_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0
                                if int(pos[0]) > 85:
                                    pos[0] = 85
                                if int(pos[1]) > 300:
                                    pos[1] = 300
                                if active_textinput.text == 'True':
                                    switch_object = Switch(size=(int(width_textinput.text), int(height_textinput.text)), active = True, pos =(670 + int(pos[0]),370 - int(pos[1])))
                                    kivy_code.append('sw=Switch(size=('+ str(int(width_textinput.text)) + ',' + str(int(height_textinput.text)) + '),' + 'active=True,' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                if active_textinput.text == 'False':
                                    switch_object = Switch(size=(int(width_textinput.text), int(height_textinput.text)), active = False, pos =(670 + int(pos[0]),370 - int(pos[1])))
                                    kivy_code.append('sw=Switch(size=('+ str(int(width_textinput.text)) + ',' + str(int(height_textinput.text)) + '),' + 'active=False,' + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                widget_added.append('switch')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                                               
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(switch_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_switch_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        switch_title = Label(text = '[b]Switch Properties[/b]', markup = True, font_size = 20, pos = (310,100))
                        width_text = Label(text='[b]width:[/b]',markup = True, font_size=15, pos = (20,50))
                        width_textinput=TextInput(text = '100', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        height_text = Label(text = '[b]height:[/b]', markup = True, font_size = 15, pos = (20,20))
                        height_textinput = TextInput(text = '20', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        active_text = Label(text = '[b]active:[/b]', markup = True, font_size = 15, pos = (200,50))
                        active_textinput = TextInput(text = 'False', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_switch)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_switch_properties)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(height_text)
                        win_p.add_widget(height_textinput)
                        win_p.add_widget(active_text)
                        win_p.add_widget(active_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(switch_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                #########################
                ###VIDEOPLAYER PROPERTIES
                #########################
                def videoplayer_properties(image):
                    def set_videoplayer(put_widget):
                        def undo_button(undo):
                            undo_flag.append('true')
                            win_r.remove_widget(videoplayer_object)
                            del(kivy_code[len(kivy_code)-1])
                            del(widget_added[len(widget_added)-1])
                            win_undo.clear_widgets()
                            widget_flag.append('none')
                        undo_flag.append('none')
                        try:
                            if widget_flag[len(widget_flag)-1] == 'none' and view_type[len(view_type)-1] == 'smartphone':
                                widget_flag.append('true')
                                pos = pos_textinput.text
                                pos = pos.strip().split(',')
                                if int(pos[0]) < 0:
                                    pos[0] = 0
                                if int(pos[1]) < 0:
                                    pos[1] = 0 
                                if int(pos[0]) > 5:
                                    pos[0] = 0
                                if int(pos[1]) > 260:
                                    pos[1] = 260
                                videoplayer_object = VideoPlayer(source = source_textinput.text, size = (int(width_textinput.text), int(height_textinput.text)), state = 'play',pos =(670 + int(pos[0]),320 - int(pos[1])))
                                kivy_code.append('vp=VideoPlayer(source=' + "'" + source_textinput.text + "'" + ',' + 'size=(' +str(int(width_textinput.text)) + ',' + str(int(height_textinput.text)) + '),' + "state= 'play'," + 'pos=(' + str(670 + int(pos[0])) + ',' + str(370 - int(pos[1])) + '))')
                                widget_added.append('videoplayer')
                                undo = Button (text='undo',font_size = 15,width = 50,height=25, background_color = (1.5,1,0.5,0), pos = (725,15))                  
                                undo.bind(on_press = undo_button)
                                win_r.add_widget(videoplayer_object)
                                win_undo.add_widget(undo)
                        except:
                            widget_warning()
                    def close_videoplayer_properties(close_properties):
                        properties.append('none')
                        win_p.clear_widgets()
                        widget_flag.append('none')
                    if properties[len(properties)-1] == 'none':
                        properties.append('true')
                        videoplayer_title = Label(text = '[b]VideoPlayer Properties[/b]', markup = True, font_size = 20, pos = (320,100))
                        source_text = Label(text='[b]source:[/b]',markup = True, font_size=15, pos = (20,50))
                        source_textinput=TextInput(text = '', font_size=15, width=100, height=30, multiline = False, pos=(100,90))
                        width_text = Label(text = '[b]width:[/b]', markup = True, font_size = 15, pos = (20,20))
                        width_textinput = TextInput(text = '50', font_size = 15, width = 100, height = 30, multiline = False, pos = (100,50))
                        height_text = Label(text = '[b]height:[/b]', markup = True, font_size = 15, pos = (200,50))
                        height_textinput = TextInput(text = '50', font_size = 15, width = 100, height = 30, multiline = False, pos = (280,90)) 
                        pos_text = Label(text='[b]pos:[/b]',markup = True, font_size=15, pos = (200,20))
                        pos_textinput=TextInput(text = '0,0', font_size=15, width=100, height=30, multiline = False, pos=(280,50))
                        put_widget = Button(text='add widget', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,80))
                        put_widget.bind(on_press = set_videoplayer)
                        close_properties = Button(text='close properties', markup = True, font_size = 15, width=120, height=30, background_color=(0,0,0.2,0), pos=(470,40))
                        close_properties.bind(on_press= close_videoplayer_properties)
                        win_p.add_widget(source_text)
                        win_p.add_widget(source_textinput)
                        win_p.add_widget(width_text)
                        win_p.add_widget(width_textinput)
                        win_p.add_widget(height_text)
                        win_p.add_widget(height_textinput)
                        win_p.add_widget(pos_text)
                        win_p.add_widget(pos_textinput)
                        win_p.add_widget(videoplayer_title)
                        win_p.add_widget(close_properties)
                        win_p.add_widget(put_widget)
                if load_project_flag[len(load_project_flag)-1] == 'none' and code_panel_flag[len(code_panel_flag)-1] == 'none' and save_project_flag[len(save_project_flag)-1] == 'none' and user_interface_flag[len(user_interface_flag)-1] == 'none':
                    user_interface_flag.append('true')
                    label = Button(text='Label',font_size = 15, width = 100, height = 25, pos = (260,310), background_color=(2,1,1,1))
                    label.bind(on_press = label_properties)
                    button = Button(text='Button',font_size = 15, width = 100, height = 25, pos = (370,310), background_color=(2,1,1,1))
                    button.bind(on_press = button_properties)
                    textinput = Button(text='TextInput',font_size = 15, width = 100, height = 25, pos = (480,310), background_color=(2,1,1,1))
                    textinput.bind(on_press = textinput_properties)
                    checkbox = Button(text='CheckBox',font_size = 15, width = 100, height = 25, pos = (260,280), background_color=(2,1,1,1))
                    checkbox.bind(on_press=checkbox_properties)
                    togglebutton = Button(text='ToggleButton',font_size = 15, width = 100, height = 25, pos = (370,280), background_color=(2,1,1,1))
                    togglebutton.bind(on_press = togglebutton_properties)
                    image = Button(text='Image',font_size = 15, width = 100, height = 25, pos = (480,280), background_color=(2,1,1,1))
                    image.bind(on_press = image_properties)
                    filechooser = Button(text='FileChooser',font_size = 15, width = 100, height = 25, pos = (260,250), background_color=(2,1,1,1))
                    filechooser.bind(on_press = filechooser_properties)
                    spinner = Button(text='Spinner',font_size = 15, width = 100, height = 25, pos = (370,250), background_color=(2,1,1,1))
                    spinner.bind(on_press = spinner_properties)
                    slider = Button(text='Slider',font_size = 15, width = 100, height = 25, pos = (480,250), background_color=(2,1,1,1))
                    slider.bind(on_press = slider_properties)
                    progressbar = Button(text='ProgressBar',font_size = 15, width = 100, height = 25, pos = (260,220), background_color=(2,1,1,1))
                    progressbar.bind(on_press = progressbar_properties)
                    switch = Button(text='Switch',font_size = 15, width = 100, height = 25, pos = (370,220), background_color=(2,1,1,1))
                    switch.bind(on_press = switch_properties)
                    videoplayer = Button(text='VideoPlayer',font_size = 15, width = 100, height = 25, pos = (480,220), background_color=(2,1,1,1))
                    videoplayer.bind(on_press = videoplayer_properties)
                    close_panel = Button(text='close', font_size = 15, width = 100, height = 25, pos = (260,180), background_color = (0,0,0.2,0))
                    close_panel.bind(on_press = close_interface)
                    #view_smartphone()
                    win_c.add_widget(label)
                    win_c.add_widget(button)
                    win_c.add_widget(textinput)
                    win_c.add_widget(checkbox)
                    win_c.add_widget(togglebutton)
                    win_c.add_widget(image)
                    win_c.add_widget(filechooser)
                    win_c.add_widget(spinner)
                    win_c.add_widget(slider)
                    win_c.add_widget(progressbar)
                    win_c.add_widget(switch)
                    win_c.add_widget(videoplayer)
                    win_c.add_widget(close_panel)
#########################
###VIEW SOURCE CODE
#########################
            def view_code(code):
                if code_panel_flag[len(code_panel_flag)-1] == 'none' and user_interface_flag[len(user_interface_flag)-1] == 'none' and save_project_flag[len(save_project_flag)-1] == 'none':
                    def save_code(close_panel):
                        code_panel_flag.append('none')
                        del(source_code[0:len(source_code)])
                        source_code.append(code_frame.text)
                        win_c.clear_widgets()
                    def code_frame_edit(code_frame):
                        code_frame.readonly = False
                    def slider_change(sld, value):
                        if sld.value < 500:
                            code_frame.readonly = False
                            code_frame.text = ''
                            code_frame.insert_text (content)
                            code_frame.scroll_y = 500 - sld.value 
                            code_frame.readonly = True
                    code_frame = TextInput(text= '',width = 320, height = 270, font_size = 15, background_color = (0,0,0.2,0), foreground_color=(1,1,1,1), multiline = False, pos = (260,70))                   
                    code_frame.readonly = True
                    code_frame.bind(on_double_tap = code_frame_edit)
                    if len(kivy_code) >= 0 and len(file_name) >= 1:
                        content_code = []
                        pos = 0
                        infile = open(file_name[len(file_name)-1], 'r')
                        content_file = infile.readlines()
                        for i in range (0,len(content_file),1):
                            if content_file[i].count('class MyApp') == 1:
                                pos = i
                        for i in range (0,pos,1):
                            content_code.append(content_file[i])
                        if widget_added.count('label') >= 1:
                            content_code.append('from kivy.uix.label import Label\n')
                        if widget_added.count('button') >= 1:
                            content_code.append('from kivy.uix.button import Button\n')
                        if widget_added.count('textinput') >= 1:
                            content_code.append('from kivy.uix.textinput import TextInput\n')
                        if widget_added.count('checkbox') >= 1:
                            content_code.append('from kivy.uix.checkbox import CheckBox\n')
                        if widget_added.count('togglebutton') >= 1:
                            content_code.append('from kivy.uix.togglebutton import ToggleButton\n')
                        if widget_added.count('image') >= 1:
                            content_code.append('from kivy.uix.image import Image\n')
                        if widget_added.count('filechooser') >= 1:
                            content_code.append('from kivy.uix.filechooser import FileChooserListView,FileChooserIconView\n')
                        if widget_added.count('spinner') >= 1:
                            content_code.append('from kivy.uix.spinner import Spinner\n')
                        if widget_added.count('slider') >= 1:
                            content_code.append('from kivy.uix.slider import Slider\n')
                        if widget_added.count('progressbar') >= 1:
                            content_code.append('from kivy.uix.progressbar import ProgressBar\n')
                        if widget_added.count('switch') >= 1:
                            content_code.append('from kivy.uix.switch import Switch\n')
                        if widget_added.count('videoplayer') >= 1:
                            content_code.append('from kivy.uix.videoplayer import VideoPlayer\n')
                        content_code.append('class MyApp(App):\n')
                        content_code.append('\tdef build(self):\n')
                        content_code.append('\t\twin = Widget()\n')
                        for j in range(0,len(kivy_code),1):
                            content_code.append('\t\t' + kivy_code[j] + '\n')
                        if widget_added.count('label') >= 1:
                            content_code.append('\t\twin.add_widget(lbl)\n')
                        if widget_added.count('button') >= 1:
                            content_code.append('\t\twin.add_widget(btn)\n')
                        if widget_added.count('textinput') >= 1:
                            content_code.append('\t\twin.add_widget(txti)\n')
                        if widget_added.count('checkbox') >= 1:
                            content_code.append('\t\twin.add_widget(chkb)\n')
                        if widget_added.count('togglebutton') >= 1:
                            content_code.append('\t\twin.add_widget(btn)\n')
                        if widget_added.count('image') >= 1:
                            content_code.append('\t\twin.add_widget(img)\n')
                        if widget_added.count('filechooser') >= 1:
                            content_code.append('\t\twin.add_widget(fc)\n')
                        if widget_added.count('spinner') >= 1:
                            content_code.append('\t\twin.add_widget(sp)\n')
                        if widget_added.count('slider') >= 1:
                            content_code.append('\t\twin.add_widget(sl)\n')
                        if widget_added.count('progressbar') >= 1:
                            content_code.append('\t\twin.add_widget(pb)\n')
                        if widget_added.count('switch') >= 1:
                            content_code.append('\t\twin.add_widget(sw)\n')
                        if widget_added.count('videoplayer') >= 1:
                            content_code.append('\t\twin.add_widget(vp)\n')
                        for k in range (pos + 3,len(content_file),1):
                            content_code.append(content_file[k])
                        content = ''.join(content_code)
                        code_frame.text = content
                    code_frame.scroll_y = 0
                    code_panel_flag.append('true')
                    close_panel = Button(text='close', markup = True, font_size = 15, width = 100, height = 25, pos = (500,10), background_color = (0,0,0.2,0))
                    close_panel.bind(on_press = save_code)
                    win_c.add_widget(code_frame)
                    win_c.add_widget(close_panel)
                    if len(file_name) > 1 or len(kivy_code) > 0:
                        sld = Slider(height = 270, min=0, max=500, value=500, orientation='vertical', step=1, pos = (535,70) )
                        sld.bind(value=slider_change)
                        win_c.add_widget(sld)
            if load_project_flag[len(load_project_flag)-1] == 'none' and load_example_flag[len(load_example_flag)-1] == 'none' and help_flag[len(help_flag)-1] == 'none':
                new_project_flag.append('true')
                gui = Button (text = 'Interface', markup = True, font_size = 18, width = 100, height = 30, pos = (260,350))
                gui.bind(on_press=interface)
                code = Button (text = 'View Code', markup = True, font_size = 18, width = 100, height = 30, pos = (370,350))
                code.bind(on_press = view_code)
                save = Button (text = 'Save',markup = True, font_size = 18, width = 100, height = 30, pos = (480,350))
                save.bind(on_press = save_project)
                win_h.add_widget(save)
                win_h.add_widget(code)
                win_h.add_widget(gui)
#########################
###LOAD SAVED PROJECT
#########################
        def load_saved_project(load_project):
            def quit_browse():
                load_project_flag.append('none')
                win_c.clear_widgets()
            def get_project(get_path):
                if len(file_textinput.text) > 0:
                    file_name.append(fc.path + '/' + file_textinput.text)
                    quit_browse()
                    open_project()
                if len(file_textinput.text) == 0:
                    def quit_warning(btn):
                        win_c.remove_widget(pop)
                    btn = Button (text='file name empty', font_size = 16)
                    btn.bind(on_press = quit_warning)
                    pop = Popup (title='Warning', content=btn, size=(200,200), pos=(300,200))
                    win_c.add_widget(pop)
            def close_filechooser(close_fc):
                quit_browse()
            def file_selection(fc,selection):
                file_path = str(fc.selection)
                inver_path = file_path[::-1]
                touse = inver_path.strip().split('/')
                touse = touse[0].replace(']','') 
                touse = touse.replace("'",'')
                touse = touse[::-1]
                file_textinput.scroll_y = 0
                file_textinput.text = ''
                file_textinput.insert_text(touse)
            if load_project_flag[len(load_project_flag)-1] == 'none' and new_project_flag[len(new_project_flag)-1] == 'none' and load_example_flag[len(load_example_flag)-1] == 'none' and help_flag[len(help_flag)-1] == 'none':
                win_h.clear_widgets()
                load_project_flag.append('true')
                edit_project_flag.append('true')
                file_label = Label(text = '[b]File name:[/b]', markup = True, font_size = 18, multiline = False, pos = (250,310))
                file_textinput = TextInput(text = '', font_size = 15, width = 200, height = 30, multiline = False, pos = (350, 345))
                fc = FileChooserListView(path = 'projects',size = (320,140), pos = (250,180))
                fc.bind(selection = file_selection)
                get_path = Button(text='open', markup = True, font_size = 15, width = 100, height = 25, pos = (230,125), background_color=(0,0,0.2,0))
                get_path.bind(on_press = get_project)
                close_fc = Button(text='close', markup = True, font_size = 15, width = 100, height = 25, pos = (500,125), background_color = (0,0,0.2,0))
                close_fc.bind(on_press = close_filechooser)
                win_c.add_widget(fc)
                win_c.add_widget(get_path)
                win_c.add_widget(close_fc)
                win_c.add_widget(file_label)
                win_c.add_widget(file_textinput)
                
##########################
###LOAD EXAMPLES
##########################
        def examples(load_examples):
            def show_code():
                def slider_change(sld, value):
                    if sld.value < 500:
                        code_frame.readonly = False
                        code_frame.text = ''
                        code_frame.insert_text (content)
                        code_frame.scroll_y = 500 - sld.value    
                        code_frame.readonly = True
                if example_flag[len(example_flag)-1] == 'ex1':
                    infile = open('code/label.py','r')
                if example_flag[len(example_flag)-1] == 'ex2':
                    infile = open('code/images.py','r')
                if example_flag[len(example_flag)-1] == 'ex3':
                    infile = open('code/widgets.py','r')
                if example_flag[len(example_flag)-1] == 'ex4':
                    infile = open('code/editor.py','r')
                if example_flag[len(example_flag)-1] == 'ex5':
                    infile = open('code/video.py','r')
                if example_flag[len(example_flag)-1] == 'ex6':
                    infile = open('code/filechooser.py','r')    
                content = infile.readlines()
                content = ''.join(content)
                code_frame.text = content
                code_frame.readonly = True
                code_frame.scroll_y = 0
                sld = Slider(height = 280, min=0, max=500, value=500, orientation='vertical', step=1, pos = (535,30) )
                sld.bind(value=slider_change)
                win_c.add_widget(sld)
            def example1(ex1):
                if example_flag[len(example_flag)-1] == 'none':
                    example_flag.append('ex1')
                    file_name.append('code/label.py')
                    win_r.clear_widgets()
                    open_project()
                    show_code()
            def example2(ex2):
                if example_flag[len(example_flag)-1] == 'none':
                    example_flag.append('ex2')
                    file_name.append('code/images.py')
                    win_r.clear_widgets()
                    open_project()
                    show_code()
            def example3(ex3):
                if example_flag[len(example_flag)-1] == 'none':
                    example_flag.append('ex3')
                    file_name.append('code/widgets.py')
                    win_r.clear_widgets()
                    open_project()
                    show_code()
            def example4(ex4):
                if example_flag[len(example_flag)-1] == 'none':
                    example_flag.append('ex4')
                    file_name.append('code/editor.py')
                    win_r.clear_widgets()
                    open_project()
                    show_code()
            def example5(ex5):
                if example_flag[len(example_flag)-1] == 'none':
                    example_flag.append('ex5')
                    file_name.append('code/video.py')
                    win_r.clear_widgets()
                    open_project()
                    show_code()
            def example6(ex6):
                if example_flag[len(example_flag)-1] == 'none':
                    example_flag.append('ex6')
                    file_name.append('code/filechooser.py')
                    win_r.clear_widgets()
                    open_project()
                    show_code()
            def quit_examples(close_examples):
                load_example_flag.append('none')
                example_flag.append('none')
                file_name.append('code/MyApp.py')
                win_c.clear_widgets()
                win_r.clear_widgets()
            if new_project_flag[len(new_project_flag)-1] == 'none' and load_project_flag[len(load_project_flag)-1] == 'none' and help_flag[len(help_flag)-1] == 'none':
                def code_frame_edit(code_frame):
                    code_frame.readonly = False
                win_h.clear_widgets()
                load_example_flag.append('True')
                ex1 = Button (text = 'Labels', markup = True, font_size = 15, width = 100, height = 25, pos = (260,350))
                ex1.bind(on_press = example1)
                ex2 = Button (text = 'Images',markup = True, font_size = 15, width = 100, height = 25, pos = (370,350))
                ex2.bind(on_press = example2)
                ex3 = Button (text = 'Widgets',markup = True, font_size = 15, width = 100, height = 25, pos = (480,350))
                ex3.bind(on_press = example3)
                ex4 = Button (text = 'Editor', markup = True, font_size = 15, width = 100, height = 25, pos = (260,320))
                ex4.bind(on_press = example4)
                ex5 = Button (text = 'Video', markup = True, font_size = 15, width = 100, height = 25, pos = (370,320))
                ex5.bind(on_press = example5)
                ex6 = Button (text = 'FileChooser', markup = True, font_size = 15, width = 100, height = 25, pos = (480,320))
                ex6.bind(on_press = example6)
                code_label = Label(text = 'Source code', font_size = 20, pos=(360,250))
                code_frame = TextInput(width = 320, height = 250, font_size = 15, background_color = (0,0,0.2,0), foreground_color = (1,1,1,1), multiline = False, pos = (260,40))
                code_frame.bind(on_double_tap = code_frame_edit)
                close_panel = Button(text='close', markup = True, font_size = 15, width = 80, height = 25, pos = (520,10), background_color = (0,0,0.2,0))
                close_panel.bind(on_press = quit_examples)
                win_c.add_widget(ex1)
                win_c.add_widget(ex2)
                win_c.add_widget(ex3)
                win_c.add_widget(ex4)
                win_c.add_widget(ex5)
                win_c.add_widget(ex6)
                win_c.add_widget(code_label)
                win_c.add_widget(code_frame)
                win_c.add_widget(close_panel)
#########################
###HELP
#########################
        def help_doc(help):
            def slider_change(sld, value):
                 if sld.value < 2200:
                     help_textinput.readonly = False
                     help_textinput.text = ''
                     help_textinput.insert_text (content)
                     help_textinput.scroll_y = 2200 - sld.value
                     help_textinput.readonly = True
            def quit_help(close_label):
                help_flag.append('none')
                win_c.clear_widgets()
            def get_kivy_manual(get_doc):
                import webbrowser
                url = 'https://github.com/btcpar/contest/blob/master/docs/kivy_lite.doc'
                webbrowser.open(url)
            if help_flag[len(help_flag)-1] == 'none' and new_project_flag[len(new_project_flag)-1] == 'none' and load_example_flag[len(load_example_flag)-1] == 'none' and load_project_flag[len(load_project_flag)-1] == 'none':
                win_h.clear_widgets()
                help_flag.append('true')
                infile = open('docs/intro.txt','r')
                content = infile.readlines()
                content = ''.join(content)
                help_label = Label(text = 'Kivy lite guide', font_size = 20, pos=(360,330))
                help_textinput = TextInput(width=320, height=300, font_size = 15, readonly = True, background_color = (0,0,0.2,0), foreground_color = (1,1,1,1), pos=(260,60))
                help_textinput.text = content
                help_textinput.scroll_y = 0
                sld = Slider(height = 300, min=0, max=2200, value=2200, orientation='vertical', step=1, pos = (535,50) )
                sld.bind(value=slider_change)
                get_doc = Button(text='[b]get manual[/b]', markup = True, font_size = 15, width = 80, height =25, pos = (260, 10), background_color = (0,0,0.2,0))
                get_doc.bind(on_press = get_kivy_manual)
                close_label = Button(text='close', markup = True, font_size = 15, width = 80, height = 25, pos = (520, 10), background_color = (0,0,0.2,0)) 
                close_label.bind(on_press = quit_help)
                win_c.add_widget(help_label)
                win_c.add_widget(help_textinput)
                win_c.add_widget(sld)
                win_c.add_widget(get_doc)
                win_c.add_widget(close_label)
#########################
###ABOUT KIVY LITE
#########################
        def about_kivy(about):
            if about_flag[len(about_flag)-1] == 'none':
                about_flag.append('true')
                def quit_about(inf):
                    win_c.remove_widget(popup)
                    about_flag.append('none')
                inf = Button (text='Visual kivy (lite) 1.0.1\n\n[b]Developer[/b]: Joaquin Panadero\n[b]Contact[/b]: btcpar@gmail.com', markup = True, font_size = 16)
                inf.bind(on_press = quit_about)
                popup = Popup(title='About Visual kivy (lite)', content = inf, size = (350,300), pos = (250,100))
                win_c.add_widget(popup)
##########################
###FIRST INTERFACE
##########################
        win = Widget()    #Main
        win_h = Widget()  #Widget header
        win_c = Widget()  #Widget center
        win_r = Widget()  #Widget right
        win_p = Widget()  #widget properties
        win_undo = Widget()
        f = FloatLayout() 
        s = Scatter(do_collide_after_children = True)     #Main scatter
        sr = Scatter(do_collide_after_children = True)
        logo = Image (source='logo.jpg', size = (80,80), pos = (40,100))
        anim = Animation (x=40,y=410,t='in_quad')
        anim.start(logo)
        app_title = Label(text='Visual kivy (lite)',font_size = 40, pos = (190, 380))
        with win.canvas:
            Color(0,0,0.2)
            Rectangle(pos=(0,0),size=(620,420))
        clear_button = Button(text='[b]clear[/b]', markup = True, width = 70, height = 25, background_color = (1.5,1,0.5,0), font_size = 16, pos = (720, 415))
        clear_button.bind(on_press = clear_app)
        start_project = Button(text='New/Edit', font_size = 25, width = 200, height = 40, pos = (50,350), background_color = (0.5,0.5,1,1))
        start_project.bind(on_press = create_project)
        load_project = Button(text='Load project', font_size = 25, width = 200, height = 40, pos = (50,300),background_color=(0.5,0.5,1,1))
        load_project.bind(on_press=load_saved_project)
        load_examples = Button(text='Examples', font_size = 25, width = 200, height = 40, pos = (50,250), background_color = (0.5,0.5,1,1))
        load_examples.bind(on_press = examples)
        help = Button(text='Help', font_size = 25, width = 200, height = 40, pos = (50,200), background_color= (0.5,0.5,1,1))
        help.bind(on_press = help_doc)
        about = Button(text='About', font_size = 25, width = 200, height = 40, pos = (50,150), background_color = (0.5,0.5,1,1))
        about.bind(on_press = about_kivy)
        smartphone_img = Image(source='smartphone.png', size = (300, 450), pos = (605,0))
        win.add_widget(smartphone_img)
        win.add_widget(win_h)
        win.add_widget(win_c)
        win.add_widget(win_r)
        win.add_widget(win_p)
        win.add_widget(win_undo)
        win.add_widget(logo)
        win.add_widget(app_title)
        win.add_widget(clear_button)
        win.add_widget(start_project)
        win.add_widget(load_project)
        win.add_widget(load_examples)
        win.add_widget(help)
        win.add_widget(about)
        s.add_widget(win)
        f.add_widget(s)
        return f
if __name__ == '__main__':
    KivyLite().run()
