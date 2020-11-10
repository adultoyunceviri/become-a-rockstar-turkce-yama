
label bar: 
    scene bar_night
    call screen bar

label stair:
    if boss_office_visit == False:
        jump boss_office_day01
    else:
        mc "{i}(I've just been there. Better go see Jacob now.){/i}"
        jump bar

label bartender:
    scene 2work02
    "Bartender" "Can I get you something?"
    mc "No thanks. That's enough for today."
    jump bar

label bar_exit:
    if boss_office_visit == False:
        mc "{i}(Before I left, I promised to go to Catherine's office.){/i}"
        jump bar
    else: 
        jump after_work

label pooltable:
    if pooltable == False:
        scene pooltable01
        "You relaxed a little and played pool."
        $ pooltable = True
        jump bar
    else:
        "You've played pool recently, that's enough for now."
        jump bar


