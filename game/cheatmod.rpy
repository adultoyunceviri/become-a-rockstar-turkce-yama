define selina_path=False
define rosa_path=False
define lisa_path=False
define lisa_friends_path=False
define jane_path=False
define jane_date_offer=False
define selina_broke_up=False
define anna_sex=False
define anna_colleague=False
define jade_path=False
define jade_kiss=False
define emma_sex=False

init python:
    config.overlay_screens.append("cheats")
    style.pref_button_text.ypadding = 0

screen cheats():
    zorder 100
    hbox:
        style_prefix "quick"
        xalign 1.0
        yalign 1.0


        textbutton _("{b}CHEATS{/b}") action ShowMenu("cheat_menu") text_size 17



screen cheat_menu():
    
    frame:
        background "gui/cm_back.png"
        xalign .98
        yalign .98

        has vpgrid:
            xfill True
            yfill True
            cols 5
            rows 12
            spacing 70
            scrollbars "vertical"
            mousewheel True



        text "Kapatmak için Esc tuşuna basın" size 25
        text ""
        textbutton "ADULT OYUN ÇEVİRİ HİLE" action OpenURL("https://www.adultoyunceviri.com/") pos(0.01,0.2) text_size 25 text_color "#f4aa44"
        text ""
        textbutton "Discord" action OpenURL("https://discord.com/invite/XsKNAub") pos(0.01,0.2) text_size 25 text_color "#f4aa44"
        #text ""
#############################
        textbutton "Lisa'nın Yolu:[lisa_path]" action Replay("1") text_size 25 text_color "#ffffff"
        #text "Lisa'nın Yolu:[lisa_path]" size 25 color "#ffffff"
        if lisa_path == True:
            textbutton "Deaktif et" action [SetVariable("lisa_path",False),SetVariable ("lisa_friends_path",True)] text_size 25
        elif lisa_path==False:
            textbutton "Aktif et" action [SetVariable("lisa_path",True),SetVariable ("lisa_friends_path",False)] text_size 25
        else:
            text "" size 25
        textbutton "Lisa'nın Puanı: [RPls]" action Replay("1") text_size 25 text_color "#ffffff"
        textbutton "+1 Puan" action SetVariable("RPls",RPls+1) text_size 25
        textbutton "-1 Puan" action SetVariable("RPls",RPls-1) text_size 25
############################################################################################
        textbutton "Jane'nın Yolu:[jane_path]" action Replay("1")text_size 25 text_color "#ffffff"
        if jane_path == True:
            textbutton "Deaktif et" action [SetVariable("jane_path",False),SetVariable("jane_date_offer",False)] text_size 25
        elif jane_path==False:
            textbutton "Aktif et" action [SetVariable("jane_path",True),SetVariable("jane_date_offer",True)]text_size 25
        textbutton "Jane'nın Puanı: [RPjn]" action Replay("1")text_size 25 text_color "#ffffff"
        textbutton "+1 Puan" action SetVariable("RPjn",RPjn+1) text_size 25
        textbutton "-1 Puan" action SetVariable("RPjn",RPjn-1) text_size 25
#####################################################################################################        
        textbutton "Selina'nın Yolu:[selina_path]" action Replay("1") text_size 25 text_color "#ffffff"
        if selina_path == True:
            textbutton "Deaktif et" action [SetVariable("selina_path",False),SetVariable("selina_broke_up",True)] text_size 25
        elif selina_path==False:
            textbutton "Aktif et" action [SetVariable("selina_path",True),SetVariable("selina_broke_up",False)]text_size 25
        textbutton "Selina'nın Puanı: [RPs]" action Replay("1") text_size 25 text_color "#ffffff"
        textbutton "+1 Puan" action SetVariable("RPs",RPs+1) text_size 25
        textbutton "-1 Puan" action SetVariable("RPs",RPs-1) text_size 25
        
##################################################################################################
        textbutton "Anna'nın Yolu:[anna_sex]" action Replay("1") text_size 25 text_color "#ffffff"
        if anna_sex == True:
            textbutton "Deaktif et" action [SetVariable("anna_sex",False),SetVariable("anna_colleague",True)] text_size 25
        elif anna_sex == False:
            textbutton "Aktif et" action [SetVariable("anna_sex",True),SetVariable("anna_colleague",False)]text_size 25
        else:
            text "" size 25
        textbutton "Anna'nın Puanı: [RPa]" action Replay("1") text_size 25 text_color "#ffffff"
        textbutton "+1 Puan" action SetVariable("RPa",RPa+1) text_size 25
        textbutton "-1 Puan" action SetVariable("RPa",RPa-1) text_size 25
############################################################################################################
        textbutton "Rosa'nın Yolu:[rosa_path]" action Replay("1") text_size 25 text_color "#ffffff"
        if rosa_path == True:
            textbutton "Deaktif et" action SetVariable("rosa_path",False) text_size 25
        elif rosa_path==False:
            textbutton "Aktif et" action SetVariable("rosa_path",True)text_size 25
        text ""
        text ""
        text ""
        #textbutton "Selina'nın Puanı: [RPs]" action Replay("1") text_size 25 text_color "#ffffff"
        #textbutton "+1 Puan" action SetVariable("RPs",RPs+1) text_size 25
        #textbutton "-1 Puan" action SetVariable("RPs",RPs-1) text_size 25
        
##############################################################################
        textbutton "Jade'nın Yolu:[jade_path]" action Replay("1") text_size 25 text_color "#ffffff"
        if jade_path == True:
            textbutton "Deaktif et" action [SetVariable("jade_path",False),SetVariable("jade_kiss",False)] text_size 25
        elif jade_path==False:
            textbutton "Aktif et" action [SetVariable("jade_path",True),SetVariable("jade_kiss",True)]text_size 25
        textbutton "Jade'nın Puanı: [RPjd]" action Replay("1") text_size 25 text_color "#ffffff"
        textbutton "+1 Puan" action SetVariable("RPjd",RPjd+1) text_size 25
        textbutton "-1 Puan" action SetVariable("RPjd",RPjd-1) text_size 25
#####################################################################################
        textbutton "Emma'nın Yolu:[emma_sex]" action Replay("1") text_size 25 text_color "#ffffff"
        if emma_sex == True:
            textbutton "Deaktif et" action SetVariable("emma_sex",False) text_size 25
        elif emma_sex==False:
            textbutton "Aktif et" action SetVariable("emma_sex",True)text_size 25
        text ""
        text ""
        text ""
        
#################################################################
        textbutton "Nicole'nın Yolu:[nicole_plus]" action Replay("1") text_size 25 text_color "#ffffff"
        if nicole_plus == True:
            textbutton "Deaktif et" action SetVariable("nicole_plus",False) text_size 25
        elif nicole_plus==False:
            textbutton "Aktif et" action SetVariable("nicole_plus",True)text_size 25
        text ""
        text ""
        text ""
        
###########################################################################################
        textbutton "Catherine'nın Yolu:[day10_catherine_offer]" action Replay("1") text_size 25 text_color "#ffffff"
        if day10_catherine_offer == True:
            textbutton "Deaktif et" action SetVariable("day10_catherine_offer",False) text_size 25
        elif day10_catherine_offer==False:
            textbutton "Aktif et" action SetVariable("day10_catherine_offer",True)text_size 25
        text ""
        text ""
        text ""
#########################################################################################################
        textbutton "Tüm galeri sahnelerinin kilidini açın" action Function (unlock_all) text_size 25 text_color "#ffffff" text_hover_color "#0099ff"
###########################################################################################################
       # textbutton "Marie'nın Yolu:[marie_path]" action Replay("1") text_size 25 text_color "#ffffff"
        #if marie_path == True:
         #   textbutton "Deaktif et" action SetVariable("marie_path",False) text_size 25
        #elif marie_path==False:
         #   textbutton "Aktif et" action SetVariable("marie_path",True)text_size 25
        #textbutton "Marie'nın Puanı: [RPm]" action Replay("1") text_size 25 text_color "#ffffff"
        #textbutton "+1 Puan" action SetVariable("RPm",RPm+1) text_size 25
        #textbutton "-1 Puan" action SetVariable("RPm",RPm-1) text_size 25
####################################################################################################
        #textbutton "Eva'nın Yolu:[eva_path]" action Replay("1") text_size 25 text_color "#ffffff"
        #if eva_path == True:
         #   textbutton "Deaktif et" action SetVariable("eva_path",False) text_size 25
        #elif eva_path==False:
         #   textbutton "Aktif et" action SetVariable("eva_path",True)text_size 25
        #textbutton "Eva Score:[RPe]" action Replay("1") text_size 25 text_color "#ffffff"
        #textbutton "+1 Puan" action SetVariable("RPe",RPe+1) text_size 25
        #textbutton "-1 Puan" action SetVariable("RPe",RPe-1) text_size 25
        
#############################################
#mc cheat point,good/bad points,father enemy, other chars etc
#jacob,jade,nicole,rosa,emma ,selina_broke_up,jade_kiss,rosa_broke_up,jane_date_offer
        
init python:        
 def unlock_all():
        persistent.day01selina=True
        
        persistent.day02jane=True
        persistent.day02selina=True
        persistent.day03eva=True
        persistent.day03marie=True
        persistent.day03lisa=True
        persistent.day04selina=True
        persistent.day04anna=True
        persistent.day04jane=True
        persistent.day05selina=True
        persistent.day05lisa =True
        persistent.day06anna  =True
        persistent.day06jane  =True
        persistent.day06lisa=True
        persistent.day07emma=True
        persistent.day07selina  =True
        persistent.day08lisa  =True
        persistent.day08lisa2  =True
        persistent.day08jane=True
        persistent.day08jacob=True
        persistent.day08rosa=True
        persistent.day09selina=True
        persistent.day09selina2=True
        persistent.day09rosa=True
        persistent.day09emma=True
        persistent.day09lisajade=True
        persistent.day10selina=True 
        persistent.day10lisajade=True 
        persistent.day10lisa=True 
        persistent.day10jane=True 
        persistent.day10anna=True
        persistent.day11nicole=True
        persistent.day11emma=True
        persistent.day11jade=True
        persistent.day11jasmine=True    
                
        

          

        persistent.day12nicole = True
        persistent.day12catherine = True
        persistent.day12lisa = True       
        
        
label day12_phone_calls:

    menu:
        "Selina sahnesi":
            
            jump day12_selina_call
        "Jane sahnesi":
            jump day12_jane_call
        
        "Anna sahnesi":
            jump day12_anna_call