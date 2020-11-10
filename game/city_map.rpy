
label city_map_day01: 
    if boss_office_visit == False:
        if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
            scene map_day
            call screen map_day01_work
        elif time_of_day == 'NIGHT':
            scene map_night
            call screen map_day01_work
    else:
        if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
            scene map_day
            call screen map_day01_home
        elif time_of_day == 'NIGHT':
            scene map_night
            call screen map_day01_home

label city_map_day02: 
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day02_morning
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day02_morning
    

label city_map_day: 
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day01_home
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day01_home

label city_map_day_stop: 
    if day == 1:
        mc "{i}(I should not be here.){/i}"
        jump city_map_day01
    elif day0203_quest == 1:
        mc "{i}(I should not be here.){/i}"
        jump city_map_day02        
    elif day0203_quest == 3:
        mc "{i}(I should not be here.){/i}"
        jump work_day02_begin
    elif day0203_quest == 4:
        mc "{i}(I should not be here.){/i}"
        jump selina_day02_begin    
    elif day0203_quest == 5:
        mc "{i}(I should not be here.){/i}"
        jump day02_end    
    elif day0203_quest == 6:
        mc "{i}(I should not be here.){/i}"
        jump day03_morning     
    elif day0203_quest == 7:
        mc "{i}(I should not be here.){/i}"
        jump day03_evening          
    else:
        mc "{i}(I should not be here.){/i}"
        jump work_day02_begin

label work_day02_begin:
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day02_evening
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day02_evening

label selina_day02_begin:
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day02_night
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day02_night

label day02_end:
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day02_night02
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day02_night02

label day03_morning:
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day03_morning
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day03_morning

label day03_evening:
    if time_of_day in ('MORNING', 'AFTERNOON', 'EVENING' ):
        scene map_day
        call screen map_day03_evening
    elif time_of_day == 'NIGHT':
        scene map_night
        call screen map_day03_evening



