#ULOZENI NAHODNEHO INTERVALU TONU
interval = 250 
delka_tonu = 0
def btnB():
    global interval, delka_tonu
    delka_tonu = randint(1, 14) * interval
    basic.show_icon(IconNames.EIGTH_NOTE)
    music.play_tone(frequency = 262, ms = delka_tonu)
    basic.clear_screen()
input.on_button_pressed(Button.B, btnB)

#OPAKOVANE PREHRATI ULOZENEHO TONU
def btnA():
    global delka_tonu
    if delka_tonu > 0:
        basic.show_icon(IconNames.EIGTH_NOTE)
        music.play_tone(frequency = 262, ms = delka_tonu)
        basic.clear_screen()
input.on_button_pressed(Button.A, btnA)

#MERENI CASU UZIVATELE
stav_mereni = False
pocatecni_cas = 0
cas_mereni = 0

def spusteni_mereni():
    global pocatecni_cas, stav_mereni
    stav_mereni = True
    pocatecni_cas = control.millis()
    obrazek_hodin()
input.on_logo_event(TouchButtonEvent.TOUCHED, spusteni_mereni)

def ukonceni_mereni():
    global pocatecni_cas, stav_mereni, cas_mereni, delka_tonu
    konecny_cas = control.millis()
    basic.clear_screen()

    if stav_mereni == True:
        cas_mereni = (konecny_cas - pocatecni_cas)
        stav_mereni = False
        
    if delka_tonu > 0:
        vyhodnoceni()
    else:
        basic.show_icon(IconNames.NO)
        soundExpression.sad.play()
input.on_logo_event(TouchButtonEvent.RELEASED, ukonceni_mereni)

#VYHODNOCENI
#POKUD cas_mereni JE VETSI JAK delka_tonu, ZOBRAZI SE ">" (ODCHYLKA 5% PRESAHU MERENI)
def vyhodnoceni():
    global cas_mereni, delka_tonu
    odchylka = (delka_tonu/100)*5
    if cas_mereni <= (delka_tonu + odchylka):
        
        led.plot_bar_graph(cas_mereni, delka_tonu)
        if led.point(0, 0):
            soundExpression.happy.play()
    else:
        basic.show_leds("""
        . # . . .
        . . # . .
        . . . # .
        . . # . .
        . # . . .
        """)
        soundExpression.sad.play()

#OBRAZEK
def obrazek_hodin():
    basic.show_leds("""
    # # # # #
    . # # # .
    . . # . .
    . # # # .
    # # # # #
    """)