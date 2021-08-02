'''import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

# Replace this with your
# current version


class MyApp(App):
    def build(self):
        video_player = VideoPlayer(source="video_1.mp4")
        video_player.state = "play"
        video_player.options = {'eos': 'loop'}
        video_player.allow_stretch = True
        return video_player


if __name__ == "__main__":
    MyApp().run()
'''

import os
import kivy
import random

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout


kivy.require('2.0.0')


class MyApp(App):
    '''def build4(self):
        def a(instance,value):
            print("Test widget button!")
        btn = Button(text="Botão",font_size=150)
        btn.bind(state=a)
        return btn'''

    def __init__(self):
        super().__init__()
        self.videos = [f'\\\desktop-vsfup0f/Webcam/{video}' for video in os.listdir('\\\desktop-vsfup0f/Webcam/') if
                       not os.path.isdir(f'\\\desktop-vsfup0f/Webcam/{video}')] + \
                      [f'\\\desktop-vsfup0f/webcam2/{video2}' for video2 in os.listdir('\\\desktop-vsfup0f/webcam2/') if
                       not os.path.isdir(f'\\\desktop-vsfup0f/webcam2/{video2}')] + \
                      [f'\\\desktop-vsfup0f/Webcam3/{video3}' for video3 in os.listdir('\\\desktop-vsfup0f/Webcam3/') if
                       not os.path.isdir(f'\\\desktop-vsfup0f/Webcam3/{video3}')]
        self.videos.sort()
        self.title = "Video Player"
        self.video_player = VideoPlayer(size_hint=(1, .75))

        self.video_random_selected = self.videos[0]
        self.video_random_ordered = ''

        self.video_player.source = self.video_random_selected
        self.video_player.state = "play"
        self.video_player.allow_stretch = True
        self.video_player.allow_fullscreen = False

        self.label_title = Label(text=self.video_random_selected)

        self.random_state = False

    def sort_list(self):
        lista = []
        for _ in range(len(self.videos)):
            video = random.choice(self.videos)
            while video in lista:
                video = random.choice(self.videos)
            lista.append(video)
        return lista

    def build(self):

        def next_video(*args):
            if args[1] == "down":
                if self.random_state:
                    video_index = 0
                    for index, value in enumerate(self.video_random_ordered):
                        if value == self.video_random_selected:
                            video_index = index
                            break

                    video_index = -1 if video_index >= len(self.videos) - 1 else video_index
                    video_atual = self.video_random_ordered[video_index + 1]
                    self.video_random_selected = video_atual
                    self.label_title.text = video_atual
                    self.video_player.source = video_atual
                    self.video_player.state = "play"
                else:
                    video_index = 0
                    for index, value in enumerate(self.videos):
                        if value == self.video_random_selected:
                            video_index = index
                            break

                    video_index = -1 if video_index >= len(self.videos) - 1 else video_index
                    video_atual = self.videos[video_index + 1]
                    self.video_random_selected = video_atual
                    self.label_title.text = video_atual
                    self.video_player.source = video_atual
                    self.video_player.state = "play"

        def prev_video(*args):
            if args[1] == "down":
                if self.random_state:
                    video_index = 0
                    for index, value in enumerate(self.video_random_ordered):
                        if value == self.video_random_selected:
                            video_index = index
                            break
                    print(video_index)
                    video_atual = self.video_random_ordered[video_index - 1]
                    self.video_random_selected = video_atual
                    self.label_title.text = video_atual
                    self.video_player.source = video_atual
                    self.video_player.state = "play"

                else:
                    video_index = 0
                    for index, value in enumerate(self.videos):
                        if value == self.video_random_selected:
                            video_index = index
                            break

                    video_atual = self.videos[video_index - 1]
                    self.video_random_selected = video_atual
                    self.label_title.text = video_atual
                    self.video_player.source = video_atual
                    self.video_player.state = "play"

        def turn_random(*args):
            self.video_random_ordered = self.sort_list()
            self.random_state = not self.random_state


        def delete_file(*args):
            if args[1] == 'down':
                if os.path.exists(self.video_random_selected):
                    # arquivo existe, hora de deletar

                    def cancel_popup(*inf):
                        if inf[1] == 'down':
                            layout.remove_widget(alert_layout)

                    def delete_popup(*inf):
                        if inf[1] == 'down':
                            try:
                                novo_video = random.choice(self.videos)
                                self.label_title.text = novo_video
                                self.video_player.source = novo_video
                                self.video_player.state = "play"
                                self.videos.remove(self.video_random_selected)
                                self.video_random_ordered = self.sort_list()
                                os.remove(self.video_random_selected)
                                self.video_random_selected = novo_video
                            except Exception as e:
                                raise RuntimeError(e)
                            layout.remove_widget(alert_layout)

                    alert_layout = ScatterLayout()
                    label_box = Label(text="Deseja deletar ?", size_hint=(None, None), width=50, height=25)
                    confirm_box = Button(text="Deletar", size_hint=(None, None), width=60, height=35)
                    cancel_box = Button(text="Não", size_hint=(None, None), width=60, height=35)

                    cancel_box.bind(state=cancel_popup)
                    confirm_box.bind(state=delete_popup)

                    label_box.pos = (Window.width / 2, Window.height / 2)
                    cancel_box.pos = (Window.width / 2 - cancel_box.width, Window.height / 2 - 30)
                    confirm_box.pos = (Window.width / 2 + confirm_box.width, Window.height / 2 - 30)

                    alert_layout.add_widget(label_box)
                    alert_layout.add_widget(confirm_box)
                    alert_layout.add_widget(cancel_box)
                    layout.add_widget(alert_layout)
                else:
                    print("The file does not exist")

        # pra fazer o random ir e voltar, criar array antes de exexutar com 300 videos e percorree aw funcoes nele
        layout = AnchorLayout(anchor_x='center',anchor_y='bottom')
        layout_video = AnchorLayout(anchor_x='center',anchor_y='top')
        layout_left = AnchorLayout(anchor_x='left',anchor_y='bottom')
        layout_right = AnchorLayout(anchor_x='right',anchor_y='bottom')
        layout.add_widget(layout_video)
        layout.add_widget(layout_left)
        layout.add_widget(layout_right)

        btn_prev = Button(text="prev", size_hint=(.15, .15))
        btn_prev.pos = (0, 10)
        btn_prev.bind(state=prev_video)

        btn_next = Button(text="next", size_hint=(.15, .15))
        btn_next.pos = ((Window.width - (btn_next.width * 1.2)), 10)
        btn_next.bind(state=next_video)

        btn_random = ToggleButton(text="RN", size_hint=(None, None), width=40, height=25)
        btn_random.pos = ((Window.width / 2) - btn_random.width, 10)
        btn_random.bind(state=turn_random)

        btn_delete = Button(text="Del", size_hint=(None, None), width=40, height=25)
        btn_delete.pos = ((Window.width / 2) + btn_delete.width, 10)
        btn_delete.bind(state=delete_file)

        self.video_player.pos = (0, 100)
        self.label_title.pos = (0, 270)

        layout_video.add_widget(self.video_player)
        layout_right.add_widget(btn_next)
        layout_left.add_widget(btn_prev)
        layout_left.add_widget(btn_random)
        layout_right.add_widget(btn_delete)
        layout.add_widget(self.label_title)
        return layout


if __name__ == "__main__":
    MyApp().run()
