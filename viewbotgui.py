#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.1
#  in conjunction with Tcl version 8.6
#    Feb 01, 2022 04:38:24 PM JST  platform: Windows NT
import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import urllib
import viewbotgui_support
import shutil
import asyncio
import nest_asyncio
nest_asyncio.apply()
bot=None
class Toplevel1:
    TFrame2=None
    vcch=None
    textch=None
    TFrame3=None
    TFrame4=None
    hist=None
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1272x450+653+653")
        top.minsize(120, 1)
        top.maxsize(2564, 1421)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.0, rely=0.0, relheight=0.989, relwidth=0.067)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")
        self.canvas1 = tk.Canvas(self.TFrame1)
        self.scrollbar1 = ttk.Scrollbar(self.TFrame1, orient="vertical", command=self.canvas1.yview)
        self.scrollable_frame1 = ttk.Frame(self.canvas1)
        self.scrollable_frame1.bind(
            "<Configure>",
            lambda e: self.canvas1.configure(
                scrollregion=self.canvas1.bbox("all")
            )
        )
        Toplevel1.viewserverlist(self.scrollable_frame1)
        self.canvas1.create_window((0, 0), window=self.scrollable_frame1, anchor="nw")
        self.canvas1.configure(yscrollcommand=self.scrollbar1.set)
        self.canvas1.pack(side="left", fill="both", expand=True)
        self.scrollbar1.pack(side="right", fill="y")
        self.scrollable_frame1.pack()
        self.TFrame2 = ttk.Frame(self.top)
        self.TFrame2.place(relx=0.071, rely=0.0, relheight=0.989, relwidth=0.925)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")
    def viewserverlist(frame):
        Toplevel1.guilds=bot.guilds
        if os.path.exists("guildicon"):
            shutil.rmtree("guildicon")
        os.mkdir("guildicon")
        for i in range(len(Toplevel1.guilds)):
            try:
                urllib.request.urlretrieve(Toplevel1.guilds[i].icon.url,"./guildicon/"+str(Toplevel1.guilds[i].id)+'.png')
            except:
                shutil.copyfile("discord.png","guildicon/"+str(Toplevel1.guilds[i].id)+'.png')
            img = tk.PhotoImage(file="guildicon/"+str(Toplevel1.guilds[i].id)+'.png')
            bt=ttk.Button(frame,image=img)
            eval("bt.configure(command=lambda:Toplevel1.viewserver(Toplevel1.guilds["+str(i)+"]))")
            bt.configure(compound='top')
            bt.configure(text=Toplevel1.guilds[i].name)
            bt.pack()
    def viewch(channel):
        asyncio.run(Toplevel1.viewchasync(channel))
    async def viewchasync(channel):
        Toplevel1.hist=await channel.history(limit=550).flatten()
        Toplevel1.hist.reverse()
        if Toplevel1.TFrame4!=None:
            Toplevel1.TFrame4.destroy()
        Toplevel1.TFrame4 = ttk.Frame(Toplevel1.TFrame2)
        Toplevel1.TFrame4.configure(relief='groove')
        Toplevel1.TFrame4.configure(borderwidth="2")
        Toplevel1.TFrame4.configure(relief="groove")
        Toplevel1.TFrame4.place(relx=0.371, rely=0.0, relheight=0.989, relwidth=0.629)
        Toplevel1.canvas3 = tk.Canvas(Toplevel1.TFrame4)
        Toplevel1.scrollbar3 = ttk.Scrollbar(Toplevel1.TFrame4, orient="vertical", command=Toplevel1.canvas3.yview)
        Toplevel1.scrollable_frame3 = ttk.Frame(Toplevel1.canvas3)
        Toplevel1.scrollable_frame3.bind(
            "<Configure>",
            lambda e: Toplevel1.canvas3.configure(
                scrollregion=Toplevel1.canvas3.bbox("all")
            )
        )
        for i in range(len(Toplevel1.hist)):
            bt=ttk.Button(Toplevel1.scrollable_frame3)
            eval("bt.configure(command=lambda:Toplevel1.msgact(Toplevel1.hist["+str(i)+"]))")
            bt.configure(compound='top')
            emb=''
            for e in Toplevel1.hist[i].embeds:
                emb=str(e.title)+'\n'+str(e.description)
            bt.configure(text=Toplevel1.hist[i].author.name+'\n'+Toplevel1.hist[i].content+'\n'+emb)
            bt.pack(anchor=tk.W)
            for atc in Toplevel1.hist[i].attachments:
                bt=ttk.Button(Toplevel1.scrollable_frame3)
                bt.configure(compound='top')
                bt.configure(text='[file]'+atc.filename)
                bt.pack(anchor=tk.W)
        Toplevel1.canvas3.create_window((0, 0), window=Toplevel1.scrollable_frame3, anchor="nw")
        Toplevel1.canvas3.configure(yscrollcommand=Toplevel1.scrollbar3.set)
        Toplevel1.scrollbar3.pack(side="right", fill="y")
        Toplevel1.canvas3.pack(side="left", fill="both", expand=True)
    def viewserver(guild):
        print(guild.name)
        Toplevel1.textch=guild.text_channels
        Toplevel1.vcch=guild.voice_channels
        if Toplevel1.TFrame3!=None:
            Toplevel1.TFrame3.destroy()
        Toplevel1.TFrame3 = ttk.Frame(Toplevel1.TFrame2)
        Toplevel1.TFrame3.configure(relief='groove')
        Toplevel1.TFrame3.configure(borderwidth="2")
        Toplevel1.TFrame3.configure(relief="groove")
        Toplevel1.TFrame3.place(relx=0.071, rely=0.0, relheight=0.989, relwidth=0.300)
        Toplevel1.canvas2 = tk.Canvas(Toplevel1.TFrame3)
        Toplevel1.scrollbar2 = ttk.Scrollbar(Toplevel1.TFrame3, orient="vertical", command=Toplevel1.canvas2.yview)
        Toplevel1.scrollable_frame2 = ttk.Frame(Toplevel1.canvas2)
        Toplevel1.scrollable_frame2.bind(
            "<Configure>",
            lambda e: Toplevel1.canvas2.configure(
                scrollregion=Toplevel1.canvas2.bbox("all")
            )
        )
        for i in range(len(Toplevel1.textch)):
            bt=ttk.Button(Toplevel1.scrollable_frame2)
            eval("bt.configure(command=lambda:Toplevel1.viewch(Toplevel1.textch["+str(i)+"]))")
            bt.configure(compound='top')
            try:
               bt.configure(text='#'+Toplevel1.textch[i].name)
            except tk.TclError:
               import re
               astral = re.compile(r'([^\x00-\uffff])')
               s = Toplevel1.textch[i].name
               new_subject = ""
               for i, ss in enumerate(re.split(astral, s)):
                  if not i%2:
                     new_subject += ss
                  else:
                     new_subject += '?'
               print('new_subject:', new_subject)
               bt.configure(text='#'+new_subject)
            bt.pack()
        for i in range(len(Toplevel1.vcch)):
            bt=ttk.Button(Toplevel1.scrollable_frame2)
            eval("bt.configure(command=lambda:Toplevel1.voicech(Toplevel1.vcch["+str(i)+"]))")
            bt.configure(compound='top')
            try:
               bt.configure(text='????'+Toplevel1.vcch[i].name)
            except tk.TclError:
               import re
               astral = re.compile(r'([^\x00-\uffff])')
               s = Toplevel1.textch[i].name
               new_subject = ""
               for i, ss in enumerate(re.split(astral, s)):
                  if not i%2:
                     new_subject += ss
                  else:
                     new_subject += '?'
               print('new_subject:', new_subject)
               bt.configure(text='[voice]'+new_subject)
            bt.pack()
        Toplevel1.canvas2.create_window((0, 0), window=Toplevel1.scrollable_frame2, anchor="nw")
        Toplevel1.canvas2.configure(yscrollcommand=Toplevel1.scrollbar2.set)
        Toplevel1.scrollbar2.pack(side="right", fill="y")
        Toplevel1.canvas2.pack(side="left", fill="both", expand=True)
def start_up(b):
    global bot
    bot=b
    viewbotgui_support.main()

if __name__ == '__main__':
    viewbotgui_support.main()
