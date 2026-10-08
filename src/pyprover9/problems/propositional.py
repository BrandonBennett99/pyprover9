
GRADESCOPE = "Propositional Logic Exercises"

HEADER = """
<H2>Propositional Logic Exercises for Prover9</H2>
This is a set of formative exercises designed to teach
you the skills of encoding problems into propositional logic
representation and solving them using an automated
theorem prover. 
<p>
Note that what is called <i>propositional logic</i>
is a logical language that only has propositional
letter symbols (representing atomic statements
that are either true or false) and truth-functional
connectives.  
"""

## If PROBLEM_SET not defined, will use all in PROBLEMS
xxPROBLEM_SET = [ 'diamond',
                 'lost_key',
                 'rembrandt',
                 'sundays',
                 'tarquin',
                 'tennis' ]

PROBLEMS = {


	"diamond" : {
    
	    "title" : "The Stolen Diamond",
	    "attribution" : "A logic problem by <b>Brandon Bennett</b>",
	    "logic" : "propositional logic",
	    "English" : [
	       "The diamond has been stolen!",
	       "If the diamond has been stolen, a thief got into the house.",
	       "If a thief got in, either the door was open or the window was smashed.",
	       "The window is not smashed.",
	       "The door was open." ],
	    
	    "vocabulary" : { "Propositional Constants":
	                    [ "DiamondStolen", "ThiefInHouse",
	                        "DoorOpen", "WindowSmashed"]
	                   }, 
	    
	    "solution" : ["DiamondStolen",
	                 "DiamondStolen -> ThiefInHouse",
	                 "ThiefInHouse-> (DoorOpen | WindowSmashed)",
	                 "-WindowSmashed",
	                 "DoorOpen"
	                ],
	    
	    "notes": [ """
	               <b>A4</b> is in the present tense, whereas the other
	               assumptions are in the past tense. We cannot easily
	               represent tenses in propositional logic.
	               Does this matter?
	               """ ]
    
    },
  
	"lost_key" : {
       "title"   : "The Lost Key",
       "attribution" : "A logic problem by <b>Brandon Bennett</b>",
       "logic" : "propositional logic",
       "English" : [ "If Alan did not lock the door he either forgot or lost the key.",
                     "If he lost the key he will be in trouble.",
                     "If he has a good memory he did not forget.",
                     "Alan has a good memory.",
                     "Either Alan locked the door or he will be in trouble."],
       
       "vocabulary" : {"Propositional Constants": 
                      ["AlanLockedDoor", "AlanForgotKey",
                       "AlanLostKey", "AlanInTrouble", "AlanGoodMemory",
                       ]},
      
       "solution"   : ["-AlanLockedDoor -> (AlanForgotKey | AlanLostKey)", 
                    "AlanLostKey -> AlanInTrouble",
                    "AlanGoodMemory -> -AlanForgotKey",
                    "AlanGoodMemory",
                    "AlanLockedDoor | AlanInTrouble"],
      
      },

  "rembrandt" : {
       "title"   : "Rembrandt's Picture",
       "attribution" : "A logic problem by <b>Brandon Bennett</b>",
       "logic" : "propositional logic",
       "English" : [ "Either the picture is valuable or it is a fake.",
                     "If it is valuable it is by Rembrandt.",
                     "If it is a fake there will be a police investigation.",
                     "Either the picture is by Rembrandt or there will be a police investigation."],
       
       "vocabulary" : {"Propositional Constants": 
                      ["PictureIsValuable", "PictureIsFake",
                       "PictureByRembrandt", "PoliceInvestigation",
                       ]},
      
       "solution"   : ["PictureIsValuable | PictureIsFake", 
                    "PictureIsValuable -> PictureByRembrandt",
                    "PictureIsFake -> PoliceInvestigation",
                    "PictureByRembrandt | PoliceInvestigation"],
      
      },

  "sundays" : {
       "title"   : "Sunday is a Holiday",
       "attribution" : "A logic problem by <b>Brandon Bennett</b>",
       "logic" : "propositional logic",
       "English" : [ "Sunday is a Holiday.",
                  "Saturday and Sunday is the weekend.",
                  "On holidays the University is closed.",
                  "It is the weekend.",
                  "It is not Saturday.",
                  "The University is closed."],
       
       "vocabulary" : {"Propositional Constants": 
                      ["Sunday","Holiday", "Saturday", "Weekend",
                       "UniversityClosed"
                       ]},
      
       "solution"   : ["Sunday -> Holiday", 
                    "(Saturday | Sunday) <-> Weekend",
                    "Holiday -> UniversityClosed",
                    "Weekend",
                    "-Saturday",
                    "UniversityClosed"],
      
      
      "notes": [ """
             Note that in some contexts we can translate names of days or time periods into
propositions. Thus, sometimes 'Saturday' can be translated as a proposition,
i.e. as 'It is Saturday'. If we were using first-order logic we would probably treat
'Saturday' and 'Sunday' as constants and 'weekend' and 'holiday' as predicates, but for this
problem you need to consider all of them as propositions which can be true or false
at a given time.
             """ ]
      },

  "tarquin" : {
       "title"   : "Tarquin's Wisdom",
       "attribution" : "A logic problem by <b>Brandon Bennett</b>",
       "logic" : "propositional logic",
       "English" : [ "If Tarquin learns philosophy then he acquires wisdom and if he learns science he will advance human knowledge.",
                     "If he acquires wisdom, Tarquin will not die in misery.",
                     "If he advances human knowledge, his aspirations will be satisfied.",
                     "If Tarquin's aspirations are not satisfied he will die in misery.",
                     "Alas, Tarquin's aspirations will never be satisfied",
                     "Thus, he learns neither philosophy nor science"],
       
       "vocabulary" : {"Propositional Constants": 
                      ["TarquinLearnsPhilosophy", "TarquinAcquiresWisdom",
                       "TarquinLearnsScience", "TarquinAdvancesKnowledge",
                       "TarquinDiesMisery", "TarquinSatisfiesAspirations"
                       ]},
      
       "solution"   : ["""(TarquinLearnsPhilosophy -> TarquinAcquiresWisdom) 
                        & (TarquinLearnsScience -> TarquinAdvancesKnowledge)""", 
                    "TarquinAcquiresWisdom -> -TarquinDiesMisery",
                    "TarquinAdvancesKnowledge -> TarquinSatisfiesAspirations",
                    "-TarquinSatisfiesAspirations -> TarquinDiesMisery",
                    "-TarquinSatisfiesAspirations",
                    "-TarquinLearnsPhilosophy & -TarquinLearnsScience"],
      
      },

 "tennis" : { "title" : "The Tennis Lover",
              "attribution": """Stolen from an anonymous worksheet, posted on the web at 
                                University of California Irvine, which says that it
                                comes from an advert for a tennis magazine.""",
              "logic" : "propositional logic",

              "outline" : """This problem is a bit different from most of the others ones.
                             Rather than being given a specific goal, you need to find an
                             appropriate goal, which both answers the question and is
                             provable from the assumptions.
                             You should try possible goals one at a time, until you find
                             one that is provable. 
                             Alternatively, you could work out the goal by your own
                             reasoning and then check it using Prover9.
                             Of course, if you have represented the other sentences
                             incorrectly, the correct goal may not be provable, and possibly
                             a different goal could be provable. So you
                             may need to check and alter the other formulae to get 
                             a proof of the correct goal. """,

              "English" : [ "If I'm not playing tennis, I'm watching tennis.",
                            "If I'm not watching tennis, I'm reading about tennis.",
                            "I cannot do more than one tennis-related activity at the same time. *",
                            "What am I doing? **",
                          ],
              "vocabulary" : { "Propositional Constants":
                               ["Playing", "Watching", "Reading"]
                             },
              "solution": [ "-Playing -> Watching",
                            "-Watching -> Reading",
                            "-( (Playing & Watching) | (Playing & Reading) | (Watching & Reading))",
                            "Watching"
                          ], 

              "notes" : [ """* You need to find a propositional formula involving the 3 tennis
                             activity propopositions which is true if only one or none of these
                             is true""",
                          """** Try each of the activies to find the one that can be proved
                                to be true. <i>Do not put several different goals in together.</i>
                                Although, Prover9 does allow multiple formulae in the goal section,
                                this will not give the proof of a specific answer that we want."""
                        ]
           },

"appointment" : {
       "title"   : "An Appointment",
       "attribution" : "A logic problem by <b>Adam Richard-Bollans</b>",
       "logic" : "propositional logic",
       "English" : [ "If Alba is not late to her appointment, the optician will be happy.",
                     "Alba is early to her appointment.",
                     "If Alba is early then Alba is not late.",
                     "The optician is happy."],
       
       "vocabulary" : {"Propositional Constants": 
                      ["AlbaLate", "OpticianHappy",
                       "AlbaEarly"
                       ]},
      
       "solution"   : ["-AlbaLate -> OpticianHappy", 
                    "AlbaEarly",
                    "AlbaEarly -> -AlbaLate",
                    "OpticianHappy"],
        "notes": [ """
                 <b>A3</b> encodes part of the relationship between the meaning of `early' and `late'.
                 If we simply remove this statement, Prover9 won't find a proof as it doesn't know what `early' or `late' mean.
                 """ ]
      
      },

    "dry_thunder" : {
       "title"   : "Dry Thunder",
       "attribution" : "A logic problem by <b>Adam Richard-Bollans</b>",
       "logic" : "propositional logic",
       "English" : [ "A Dry Thunderstorm is defined by the occurence of lightning without rain.",
                     "There is a dry thunderstorm.",
                     "If there is lightning then it is either raining or its hot.",
                     "It is hot."],
       
       "vocabulary" : {"Propositional Constants": 
                      ["DryThunder", "Lightning",
                       "Raining", "Hot"
                       ]},
      
       "solution"   : ["DryThunder <-> (-Raining & Lightning)", 
                    "DryThunder",
                    "Lightning -> (Raining|Hot)",
                    "Hot"],
      
      },

    "dragons" : {
       "title"   : "Angry Dragons",
       "attribution" : "A logic problem by <b>Adam Richard-Bollans</b>",
       "logic" : "propositional logic",
       "English" : [ "If the dragon destroys the village, the villagers will be homeless unless they take the King's Castle.",
                     "If the King is mean then the villagers will take the castle.",
                     "If the King is not mean then the dragon won't destroy the village.",
                     "The dragon destroys the village.",
                     "The villagers are not homeless."],
       
       "vocabulary" : {"Propositional Constants": 
                      ["DragonDestroysVillage", "VillagersTakeCastle",
                       "VillagersHomeless", "KingMean"
                       ]},
      
       "solution"   : ["DragonDestroysVillage -> ((-VillagersTakeCastle -> VillagersHomeless) & (VillagersTakeCastle -> -VillagersHomeless))", 
                    "KingMean -> VillagersTakeCastle",
                    "-KingMean -> -DragonDestroysVillage",
                    "DragonDestroysVillage",
                    "-VillagersHomeless"],
        "notes": [ """
                 In <b>A1</b> there may be multiple ways to interpret `unless'. If the villagers take the castle will they be homeless?
                 You may have arrived at a different solution and this problem highlights some of the challenges of translating natural language to formal logic.""" ]
      
      },
}
