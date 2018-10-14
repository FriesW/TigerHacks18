from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

from time import sleep

import recv
import send
from api import api

class ListView(Frame):
    def __init__(self, screen):
        super(ListView, self).__init__(screen,
                                       screen.height * 2 // 3,
                                       screen.width * 2 // 3,
                                       on_load=self._reload_list,
                                       hover_focus=True,
                                       title="Inbox")
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            recv.build_option(IMAP_EP, USER, PASS),
            name="emails",
            on_change=self._on_pick)
        self._view_button = Button("View", self._view)
        self._delete_button = Button("Delete", self._delete)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Label(recv.get_header()))
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Refresh", self._update_cb), 0)
        layout2.add_widget(self._view_button, 2)
        layout2.add_widget(self._delete_button, 3)
        layout2.add_widget(Button("Compose", self._compose), 1)
        layout2.add_widget(Button("Quit", self._quit), 4)
        self.fix()
        self._on_pick()

    def _on_pick(self):
        self._view_button.disabled = self._list_view.value is None
        self._delete_button.disabled = self._list_view.value is None

    def _update_cb(self):
        self._list_view.options = recv.build_option(IMAP_EP, USER, PASS)
    
    def _reload_list(self, new_value=None):
        self._list_view.value = new_value

    def _compose(self):
        raise NextScene("Compose Email")

    def _view(self):
        pass
        #self.save()
        #raise NextScene("Edit Contact")

    def _delete(self):
        pass
        #self.save()
        #self._reload_list()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


class ContactView(Frame):
    def __init__(self, screen):
        super(ContactView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          title="Compose",
                                          reduce_cpu=True)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._pow_txt = Text("Proof:", "pow")
        self._pow_txt.value = ''
        layout.add_widget(Text("To:", "recip",on_blur=self._api))
        layout.add_widget(Text("Subject:", "subject"))
        layout.add_widget(self._pow_txt)
        layout.add_widget(TextBox(
            Widget.FILL_FRAME, "Body:", "body", as_string=True, line_wrap=True))
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Send", self._send), 0)
        layout2.add_widget(Button("Cancel", self._cancel), 3)
        self.fix()

    #def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        #super(ContactView, self).reset()

    def _api(self):
        self.save()
        if 'recip' not in self.data:
            return
        res = api.get(USER,self.data['recip'])
        if res != None:
            self._pow_txt.value = str(res)
        
    def _send(self):
        self.save()
        pow = self.data['pow']
        if not pow.isdigit():
            pow = None
        else:
            pow = int(pow)
        send.sendemail(USER, self.data['recip'], '',
            self.data['subject'], self.data['body'], pow,
            SMTP_EP, USER, PASS)
        raise NextScene("Main")

    @staticmethod
    def _cancel():
        raise NextScene("Main")


def demo(screen, scene):
    scenes = [
        Scene([ListView(screen)], -1, name="Main"),
        Scene([ContactView(screen)], -1, name="Compose Email")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene)

SMTP_EP = None
IMAP_EP = None
USER = None
PASS = None

if __name__ == '__main__':
    conf = sys.argv[1]
    with open(conf, 'r') as f:
        SMTP_EP = f.readline().strip()
        IMAP_EP = f.readline().strip()
        USER = f.readline().strip()
        PASS = f.readline().strip()
    
    print(SMTP_EP, '\t', IMAP_EP, '\t', USER)
    sleep(5)
        
    last_scene = None
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
