#!/usr/bin/env python
import pygtk,gtk
import imdb
sre=None
ap=imdb.IMDb()
def fdata(widget):
        x=int(entrym.get_text())
        entry.set_text('')
        buffer1.delete(buffer1.get_iter_at_offset(-1),buffer1.get_iter_at_offset(0))
        selmov=sre[x-1]
        print selmov.movieID,selmov['title']
        ap.update(selmov)
        sum=selmov.summary()
        sum=sum+selmov.get('plot outline')
        iter=buffer1.get_iter_at_offset(-1)
        buffer1.insert(iter,sum)
        
          

#Backend code
def back(widget):
        mvname=entry.get_text()
        entry.set_text("")
        buffer1.delete(buffer1.get_iter_at_offset(-1),buffer1.get_iter_at_offset(0))
        sresult=ap.search_movie(mvname)
        global sre
        sre=sresult
        print type(sresult),type(sre)
        mvlist=''
        no=0
        for i in sresult:
                no=no+1
                mvlist=mvlist+'\n'+str(no)+') '+i['title']+'\n'
        iter=buffer1.get_iter_at_offset(-1)
        buffer1.insert(iter,mvlist)
        

#GUI code

win=gtk.Window()
win.set_size_request(350,420)
win.set_resizable(False)
win.set_position(gtk.WIN_POS_CENTER_ALWAYS)
win.set_title("ImdbPy")

vbox=gtk.VBox()
vbox.set_border_width(10)
vbox.set_spacing(5)
label=gtk.Label()
label.set_markup("Search:")
entry=gtk.Entry()
button=gtk.Button("Go")
button.connect("clicked",back)
    
hbox=gtk.HBox()
hbox.set_spacing(5)
hbox.pack_start(label)
hbox.pack_start(entry)
hbox.pack_start(button)
vbox.add(hbox)


sw = gtk.ScrolledWindow()
sw.set_policy(gtk.POLICY_ALWAYS, gtk.POLICY_ALWAYS)
textview = gtk.TextView()
textview.set_editable(False)
textview.set_cursor_visible(False)
buffer1=textview.get_buffer()
sw.add(textview)
sw.show()
textview.show()
sw.set_size_request(200,270)
vbox.pack_start(sw)

hboxs=gtk.HBox()
label2=gtk.Label("Select movie:")
entrym=gtk.Entry()
hboxs.pack_start(label2)
hboxs.pack_start(entrym)
vbox.pack_start(hboxs)

separator = gtk.HSeparator()
vbox.pack_start(separator, False, False,0) 


fbutton=gtk.Button("Fetch data...")
fbutton.connect("clicked",fdata)
vbox.pack_start(fbutton)

win.add(vbox)

win.connect("destroy",lambda wid:gtk.main_quit())
win.show_all()
gtk.main()




