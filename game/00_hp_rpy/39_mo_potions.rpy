###POTION SCENES
label potion_scene_1: #catears (keep in mind Genie is trying to transform her into another girl)
    m "[hermione_name]?"
    $ her_main("Yes, [genie_name]?","body_01")
    m "Today I have a new type of favour for you to perform."
    $ her_main("What do you mean new? What do I have to do?","body_07")
    m "It's quite simple, today you will be drinking a potion"
    $ her_main("Is that it? How much will I get paid?","body_08")
    m "20 points."
    $ her_main("Hmmm, what type of potion is it?","body_17")
    $ her_main("Polyjuice? Amortentia? Babbling Beverage? Felix Felicis?","body_24")
    m "That's a secret [hermione_name]."
    $ her_main("...","body_73")
    m "Well [hermione_name], what do you say? Will you drink a harmless little potion?"
    m "For Gyrffindor?"
    $ her_main("Fine...","body_16")
    ">Hermione takes a whif of the thick potion."
    $ her_main("This smells disgusting. Like mud and wet dog fur.","body_43")
    $ her_main("Do I really have to drink this?","body_11")
    m "You do. I suggest holding your nose if the smell is too much."
    $ her_main("For Gryffindor.","body_20")
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione holds her nose and quickly downs the flask."
    $ her_main("","body_42")
    pause
    $ her_main("","body_22")
    hide screen ch_potion
    show screen hermione_blink
    her "Ughhh. That was horrible."
    m "Well done."
    $ her_main("Now will you at least tell me what this potion does.","body_21")
    m "It should be noticeable any second now..."
    $ her_main("Well? Is it supposed to make my breasts bigger? They don't feel any bigger.","body_73")
    m "No. Hmmmm, it mustn't have worked."
    $ her_main("What was it supposed to do?","body_70")
    m "There's no point in telling you now. It was going to be a surprise."
    m "Damn Snape must've conned me."
    $ her_main("Is that all [genie_name]?","body_15")
    m "Yes, [hermione_name], 20 points to Gryffindor."
    $ her_main("Thank you [genie_name].","body_06")
    ">Hermione heads off to class."
    $ gryffindor += 20

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ ears = True
    if hair_color == 5:
        $ hair_color = 0
    elif hair_color == 6:
        $ hair_color = 1
    elif hair_color == 7:
        $ hair_color = 3
    elif hair_color == 8:
        $ hair_color = 4
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_1_2: #Scene where Hermione comes back after classes angry and confused at being given cat ears and a tail.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    $ her_main("How could you do this to me [genie_name]?","body_05")
    her "Try and turn me into a cat!"
    $ her_main("In the middle of class!","body_29")
    m "I didn't try and turn you into a cat [hermione_name]."
    $ her_main("Then why do I have ears and a tail?","body_30")
    m "I have no idea. The potion I gave you was supposed to turn you into a different girl."
    $ her_main("What!? You didn't use polyjuice potion did you [genie_name]?","body_48")
    m "What's that?"
    $ her_main("There's no point playing dumb [genie_name].","body_79")
    $ her_main("Well at least I know that it will wear off by morning.","body_69")
    menu:
        "-Let her go-":
            m "Goodnight [hermione_name]."
            $ her_main("Goodnight [genie_name].","body_120")
            hide screen bld1
            hide screen hermione_main
            hide screen blktone 
            hide screen ctc
            with Dissolve(.3)
            $ ears = False
            
            call her_walk(400,610,2)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            with Dissolve(.3)
            
            $ hermione_sleeping = True
            jump night_main_menu
        "-Make her suck you off-" if whoring >= 17:
            pass
    m "Wait [hermione_name], how would you like to earn 75 additional points?"
    $ her_main("75 points? How?","body_17")
    m "By sucking my cock."
    $ her_main("Like this? I look like a cat! Why would you ask me at a time like this?","body_119")
    $ her_main("You're not some sort of pervert who likes animals are you?","body_117")
    m "Of course not, I just think that you have a very unique look at the moment and that it would be a shame not to do anything with it."
    $ her_main("Fine, just promise me you aren't going to do anything weird.","body_120")
    m "I promise. Now, kneel."
    ">Hermione walks over and kneels before you."
    m "Good girl."
    $ her_main("...","body_115")
    ">Hermione takes you into her mouth"                ###Have the chibi scene of her sucking
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    show screen g_c_u
    
    hide screen hermione_blink #Hermione stands still.
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    show screen ctc
    with fade
    pause
    show screen bld1
    with d3
    m "Good god what is with your tongue?! It feels like velcro."
    her "*Slurp?*"    
    $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_chibi_ypos = 10
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ hermione_main_zorder = 8
    $ her_main("It's because of your stupid potion, it's \nmade my tongue all rough.","body_116")
    $ her_main("Do you want to stop?","body_68")
    hide screen hermione_main
    m "No, keep going, just try not to focus on the tongue work too much."
    $ her_main("Yes [genie_name].","body_69")
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    hide screen h_c_u
    show screen g_c_u
    with d3
    ">Hermione swallows your cock again, taking care\nnot to apply too much pressure with her tongue."   ###start sucking scene. might insert more sucking noises for a little while or add pauses
    m "So you still went to all your classes?"
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ her_main("Of course [genie_name].","body_128")     
    hide screen hermione_main  
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    hide screen h_c_u
    show screen g_c_u
    m "Even looking like this?"                         ###start sucking
    m "What would everyone have thought? Would they just assume that you were under an evil slytherin spell?"
    m "Or would they just think that slutty little Miss Granger was just begging for attention again."
    m "Wearing skimpy outfits and trying to look like a cat."
    ">You go to place your hand on the back of her head but her new ears block the way."
    m "These are quite soft."
    ">You start feeling and patting the ears."
    ">Hermione starts involuntary purring"
    m "Oh good heavens!"
    m "It's like your whole mouth has become a vibrator."
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ her_main("I can't help it [genie_name], whenever \nanything touches my ears I just purr.","body_74")
    hide screen hermione_main
    m "It feels amazing, now cock back in the mouth girl."
    $ her_main("Yes [genie_name].","body_80")
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    hide screen h_c_u
    show screen g_c_u
    hide screen hermione_main
    with d3
    m "You immediately put your hands back on her ears and start stroking them as she sucks you."### start sucking
    her "*Slurp!* *Purr* *Slurp!*"
    m "Oh gods yes. This is Fantastic."
    her "*Purr* *Slurp!* *Purr*"
    m "Get ready girl... Here it comes."
    her "*Purr* *Purr* *Purr*"
    ">You grab her ears and pull her head into you causing the tip of your cock to rest on her purring throat."###show genie climax scene
    g4 "{size=+10}ARGH!!!!!!!!!!!!!!!!{/size}"
    her "*Purr* *Purr* *Purr*"
    ">You shoot you load directly down her throat."     ###have picture 125 and 126 play each time she swallows
    show screen ctc
    pause
    with d3
    $ g_c_u_pic = "cum_in_mouth_ani"
    hide screen h_c_u   # SUCKING
    show screen g_c_u # SUCKING
    with d3 
    $ her_main("","body_125")
    pause .1
    $ her_main("*gulp* *Purr* *Purr*","body_126")
    $ her_main("","body_125")
    pause .1
    $ her_main("*gulp* *Purr* *gulp*","body_126")
    $ her_main("","body_125")
    pause .1
    $ her_main("*Purr* *gulp* *gulp*","body_126")
    ">You pull your cock out of her purring mouth."
    show screen h_c_u
    hide screen g_c_u
    $ her_main("Mmmmm, it might be this potion but that tasted \ngood...","body_128")
    hide screen hermione_main
    m "Well, you certainly earned your 75 points."
    $ gryffindor += 75
    $ h_c_u_pic = "hand_ani"
    $ her_main("Thank you [genie_name]. Will that be all.","body_78")
    hide screen hermione_main
    m "One last thing."
    m "Who's a good girl?"
    $ her_main("..........","body_29")
    $ her_main("I am...","body_46")

    $ ears = False
    $ hermione_main_zorder = 5
    hide screen chair_02
    hide screen bld1
    hide screen h_c_u
    hide screen g_c_u
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ hermione_chibi_ypos = 250
    jump night_main_menu
    
    
label potion_scene_2_1: #breast expansion - Until chibis are added for it tifucking won't be written
    m "Guess what I have for you today."
    $ her_main("Is it another foul tasting potion that will try transform me into a hideous animal?","body_04")
    m "Well I mean this one smells nice."
    $ her_main("Will it taste nice though?","body_02")
    m "Only one way to find out."
    ">You hand her the potion and she brings it up to her nose."
    $ her_main("Well you're right, it does smell good. Let's find out if it tastes good...","body_06")
    hide screen hermione_blink
    show screen ch_potion
    ">She drinks the potion at a leisurely pace."
    $ her_main("Ahhh.","body_74")
    $ her_main("","body_64")
    show screen hermione_blink
    hide screen ch_potion
    her "That wasn't actually that bad."
    $ her_main("So, now that I've had the potion, will you tell me what it's supposed to do.","body_122")
    m "No need to ruin the fun, it should take effect relatively quickly."
    $ her_main("Well what am I supposed to do until then?","body_128")
    m "You could show me your tits."
    $ her_main("I don't think so [genie_name], you're only paying me for drinking the potion.","body_127")
    $ her_main("If you expect to see me without my shirt on then you'll have to try a little harder.","body_129")
    m "Oh I wouldn't be so sure of that."
    $ her_main("So is that what it does? Makes me show you my breasts? Is it some sort of mind control potion?","body_45")
    m "Mind control? Where's the fun in that? No, this is something much more entertaining."
    $ her_main("Well it better happen soon otherwise I'm lea-","body_69")
    ">You notice her breasts start to expand ever so slightly." ###Start using facial expressions mixed with Captain Nemo art
    $ her_main("...","body_79")
    $ her_main("As I said, something better happen soon or I'm leaving.","body_29")
    m "I wouldn't worry about it, from the looks of it, it's already started."
    $ her_main("Why, what's wrong with me?","body_31")
    m "There's nothing wrong with you. If anything, it's an improvement."
    $ her_main("What is?","body_79")
    ">She starts patting down her body. Checking to see if she has grown any new ears or a tail."
    $ her_main("I don't see what you could be...","body_87")
    ">She grabs her breasts to check them."
    $ her_main("!!!","body_118")
    $ her_main("Have my breasts gotten bigger?","body_119")
    m "About time you noticed."
    $ her_main("Why would you make my breasts bigger? They're already big enough!","body_117")
    m "You know what they say, can't have too much of a good thing."
    $ her_main("It's the other way around [genie_name].","body_79")
    m "Is it? Well I prefer my version."
    $ her_main("Well how big are they supposed to-","body_118")
    ">Her breast swell up again."
    $ custom_breast = 4
    $ her_main("You can't be serious. At this rate they're going to rip my shirt.","body_119")
    m "Well they should stop there."
    $ her_main("Good, they're big enough as is.","body_47")
    menu:
        "-Send her to class-":
            m "You're right, I suppose they are big enough."
            m "Well that's all for today, 20 points to Gryffindor."
            $ her_main("That's all? You're not going to make me do something else?","body_48")
            m "Why would I, I asked you to drink a potion and you drank it. You're free to leave."
            $ her_main("Thank you [genie_name], I'll head back to my room.","body_46")
            m "Room? It's time for class [hermione_name]. What do you think Professor Snape will say once he hears that you skipped class?"
            $ her_main("Well I can't be expected to go like this.","body_66")
            m "Why not? Everything is covered."
            $ her_main("Barely. And what will people think of me.","body_118")
            m "Just tell them that you are still developing. I'm sure that they're used to enormous breasts anyway, what's a few extra sizes."
            $ her_main("...Fine. Just promise me that they won't get any bigger.","body_120")
            m "I can't promise that, your still in highschool. A lot of girls don't stop growing until their 30."
            $ her_main("You know what I mean [genie_name].","body_86")
            m "I'm afraid that I don't [hermione_name], now you'd best hurry if you don't want to be late."
            $ her_main("...Yes [genie_name].","body_79")
            hide screen bld1
            hide screen hermione_main
            hide screen blktone 
            hide screen ctc
            with Dissolve(.3)
            
            call her_walk(400,610,2)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            with Dissolve(.3)
            
            $ hermione_takes_classes = True
            jump day_main_menu
        "-Play with her breasts-":
            pass
    m "Well that's a matter of personal opinion."
    m "Now how would you like to earn some additional points?"
    $ her_main("I want an extra 40.","body_79")
    m "I haven't even told you what I want to-"
    $ her_main("If you want to touch my breasts it will be an extra 40 points.","body_69")
    m "Deal."
    ">Hermione walks over to behind your desk, her breasts swaying rhythmically as she moves."
    show screen blkfade
    hide screen hermione_blink #Stands with tits out.
    hide screen genie
    show screen groping_naked_tits
    with d1
    with d5
    hide screen blkfade
    $ her_main("Well...","body_44")
    ">You reach out and grab her breasts through her stretched shirt."
    $ her_main("!!!","body_119")
    $ her_main("Please be gentle [genie_name]. They seem to be much more sensitve than usual, it must be the potion.","body_117")
    m "Well I'll take that into account..."
    ">You take a breast in each hand and start kneading them with your fingers."
    $ her_main("...","body_127")
    m "They're certainly much larger than usual."
    $ her_main("...yes","body_121")
    ">You continue massaging them gently through her shirt. Pulling them apart and then pressing them into one another."
    $ her_main("...It feels like they're getting-","body_118")
    $ custom_breast =2
    $ custom_outfit_old = 20
    "*RIIIP*"
    $ her_main("!!!","body_119")
    $ her_main("You said that they wouldn't get any bigger! Now look, my shirt has been ruined.","body_86")
    m "Don't worry about that [hermione_name], worry about earning your 40 points."
    $ her_main("Just hurry up.","body_79")
    menu: #Will add titfuck here
        #"-Suck her nipples-":
            #"asd"
        #"-Titfuck her-":
            #"asd"
        "-Play with her nipples-":
            pass
    ">You take her exposed breasts back into your hands and continue massaging"
    $ her_main("sir... they seem to have become more sensitive...","body_78")
    $ her_main("Please don't do anything sudden.","body_121")
    m "Like this?"
    ">You take both nipple between your thumb and index finger."
    $ her_main("!!!","body_130")
    $ her_main("Please stop... it's too much, it's like my nipples are on fire.","body_132")
    m "Shhhh, just be still, it'll all be over soon."
    ">You start rolling her nipples in between your fingers."
    $ her_main("...","body_131")
    ">You feel her push her crotch against your thigh."
    m "Feeling a little aroused are we?"
    ">You start to pinch and pull her nipples."
    $ her_main("Ohhh","body_121")
    ">She starts grinding herself against your thigh"
    m "Well, well, well, you are sensitive now aren't you? Trying to grind out an orgasm on your headmasters leg, how shameless."
    $ her_main("...","body_123")
    m "Well let's see if we can do something about that."
    ">You start alternating pinching and pulling her nipples hard, pulling the nipples out as far as you can and then pushing them back into her breast."
    $ her_main("!!!","body_130")
    her "I-I-I'm cumming!"
    ">She starts grinding hard against your leg as a wet spot starts to form on her skirt."
    m "What a naughty little girl."
    ">She breathes heavily as she rests against you"
    $ her_main("Will... that be all [genie_name]?","body_121")
    m "Yes [hermione_name]. You can go now."
    $ custom_breast = 0
    $ custom_outfit_old = 0
    hide screen bld1
    hide screen hermione_main
    hide screen groping_naked_tits
    hide screen blktone 
    hide screen ctc
    show screen genie
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_takes_classes = True
    jump day_main_menu



label potion_scene_2_1_2: #Hermione comes back after having her breasts expand in class


label potion_scene_2_2: #ass expansion
    m "[hermione_name], I have another potion for you to try today."
    $ her_main("Another one? Where are you getting these?","body_08")
    m "That's of no concern to you. What should concern you is the 20 points that you are able to earn should you drink it."
    $ her_main("...Fine, give me the bottle.","body_07")
    ">She takes a quizzical smell of the bottle."
    $ her_main("At least this one smells good.","body_06")
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">She drinks the whole potion over a series of gulps."
    hide screen ch_potion
    with d3
    show screen hermione_blink
    $ her_main("Ahhh, that was good! So what was it?","body_24")
    m "The effects should be visible soon enough."
    $ her_main("Well can you at least give me a hint?","body_14")
    m "Let's just say that it's a redistribution of ass{w}ets." ###Added {w} instead of your ...
    $ her_main("What do you mean by--","body_12")
    ">Hermione goes white as she starts to feel her body churn."
    $ her_main("What's going on. It feels like my insides are moving.","body_18")
    $ her_main("And my ass, it feels so... good.","body_121")
    ">You start to notice her ass increase in size."    ###Use bigger butt from Captain Nemo
    $ her_main("It feels too sensitive... I have to take my skirt off","body_119") ###changed so to too
    pause 0.2
    $ custom_skirt = 2
    $ her_main("ughhh, has it gotten bigger?","body_118")
    $ her_main("Is that what this potion's supposed to do? Makes my ass bigger?","body_120")
    m "Evidently."
    $ her_main("Why does my ass feel so good?","body_121") ###new
    ">Hermione keeps rubbing her ass, rolling her fingers across her expanded buttocks."
    m "Hmmm, it's not supposed to, but I guess every case is different."
    $ her_main("It's just so sensitive... [genie_name] do you think that you could... massage me?","body_123")
    m "Well I mean I'm hardly going to say no am I."
    ">Hermione hops over to your desk, her ass bouncing as she moves, and presents herself to you."
    hide screen bld1
    with d3
    
    call her_walk(400,280,3,redux_pause=2)
    show screen blkfade
    with Dissolve(1)
    pause.5
    hide screen genie
    show screen ctc
    show screen no_groping_02
    with d1
    hide screen blkfade
    with d5
    pause
    $ her_main("Please [genie_name]... please take advantage of me...","body_131")
    m "As you command."
    ">You take her engorged buttocks in your hands. Each one is now much larger than before."
    hide screen hermione_main
    hide screen no_groping_02
    with d3
    show screen groping_02
    m "Well this potion certainly is effective."
    ">You start firmly stroking her ass cheeks. Pulling them apart to reveal her asshole and then squishing them together."
    ">Seeing her tight asshole gives you an idea."
    $ hermione_main_zorder = 8
    menu: #Thought about adding a rimming option here but the chibis don't really support it
        "-Finger her asshole-":
            ">You pull her asscheeks open again to show her puckered hole."
            m "Let's see how sensitive you really are."
            ">You start teasing the entrance with your finger, circling the entrance slowly."
            $ her_main("!!!","body_132")
            $ her_main("[genie_name] please... I'm too sensitive. If you do that, \nI'm not sure I'll be able to control myself.","body_121")
            hide screen hermione_main
            m "Well in that case..."
            ">You slowly pull your finger away from her asshole."
            $ her_main("Thank yo-","body_121")
            ">And then fully insert it."
            $ her_main("...","body_119")
            her "..."
            her "..."
            $ her_main("{size=-10}I'm cumming{/size}","body_130")
            hide screen hermione_main
            m "What was that?"
            ">You start turning your finger."
            $ her_main("{size=+10}I'm cumming!{/size}","body_32")
            ">Her asshole starts quivering around your finger."
            hide screen hermione_main
            m "What a little anal slut. I wonder what you'll do once I try this."
            ">You start pumping your finger in and out of her shivering asshole."
            $ her_main("!!!","body_132")
            $ her_main("I'm cumming again!","body_131")
            m "So soon?"
            $ her_main("I can't stop! Please [genie_name], please, no more!","body_119")
            menu:
                "-Stop-":
                    m "Well, I suppose that's enough for now..."
                    ">You pull your finger out of her asshole and she immediately slumps over your desk."
                    $ her_main("That was... great...","body_123")
                    ">She lies on your desk, breathing heavily."
                "-Keep Going-":
                    m "What was that [hermione_name]? It almost sounded like you asked me to stop."     ###Or would it be better if she start to tear up and cry a bit?
                    ">You increase the pace."
                    $ her_main("Please...","body_131")
                    m "Please what?"
                    ">You insert a second finger."
                    $ her_main("Please... stop... you'll break me...","body_118")
                    ">You grab her hip with one hand and keep finger fucking her asshole."
                    $ her_main("...","body_132")
                    $ her_main("...","body_32")
                    ">You feel her body go limp as her asshole relentlessly quivers around your fingers."
                    m "There, wasn't that nice?"
                    ">You slow down and pull out of her asshole."
                    $ her_main("...yeeess...[genie_name]...","body_123")
                    m "Good girl."
            m "Well you best be off to class."
            $ her_main("...With my butt looking like this?","body_118")
            m "I'm sure no one will be able to tell \nwith your skirt on. Now hurry up \nI have things to attend to."
            $ hermione_main_zorder = 5
            hide screen blktone8
            hide screen ctc
            hide screen bld1
            hide screen groping_01
            hide screen groping_02
            show screen hermione_blink
            show screen genie
            with d1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            show screen bld1
            hide screen blkfade
            with Dissolve(1)
            $ her_main("Yes [genie_name].","body_124")
            m "Oh I almost forgot, 20 points to Gryffindor!"
            $ gryffindor += 20
            $ her_main("Oh... right, the points. Thank you.","body_123")
            ">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it."
            $ custom_skirt = 0
            $ her_main("...","body_87")
        "-Hot dog her-" if whoring >= 17:
            m "Bend over [hermione_name]."
            ">Before she even has a chance to react you push her forward over your desk."
            hide screen hermione_main
            hide screen groping_02
            with d3
            show screen ch_hotdog
            $ her_main("!!!","body_119")
            $ her_main("What are you going to do [genie_name]?","body_122")
            hide screen hermione_main
            m "Well seeing as how your ass has become so fucking huge I thought I may as well put it to good use."
            ">You pull you cock out from your robes and place it on top of her ass crack."
            $ her_main("Your not going to fuck my asshole are you [genie_name]?","body_123")
            hide screen hermione_main
            m "Not your asshole, [hermione_name], I intend to fuck your entire ass!"
            ">You grab a firm hold of her cheeks and pull them apart, allowing your shaft to rest in between, on top of her asshole."
            m "A perfect fit wouldn't you say?"
            $ her_main("What do you-","body_117")
            hide screen hermione_main
            ">You squeeze her asscheeks back together around your cock and start pumping in between them."
            $ her_main("!!!","body_136")
            hide screen hermione_main
            m "Fuck, you're ass is so soft. It's like fucking a pillow."
            $ her_main("Ahhh","body_138")
            $ her_main("Please [genie_name]","body_134")
            hide screen hermione_main
            m "Ughh, this feels so good, we might have to make this permanent."
            $ her_main("Permanent?","body_139")
            hide screen hermione_main
            m "You wouldn't mind would you?"
            m "Having me use your ass a sextoy everyday."
            $ her_main("...","body_141")
            hide screen hermione_main
            m "I asked you a question [hermione_name]."
            $ her_main("... no [genie_name]...","body_133")
            hide screen hermione_main
            ">You feel her asshole start quiver as you glide over it."
            m "Of course you wouldn't, you're enjoying this more than I am, aren't you?"
            $ her_main("...yes... I'm loving... you using my ass as your toy","body_134")
            hide screen hermione_main
            m "That's it girl, here I come!"
            ">With one final thrust you cum, covering her fat ass with your seed."
            hide screen ch_hotdog
            $ g_c_u_pic = "sex_cum_out_ani"
            show screen chair_02
            show screen g_c_u
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            show screen ctc
            pause
            hide screen ctc
            $ uni_sperm = True
            $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
            m "Ughhh"
            m "All over your fucking back."
            ">You fall back into your chair, spent."
            m "You may go now [hermione_name]."
            $ hermione_main_zorder = 5
            hide screen blktone8
            hide screen ctc
            hide screen bld1
            hide screen groping_01
            hide screen groping_02
            hide screen chair_02
            hide screen g_c_u
            show screen hermione_blink
            show screen genie
            with d1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            show screen bld1
            hide screen blkfade
            with Dissolve(1)
            $ her_main("...With my butt looking like this?","body_141")
            m "I'm sure no one will be able to tell with your skirt on. Now hurry up, I feel like a nap.'"
            #$ her_main("Yes [genie_name].","body_141")
            m "Oh I almost forgot, 20 points to Gryffindor!"
            $ gryffindor += 20
            $ her_main("Oh... right, the points. Thank you.","body_136")
            ">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it."
            $ custom_skirt = 0
            ">Your cum is still visible on her ass."
            $ her_main("...","body_127")


    hide screen bld1
    hide screen hermione_main
    $ uni_sperm = False
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ hermione_takes_classes = True
    hide screen groping_02
    hide screen hermione_main
    hide screen no_groping_02

    jump day_main_menu
        #will add this later
        #"-Fuck her ass-" if whoring >= 22:    

label potion_scene_3: #cum addiction - work in progress, has some scenes adjusted for it
    m "[hermione_name], today I have a very special potion that I would like you to drink."
    $ her_main("What does this one do?","body_07")
    m "As always, it's going to be a surprise."
    $ her_main("You're not going to try to transform me into a cat again are you [genie_name]?","body_07")
    $ her_main("","body_07")
    m "Of course not, now would you kindly drink the potion."
    $ her_main("...","body_12")
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">Hermione cautiously starts drinking the potion."
    $ her_main("","body_126")
    pause .5
    hide screen ch_potion
    with d3
    show screen hermione_blink
    $ her_main("This isn't a potion! This is just a bottle full of your cum!","body_30")
    $ her_main("Ughhh and it's cold as well.","body_43")
    m "So it just tastes like cum to you?"
    $ her_main("Of course it does, what else would it taste like?","body_47")
    ">Hermione starts unconsciously licking her lips."
    $ her_main("At least warn me next time you make me drink your cum [genie_name].","body_10")
    m "What do you mean next time?"
    $ her_main("Well you're such a pervert you'll probably try and do this again. At least warn me so it's not such a shock.","body_79")
    m "Ok, [hermione_name], I'll make sure to warn you next time."
    $ her_main("Is that all then [genie_name]?","body_69")
    m "Yes [hermione_name], 20 points to Gryffindor."
    $ her_main("Thank you [genie_name].","body_08")
    ">Hermione leaves the room with the remaining potion firmly in her grasp."    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ addicted = True
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_3_2: #Scene where Hermione comes back addicted to your cum (replace sucking noises with actual text)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    ">Hermione quickly enters your office."
    $ her_main("What the hell did you do to me?","body_32")
    m "Whatever are you talking about [hermione_name]?"
    $ her_main("Ughh, it doesn't matter, just let me suck it.","body_29")
    m "Why on earth would you want to do that? You're a top student, that doesn't sound appropriate."
    $ her_main("You know exactly what you did to me. Now let me suck your filthy old cock.","body_47")
    menu:
        "-Let her suck your dick-":
            m "Well if you insist [hermione_name]."
        "-Make her beg-":
            m "I don't think that you deserve to after calling it filthy and old."
            m "Perhaps if you asked nicely..."
            $ her_main("Fine. Please let me suck your dick [genie_name].","body_44")
            m "Hmmm, I don't think that was sincere enough."
            $ her_main("Please [genie_name], let me suck your big, thick dick. Pretty please.","body_34")
            m "Much better."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    $ h_c_u_pic = "hand_ani"
    show screen chair_02
    show screen g_c_u
    
    hide screen hermione_blink #Hermione stands still.
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    show screen ctc
    with fade
    pause
    show screen bld1
    with d3
    $ hermione_main_zorder = 8
    ">As soon as you remove your cock from your robe Hermione is on top of you."
    $ her_main("","body_66")
    $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_chibi_ypos = 10
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3      
    her "Do you have any idea how hard it was sitting \nthrough classes today?"
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3      
    her "*Slurp!* *Slurp!* *Slurp!*"    ###start sucking etc....
    $ her_main("","body_69")
    show screen h_c_u
    hide screen g_c_u
    with d3   
    her "Being this aroused."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gobble!* *Slurp!*"
    $ her_main("","body_68")
    show screen h_c_u
    hide screen g_c_u
    with d3   
    her "With no way to relieve myself."
    her "I tried everything."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Gobble!* *Slurp!* *Slurp!*"
    $ her_main("","body_64")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "I even masturbated in the girls bathroom."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    $ her_main("","body_79")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "But nothing worked."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gulp!* *Slurp!*"
    $ her_main("","body_78")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "All I could think about was the taste of your \nfilthy cum."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gulp!* *Gulp!*"
    m "My my, someone is becoming quite the slut wouldn't you say [hermione_name]"
    her "*Slurp!* *Gulp!* *Slurp!*"
    $ her_main("","body_65")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "You know why this is happening to me."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3  
    her "*Slurp!* *Slurp!* *Gulp!*"
    $ her_main("","body_64")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "Whatever was in that delicious potion you made \nme drink this morning."
    hide screen hermione_main
    m "Delicious? I thought you said it was just a bottle full of my cum?"
    m "Are you sure that you're just not a little slut who's become addicted to her Headmaster's semen?"
    $ her_main("I'm sure. There was something else in there.","body_122")
    hide screen hermione_main
    m "Whatever you say [hermione_name]. Now if you want your reward you better get back to work."
    $ her_main("","body_129")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "..."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Slurp!* *Gulp!*"
    ">She is incredibly enthusiastic. You can feel your load building."
    menu:
        "-Cum down her throat-":
            m "Here it comes slut."
            ">Hermione quickly swallows the majority of your shaft. You can feel the tip of your head pressed against the entrance to her throat."
            m "You'll have to do better than that if you want your reward [hermione_name]."
            ">You place your hands on the back of her head pull her head into you."
            $ her_main("{size=+7}!!!{/size}","body_32")
            hide screen hermione_main
            ">The sensation of entering her throat sends you over the edge."
            m "Better start swallowing slut!"
            ">You start pumping your thick load directly into her stomach."
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            ">Hermione's eyes widen and tears form as she senses your semen enter her."
            $ her_main("hhaanooo hhhheerrr","body_130")
            hide screen hermione_main
            ">Her hands shoot down into her pants as she starts violently orgasming."
            ">The sight of her pleasuring herself as you use her throat only prolongs your orgasm."
            m "You dirty little girl. Getting off from your headmaster sticking his cock down your throat."
            m "I bet your loving this, being used as a nothing more than a toy."
            ">She says nothing but quickens the pace of her masturbation."
            ">You finally pull out of keen mouth with a satisfactory pop."
            $ her_main("It won't stop!","body_132")
            hide screen hermione_main
            m "What won't?"
            $ her_main("I-I can't stop cumming [genie_name]...","body_117")
            hide screen hermione_main
            ">The stimulation proves too much and she passes out."
            
        "-Cum in her mouth-":
            m "This is it girl. Get ready."
            ">Hermione starts swirling her tongue and focusing on the tip of your shaft."
            m "That's done it slut. Start swallowing."
            ">You explode into her mouth."
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            $ her_main("mmmmmmm *gulp* *gulp*","body_125")
            hide screen hermione_main
            ">Hermiones eyes go blank as she starts swallowing down your load."
            m "That's it, swallow it down like a good girl. You earned your prize."
            $ her_main("*gulp* *gulp* *gulp* *gulp*","body_126")
            hide screen hermione_main
            ">As she swallows you notice her legs start to convulse as she starts to orgasm."
            $ her_main("*gulp* *gulp* *gulp* ","body_125")
            hide screen hermione_main
            ">You finally remove your shaft from her hungry mouth."
            m "Very good girl. Almost entirely clean... except for a bit of cum on the tip."
            m "I can't dirty my robes now can I? Better wipe this off."
            ">You wipe yourself clean on the tip of her nose."
            $ her_main("...","body_126")
            hide screen hermione_main
            m "There much better."
            ">Her legs have not stopped quivering since you first came."
            m "Well aren't you going to say anything [hermione_name]?"
            $ her_main("Thank you maste-","body_133")
            hide screen hermione_main
            ">She collapses into a heap on the ground with her legs still shaking."
        "-Cum on her face-":
            m "Get ready girl, here it comes."
            ">Hermione increases her efforts and starts focusing on the head of your penis."
            m "Not so quick [hermione_name]."
            show screen h_c_u
            hide screen g_c_u
            with d3 
            ">You quickly pull your penis out from her mouth."
            $ her_main("What are you doing [genie_name]?","body_48")
            hide screen hermione_main
            m "Giving you your well earned reward."
            $ g_c_u_pic = "cum_on_face_ani"
            hide screen h_c_u
            show screen g_c_u
            with d3 
            $ uni_sperm = True
            ">You start pumping your cock quickly and explode all over the young witch's face"
            m "Take it you filthy cum slut!"
            $ her_main("{size=+5}!!!{/size}","body_121")
            hide screen hermione_main
            ">Hermione immediately starts masturbating shamelessly in front of you."
            $ her_main("{size=+5}I'm cumming{/size}","body_117")
            hide screen hermione_main
            m "What was that [hermione_name]?"
            $ her_main("I-I'm cumming","body_130")
            hide screen hermione_main
            m "Just from a facial? What sort of cumslut have you become Miss Granger?"
            m "What would your parents think? Looking at you covered in some old mans cum."
            $ her_main("No. Please stop, I'll-","body_34")
            hide screen hermione_main
            m "They'd be ashamed at what you've become. A whore who gets off from being used as a toy."
            $ her_main("I-I'm cumming again [genie_name]. It won't stop...","body_32")
            hide screen hermione_main
            ">Hermione's voice trails off as she pass out from the over stimulation."
        "-Cum on the floor-":
            m "I'm cumming whore."
            $ her_main("mmmmmmmm","body_115")
            hide screen hermione_main
            ">She goes to bury her face into her crouch but you put your palm on her forehead and push her away."
            show screen h_c_u
            hide screen g_c_u
            with d3 
            $ her_main("[genie_name], what are you doing?","body_119")
            hide screen hermione_main
            m "giving you your reward"
            ">After a few quick pumps you point your dick at the floor and explode."
            $ her_main("PROFESSOR! Why would you waste that?","body_118")
            hide screen hermione_main
            m "It's not wasted [hermione_name], your reward is right there waiting for you."
            $ her_main("I'm not going to eat that. The floor in here is\n disgusting.","body_117")
            hide screen hermione_main
            m "Well you can always wait until tomorrow morning then."
            $ her_main("TOMORROW MORNING!? I can't wait that long. \nCan't you just cum again?","body_119")
            hide screen hermione_main
            m "No [hermione_name], I'm a tired old man and it's time for me to go to sleep."
            m "You can either eat off the floor or you can come back tomorrow."
            $ her_main("...Fine","body_120")
            hide screen hermione_main
            ">She begrudgingly starts scooping your cum off the floor with her fingers."
            menu:
                "-Watch her-":
                    $ her_main("","body_125")
                    ">She scoops up as much as she can into her palm \nand quickly moves it to her mouth."
                    pass
                "-Make her lick it up-":
                    m "Not with your fingers [hermione_name]."
                    $ her_main("What do you mean not with my fingers? How \nelse am I supposed to eat it?","body_117")
                    hide screen hermione_main
                    m "You have a perfectly good tongue, I suggest that you put it to use."
                    $ her_main("You expect me to LICK your old cum off the \nfloor?","body_118")
                    hide screen hermione_main
                    m "I do. Unless of course you would prefer to go back to your room hungry and unsatisfied."
                    $ her_main("...","body_117")
                    hide screen hermione_main
                    ">She bends over with her head to the floor."
                    $ aftersperm = True
                    $ her_main("(This is so degrading)","body_116")
                    hide screen hermione_main
                    ">She puts her tongue out licks your cum."
            ">The effect is instantaneous."
            $ aftersperm = True
            $ her_main("I-I'm cumming.","body_126") #small text
            hide screen hermione_main
            m "What was that?"
            $ her_main("I'm cumming!","body_133")
            hide screen hermione_main
            ">Hermione's hand shoots under her skirt as she starts violently orgasming."
            $ her_main("What's wrong with me [genie_name]?","body_134")
            hide screen hermione_main
            m "A lot of things [hermione_name], considering you just ate my cum off the ground."
            $ her_main("I can't stop cumming...","body_139")
            hide screen hermione_main
            ">Hermione loses conciousness."
    hide screen bld1
    hide screen hermione_main
    ">Hermione is in an unconscious heap on the floor."
    menu:
        "-Carry her back to her room as is-":   
            ">You pick her limp body up and carry her to her room."
            ">As you enter the dormitory you hear her talk in her sleep."
            $ her_main("Of course I swallow... just form a line...","body_131")
            hide screen hermione_main
            ">You place her carefully back into her bed."
            m "Sleep tight slut."
        "-Clean her up and take her back to her room-":   
            $ uni_sperm = False
            ">You pick her limp body up and carry her to her room."
            ">As you enter the dormitory you hear her mumble in her sleep."
            $ her_main("You want a kiss [genie_name]? Of course I don't mind...","body_127")
            hide screen hermione_main
            ">You place her carefully back into her bed."
            m "Sleep tight Hermione."
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    hide screen blkfade
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    $ addicted = False
    $ uni_sperm = False
    $ aftersperm = False
    with Dissolve(.3)
    $ hermione_main_zorder = 5
    $ hermione_sleeping = True
    hide screen hermione_main

    jump night_main_menu
        
label potion_scene_4: #Transparent uniform
    m "[hermione_name], I have another potion for you."
    $ her_main("I'm not sure that I like these potions [genie_name].","body_07")
    $ her_main("Especially after the time you tried to turn me into a cat.","body_09")
    m "To be fair I was trying to turn you into another girl..."
    $ her_main("That's not much better [genie_name].","body_05")
    m "Isn't it?"
    $ her_main("Well at least promise me that this one isn't going to embarrass me in the middle of class.","body_04")
    $ her_main("My reputation is suffering enough as it is. I don't need these constant potions causing me to transform in front of my peers.","body_12")
    m "I promise that this potion won't affect your body in any way."
    $ her_main("Well then what on earth is it going to do?","body_05")
    m "As always [hermione_name], you'll ha-"
    $ her_main("Have to wait and see. I know.","body_07")
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione quickly drinks the potion."      #new
    $ her_main("","body_04")
    hide screen ch_potion
    show screen hermione_blink
    her "Can I go now?"
    m "Yes you may. 20 points to Gryffindor"
    $ her_main("Thank you [genie_name].","body_16")
    
    $ gryffindor += 20
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_takes_classes = True
    if whoring <= 7:
        $ transparency = 0.8
    elif whoring <= 13:
        $ transparency = 0.6
    elif whoring <= 20:
        $ transparency = 0.4
    else:
        $ transparency = 0.2
    jump day_main_menu

label potion_scene_4_2: #Scene where Hermione comes back after classes angry and confused at having her uniform made transparent
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    if whoring <= 7: #Very angry and embarrassed
        ">Hermione bursts into your office."
        $ her_main("How could you [genie_name]!","body_22")
        $ her_main("I am the laughing stock of the entire school!","body_21")
        $ her_main("Now everyone knows what I look like naked!","body_20")
        m "Tell me about what happened."
        $ her_main("Tell you about what happened? I'm never speaking to you again.","body_21")
        $ mad += 20
        $ transparency = 1
    elif whoring <= 13: #Mildly aggravated
        ">Hermione comes into your office quickly without knocking."
        $ her_main("Again?","body_34")
        m "What's this about [hermione_name]?"
        $ her_main("Why would you make my clothes invisible again?","body_31")
        m "Why not?"
        $ her_main("Ugh, you're such a pig.","body_29")
        m "Tell me about what happened."
        $ her_main("...","body_33")
        $ her_main("Fine, but I expect an extra 10 points.","body_31")
        m "As you wish."
        $ her_main("Well I started off with potions class as usual when I started to feel like all eyes were on me.","body_66")
        m "I wonder why."
        $ her_main("As I was saying I was completing potions class and felt like everyone wouldn't take their eyes off of me.","body_69")
        $ her_main("I didn't think anything of it until I was approached by Professor Snape at the end of the lesson.","body_79")
        $ her_main("He normally criticises me during potions class. Stuff like getting dosages wrong, things that I know are correct.","body_29")
        m "Back to the story [hermione_name]."
        $ her_main("Well when he commented that he liked my outfit I was suspicious. I thought that perhaps he was talking about my shirt until I looked down and saw that everything was see through.","body_66")
        $ her_main("But I just ignored him, finished class and ran here.","body_69")
        m "You just finished class?"
        $ her_main("Of course, I can't afford to miss potions class. I'm doing poorly enough without missing class.","body_79")
        m "Well fair enough. You may go now."
        $ her_main("Hmmph. Goodbye [genie_name].","body_29")

    elif whoring <= 20: #Slightly aroused
        ">Hermione enters your office"
        $ her_main("Can you at least warn me next time?","body_08")
        m "Well, that'd take away from the suspense wouldn't it?"
        $ her_main("Hmmmm, well at least ask what I'm doing before you give me the potion.","body_10")
        m "Why, what did you have to do today that was so important?"
        $ her_main("I had to give a speech for languages!","body_28")
        $ her_main("Do you have any idea how inappropriate it was giving a speech on morality in front of the entire class-","body_16")
        $ her_main("{size=+5}As my clothes became transparent!{/size}","body_28")
        m "Well I imagine it depends on what side of morality you were arguing."
        $ her_main("It doesn't matter.","body_16")
        m "Are you sure that you didn't enjoy it?"
        $ her_main("How could I. I had to stand there as my friends and peers all saw me naked.","body_17")
        m "You finished your speech?"
        $ her_main("Certainly, I had to make sure that everyone knew my views on morality.","body_15")
        m "Well I'm sure they have a crystal clear view of it now."
        $ her_main("Hmmph, are you done?","body_12")
        m "Yes, you may go now."
        $ her_main("Good bye [genie_name].","body_02")
    else: #Highly aroused (doesn't even acknowledge that her clothes are see-through)
        ">Hermione enters the office casually."
        m "Hello [hermione_name], how was your day today?"
        $ her_main("Fine [genie_name]. Why do you ask?","body_06")
        m "No reason. Anything unusual happen today?"
        $ her_main("Hmmmm, now that you mention it I suppose that boys in class were a little more forward than usual.","body_10")
        m "How so?"
        $ her_main("Well nothing serious, just small stuff like calling me names, groping me.","body_13")
        m "Groping you? What on earth could have provoked them to do that?"
        $ her_main("I don't know [genie_name]. I can't imagine any reason that I would be attracting attention today...","body_45")
        m "You're getting off on this aren't you?"
        $ her_main("...","body_46")
        $ her_main("I've never been so turned on in my life. Having all eyes on me. Having every boy imagine doing unspeakable things to me.","body_121")
        $ her_main("Snape made me stand out the front of class after I talked back to him.","body_124")
        $ her_main("I think that I orgasmed just from the looks people gave me.","body_123")
        m "Well done [hermione_name]. You're becoming quite the slut."
        $ her_main("Thank you [genie_name]. Is that all?","body_128")
        m "Yes, you can go now slut."
        $ her_main("{image=textheart}","body_46")
    $ transparency = 1
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_sleeping = True
    jump night_main_menu
        
label potion_scene_5: #Lamia potion
    $ her_main("That's dumb.","body_32")
    m "I literally don't know."
    jump day_main_menu

label potion_scene_6: #Luna potion
    m "Might I offer you a drink?"
    $ her_main("You're not trying to get me drunk on Butterbeer again are you?","body_03")
    m "Nothing of the sort, just a harmless little potion."
    ">You hand her the potion bottle."
    $ her_main("Another of your mysterious potions?","body_08")
    her "Let me guess, you won't tell me what it does and I'll embarrass myself in front of the whole class?"
    m "Not at all."
    $ her_main("That's new.","body_17")
    her "... and somehow worrying"
    her "So what exactly is it then?"
    m "It's your regular, run-off-the-mill Polyjuice Potion."
    $ her_main("Ugh. Those taste like muck.","body_33")
    her "... and what'll it turn me into?"
    m "That, Miss Granger, is a secret."
    $ her_main("Typical.","body_23")
    m "It'll taste a lot sweeter if you imagine all the points you'll earn for Gryffindor."
    m "How much of a lead did Slytherin have on you again?"
    her "You're right [genie_name]. I can't let Gryffindor down!"
    ">She downs the thick potion."
    $ her_main("Blehgh.","body_43")
    her "I was wrong, not muck. Snot. It's as thick as Trollsnot."
    m "As long as you keep it down, you'll earn Gryffindor a great deal of points."
    her "And I will."
    $ her_main("So what now? I just go to class?","body_44")
    m "Not yet, tell me something about yourself."
    $ her_main("Well, ever since I started my \"Extracurricular activities\" with you my attendance and grades have started slipping.","body_16")
    m "Troubling indeed."

    if whoring <= 13:
        $ her_main("It is! [genie_name], I used to be at the top of the class. My scores were impeccable. ","body_30")
        m "And how are your scores now?"
        $ her_main("Well I'm still at the top... Just not by as much.","body_12")
        m "Well, there are times when academic excellence shouldn't be your primary concern."
        $ her_main("Hmmph, and what /should/ be my primary concern then?","body_17")
        m "Currently. I'd say your face is pretty high on the list"
        $ her_main("Excuse me. That is hardly appropriate for a headmaster.","body_35")
        m "No, I'm serious. You should really see the look on your face."

    else:
        $ her_main("Not really. I realize there are other things I can excel in.","body_06")
        m "Like sucking cocks for house-points"
        $ her_main("Professor!","body_30")
        m "Oh don't be so modest. If sucking dick was a class, you'd be Magna Cum Laude."
        $ her_main("Thank you professor. You know, there's time to earn some more points before class. If you're feeling generous I could...","body_30")
        m "I'd have to know on whose face I'll be cumming though "
        $ her_main("What do you mean? ...My face of course... I mean ...*urp*","body_30")
        m "Maybe you should check the mirror"
    "*POOF*"
    hide screen hermione_main
    hide screen hermione_blink
    $ luna_chibi("stand")
    $ changeLuna(1, 1, 4, 1)
    her "Ughhh... I feel like I'm going to throw up! Did the Polyjuice work??"
    m "Like a charm."
    ">Hermione starts examining herself, feeling out her outfit and pausing at her breasts." 
    $ changeLuna(5, 1, 5, 1)
    her "Apparently I'm still a girl. Someone from Ravenclaw?"
    m "Keen powers of observation, Miss Granger"
    ">Hermione grabs a lock of her hair"
    $ changeLuna(1, 7, 1, 4)
    her "Definitely a blonde, though she could absolutely use a comb"
    $ changeLuna(1, 5, 1, 1)
    ">Suddenly Hermione feels something stuck in the mess of blonde. On closer examination it appears to be a wand."
    $ changeLuna(4, 1, 3, 1)
    her "..."
    her "You turned me into Loony Lovegood... I mean Luna Lovegood!?!"
    m "Very astute [hermione_name]."
    m "(No idea who that is, but she looks good.)"
    $ changeLuna(4, 1, 3, 17)
    her "Why on earth would you want me to look like Luna? She's completely mental!"
    m "I'm not seeing anything really wrong with her."
    $ changeLuna(1, 1, 4, 4)
    her "She has... imaginary friends and believes in things that can't possibly exist [genie_name]. She is absolutely mad."
    m "Fortunately, I'm not really interested in her mental health. I am interested in her impressive, and quite real, chest."
    $ changeLuna(5, 1, 5, 3)
    her "You can't possibly be interested in that... that girl's paltry breasts."
    m "Currently they're yours. And they don't look so paltry from where I'm sitting [hermione_name]. Do I detect a hint of jealousy?"
    $ changeLuna(1, 1, 3, 3)
    her "Not at all, I suppose it is only natural that someone of your advanced age has trouble with their eyesight."
    m "(definitely struck a nerve there.) Is that any way to talk to your elders, [hermione_name]? Perhaps you need a good spanking to remind you of your manners. We old people are good at giving those."
    $ changeLuna(1, 1, 4, 9)
    her "I..I apologize [genie_name]. I don't know what came over me."
    m "Apology accepted. I'm sure they can't hold a candle to the brilliance of your boobs."
    $ changeLuna(1, 2, 1, 4)
    her "I'd like to think I'm more than just a pair of breasts... but thank you [genie_name]. That was flattering. In a way."
    m "If you want to dispel all doubt, we could compare. Why don't you lift your shirt and show me what you... err... She's got under that sweater."
    $ changeLuna(4, 2, 3, 4)
    her "I'm still not entirely comfortable with this..."
    ">Hermione quickly strips off her Ravenclaw top, followed by her bra."
    hide screen luna
    $ luna_chibi("stand_topless")
    $ luna_wear_top = False
    $ luna_wear_bra = False
    $ changeLuna(5, 2, 5, 3)
    her "There, see. Perfectly ordinary breasts. Absolutely no need to keep looking at them."
    m "I'm not quite convinced, the soft pale skin, the cute pink nipples and they look like quite a handful. I think you might have some serious competition here [hermione_name]."
    $ changeLuna(5, 1, 3, 17)
    her "You can't be serious! They're saggy and couldn't even fill a first-year's palm!"
    m "Hmmm, I'm not sure. I think a closer examination is required."
    ">In a huff, Hermione walks over and presents her new set of breasts"
    m "Yes yes, upon closer inspection it seems I was wrong. Luna's breasts are indeed second to your own."
    $ changeLuna(5, 1, 3, 4)
    her "I'm glad you came to your senses. Thank you, If you're completely satisfied, I'll cover these hideous things up now."
    m "Completely [hermione_name]. 20 points to Gryffindor."
    hide screen luna
    $ luna_chibi("stand")
    $ luna_wear_top = True
    $ luna_wear_bra = True
    $ changeLuna(3, 1, 1, 1)
    her "Well I best be off to classes."
    m "You're going to class looking like a fellow classmate?"
    $ changeLuna(1, 1, 5, 1)
    her "It's not going to be a problem. Luna's barely in class as it is, I can just pretend to be her. Maybe I'll even improve her test scores. You'll notify the teachers I can't attend class right?"
    m "Absolutely. (Not a chance.) But, what if you bump into her in the halls?"
    $ changeLuna(5, 1, 1, 4)
    her "Believe me [genie_name], Luna will probably think I'm some kind of Wrackspurt that's messing with her head."
    hide screen bld1
    hide screen blkfade
    hide screen luna
    $ menu_x = 0.5 
    $ hermione_takes_classes = True
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen luna_chibi
    with d3
    $ luna_known = True
    jump day_main_menu
    
label potion_scene_7: #hyper sensitivity potion
    m "I'd like you to drink a potion today."
    her "Alright then."
    m "Just like that? No putting up a fight or demanding to know what it is?"
    her "Would you tell me what it is?"
    m "No, probably not."
    her "Then why ask?"
    m "Fair enough, here it is."
    menu:
        "-Drop it on her chest-":
            jump potion_scene_7_1
        "-Hand it to her-":
            jump potion_scene_7_2
        "-Drop it on her skirt-":
            jump potion_scene_7_3

label potion_scene_7_1: #Hyper sensitive breasts
    ">You fumble with the potion, spilling it over Hermione's front, soaking her shirt through."
    her "Professor! What were you thinking?"
    ">You place the still half full bottle back on your desk in front of you."
    m "It was an accident, my hands aren't what they once were."
    her "Ughhh, now I'm going to have to go change before classes."
    her "I expect to be compensated accordingly."
    m "Ok, ok. How about I give you a nice massage to calm you down."
    her "A massage? That's hardly fair compensation!"
    m "Are you sure?"
    her "Positive."
    m "Ok, I'll make a bet with you then."
    her "...{p}Go on..."
    m "I'll start massaging you. If you don't like it after two minutes then you can tell me to stop."
    her "And what do I get for telling you to stop?"
    m "two hundred points."
    her "two hundred points!"
    m "But if you don't ask me to stop I get to massage you for as long as I like, wherever I like."
    her "Deal."
    m "Are you sure?"
    her "No offense [genie_name], but I think I can resist a massage for 200 points."
    m "you sound confident. Care to raise the stakes?"
    her "Are you saying that I can earn more than 200 points?"
    m "five hundred."
    her "{size=+10}Five HUNDRED!{/size}" #size up
    her "Deal."
    m "I haven't even told you what happens if you lose."
    her "it doesn't matter, For 500 points I would turn down a massage from Viktor Krum himself."
    m "Well for the sake of the bet I'll explain anyway."
    m "I expect you to strip naked if you want to be massaged after your two minutes are up."
    her "Naked!"
    m "Only if you lose."
    her "Well I suppose that's ok then, it's not like I'll have to do it."
    m "well are you ready?"
    her "Yes, let's make it quick. I have to go back to the dorms and change after this. My shirt is soaked through."
    ">Hermione walks over and stands in front of you."
    her "So what's your plan? Do you expect me to give in just because you rub my shoulders?"
    m "Shoulders? Who said anything about shoulders?"
    her "Are you going to grope my butt again?"
    m "No, no. Today we're sticking with the fundamentals."
    ">You grab her breasts through her soaked shirt."
    her "!!!"
    m "There we are. I'll start the time now shall I?"
    her "What is wrong with me?"
    m "Nothing, apart from underestimating your elders."
    her "My breasts... they're on fire."
    m "If they were I think I would know."
    ">You gently roll her nipples between your thumbs and forefingers."
    her "Please [genie_name], you have to stop."
    m "You're not allowed to ask me to stop until the two minutes are up."
    m "And by my count there's still over a minute and a half to go."
    ">You kneed her breasts firmly."
    her "I'm calling off the bet..."
    m "Now now, no one likes a quiter."
    her "This isn't a joke, it feels like..."
    her "It feels amazing..."
    m "I told you I'm good."
    her "No [genie_name], this is the best thing I've ever felt."
    her ""
    
label potion_scene_7_2: #Hyper sensitive mouth/throat
    
label potion_scene_7_3: #Hyper sensitive pussy
    
    
    
    
