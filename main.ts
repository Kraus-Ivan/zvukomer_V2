// ULOZENI NAHODNEHO INTERVALU TONU
let interval = 250
let delka_tonu = 0
input.onButtonPressed(Button.B, function btnB() {
    
    delka_tonu = randint(1, 14) * interval
    basic.showIcon(IconNames.EigthNote)
    music.playTone(262, delka_tonu)
    basic.clearScreen()
})
// OPAKOVANE PREHRATI ULOZENEHO TONU
input.onButtonPressed(Button.A, function btnA() {
    
    if (delka_tonu > 0) {
        basic.showIcon(IconNames.EigthNote)
        music.playTone(262, delka_tonu)
        basic.clearScreen()
    }
    
})
// MERENI CASU UZIVATELE
let stav_mereni = false
let pocatecni_cas = 0
let cas_mereni = 0
input.onLogoEvent(TouchButtonEvent.Touched, function spusteni_mereni() {
    
    stav_mereni = true
    pocatecni_cas = control.millis()
    obrazek_hodin()
})
input.onLogoEvent(TouchButtonEvent.Released, function ukonceni_mereni() {
    
    let konecny_cas = control.millis()
    basic.clearScreen()
    if (stav_mereni == true) {
        cas_mereni = konecny_cas - pocatecni_cas
        stav_mereni = false
    }
    
    if (delka_tonu > 0) {
        vyhodnoceni()
    } else {
        basic.showIcon(IconNames.No)
        soundExpression.sad.play()
    }
    
})
// VYHODNOCENI
// POKUD cas_mereni JE VETSI JAK delka_tonu, ZOBRAZI SE ">" (ODCHYLKA 5% PRESAHU MERENI)
function vyhodnoceni() {
    
    let odchylka = delka_tonu / 100 * 5
    if (cas_mereni <= delka_tonu + odchylka) {
        led.plotBarGraph(cas_mereni, delka_tonu)
        if (led.point(0, 0)) {
            soundExpression.happy.play()
        }
        
    } else {
        basic.showLeds(`
        . # . . .
        . . # . .
        . . . # .
        . . # . .
        . # . . .
        `)
        soundExpression.sad.play()
    }
    
}

// OBRAZEK
function obrazek_hodin() {
    basic.showLeds(`
    # # # # #
    . # # # .
    . . # . .
    . # # # .
    # # # # #
    `)
}

