GRADESCOPE = "1st-Order Logic Exercises"

HEADER = """
<H2> Introductory First-Order Logic Exercises for Prover9 </H2>
This is a set of formative exercises designed to teach
you the skills of encoding problems into first-order logic
representation and solving them using an automated
theorem prover. 
"""

## If PROBLEM_SET not defined, will use all in PROBLEMS
XPROBLEM_SET = [  'barbara',
                 'celarent',
                 'ferio',
                 'baroco',
                 'greedy_rabbits',
                 'young_rabbits']

PROBLEMS = {


  "barbara" : {
       "title"   : "A Famous Syllogism",
       "attribution" : """A very well known example of a syllogism, 
                          probably first presented by <b>John Stewart Mill</b>""",
       "logic" : "first-order logic",
       "English" : [ "All Greeks are men.",
                  "All men are mortal.",
                  "All Greeks are mortal."
                  ],
       
       "vocabulary" : {"Predicates": 
                      ["Greek", "Man",
                       "Mortal"
                       ]},
      
       "solution"   : ["all x (Greek(x) -> Man(x))",
                    "all x (Man(x) -> Mortal(x))",
                    "all x (Greek(x) -> Mortal(x))"],
      
      },

  "celarent" : {
       "title"   : "Furry Reptiles",
       "attribution" : "A logic problem by <b>Brandon Bennett</b>",
       "logic" : "first-order logic",
       "English" : [ "No reptiles have fur.",
                  "All snakes are reptiles.",
                  "No snakes have fur."
                  ],
       
       "vocabulary" : {"Predicates": 
                      ["Reptile", "HasFur",
                       "Snake"
                       ]},
      
       "solution"   : ["all x (Reptile(x) -> -HasFur(x))",
                    "all x (Snake(x) -> Reptile(x))",
                    "all x (Snake(x) -> -HasFur(x))"],
      
      },

    "ferio" : {
         "title"   : "Homework is Fun",
         "attribution" : "A logic problem by <b>Brandon Bennett</b>",
         "logic" : "first-order logic",
         "English" : [ "No homework is fun.",
                    "Some reading is homework.",
                    "Some reading is not fun."
                    ],
         
         "vocabulary" : {"Predicates": 
                        ["Homework", "Fun",
                         "Reading"
                         ]},
        
         "solution"   : ["all x (Homework(x) -> -Fun(x))",
                      "exists x (Reading(x) & Homework(x))",
                      "exists x (Reading(x) & -Fun(x))"],
        
        },
    
    "baroco" : {
         "title"   : "Web sites",
         "attribution" : "A logic problem by <b>Brandon Bennett</b>",
         "logic" : "first-order logic",
         "English" : [ "All informative things are useful.",
                    "Some web sites are not useful.",
                    "Some web sites are not informative."
                    ],
         
         "vocabulary" : {"Predicates": 
                        ["Informative", "Useful",
                         "Website"
                         ]},
        
         "solution"   : ["all x (Informative(x) -> Useful(x))",
                      "exists x (Website(x) & -Useful(x))",
                      "exists x (Website(x) & -Informative(x))"],
        
        },
  "greedy_rabbits" : {
           "title"   : "Greedy Rabbits",
           "attribution" : "A logic problem by <b>Brandon Bennett</b>",
           "logic" : "first-order logic",
           "English" : [ "No old rabbits are greedy.",
                      "All black rabbits are greedy.",
                      "No old rabbits are black."
                      ],
           
           "vocabulary" : {"Predicates": 
                          ["Rabbit", "Old",
                           "Greedy", "Black"
                           ]},
          
           "solution"   : ["all x ((Rabbit(x) & Old(x)) -> -Greedy(x))",
                        "all x ((Rabbit(x) & Black(x)) -> Greedy(x))",
                        "all x ((Rabbit(x) & Old(x)) -> -Black(x))"],
          
          },
  "young_rabbits" : {
             "title"   : "Young Rabbits",
             "attribution" : "A logic problem by <b>Brandon Bennett</b>",
             "logic" : "first-order logic",
             "English" : [ "Young rabbits are greedy.",
                        "Greedy animals are fat.",
                        "Rabbits are animals.",
                        "All young rabbits are fat."
                        ],
             
             "vocabulary" : {"Predicates": 
                            ["Young","Rabbit", "Fat",
                             "Greedy", "Animal"
                             ]},
            
             "solution"   : ["all x ((Rabbit(x) & Young(x)) -> Greedy(x))",
                          "all x ((Animal(x) & Greedy(x)) -> Fat(x))",
                          "all x (Rabbit(x) -> Animal(x))",
                          "all x ((Rabbit(x) & Young(x)) -> Fat(x))"],
            
            },

    "invalid_syllogism" : {
       "title"   : "An Invalid Syllogism",
       "attribution" : "A logic problem by <b>Brandon Bennett</b>",
       "logic" : "first-order logic",
       "English" : [ "Some rhombuses are equilateral.",
                  "Some equilaterals are triangular.",
                  "Some rhombuses are triangular."
                  ],
       
       "vocabulary" : {"Predicates": 
                      ["Rhombus", "Equilateral",
                       "Triangular"
                       ]},
      
       "solution"   : ["exists x (Rhombus(x) & Equilateral(x))",
                    "exists x (Equilateral(x) & Triangular(x))",
                    "exists x (Rhombus(x) & Triangular(x))"],
      "notes": [ """ This is an example of a syllogism which is <b>not valid </b>. Try proving it and see what happens.
                 """ ]
      
      },

    "socrates" : {
             "title"   : "Socrates",
             "attribution" : "A logic problem by <b>Brandon Bennett</b>",
             "logic" : "first-order logic",
             "English" : [ "Socrates is Greek.",
                        "All Greeks are men.",
                    "All men are mortal.",
"Socrates is mortal."
                        ],
             
             "vocabulary" : {"Predicates": 
                            ["Greek","Man", "Mortal"
                             ], "Constants":["Socrates"]},
            
             "solution"   : ["Greek(Socrates)",
                          "all x (Greek(x) -> Man(x))",
                          "all x (Man(x) -> Mortal(x))",
                          "Mortal(Socrates)"],
            
            },

    "porky" : {
             "title"   : "Porky",
             "attribution" : "A logic problem by <b>Brandon Bennett</b>",
             "logic" : "first-order logic",
             "English" : [ "Porky is a pig.",
                        "Pigs are animals.",
                    "All pigs are fat.",
"No fat animals run fast.",
"Porky does not run fast."
                        ],
             
             "vocabulary" : {"Predicates": 
                            ["Pig","Animal", "Fat", "Fast"
                             ], "Constants":["Porky"]},
            
             "solution"   : ["Pig(Porky)",
                          "all x (Pig(x) -> Animal(x))",
                          "all x (Pig(x) -> Fat(x))",
                          "all x ((Fat(x) & Animal(x)) -> -Fast(x))","-Fast(Porky)"],
            
            },

            "jabberwock" : {
             "title"   : "Jabberwock",
             "attribution" : "A logic problem by <b>Brandon Bennett</b>",
             "logic" : "first-order logic",
             "English" : [ "The Jabberwock is a creature with eyes of flame.",
                        "All creatures with eyes of flame whiffle and burble.",
                    "All creatures that whiffle or burble have claws.",
"The Jabberwock has claws."
                        ],
             
             "vocabulary" : {"Predicates": 
                            ["FlameyEyes","Creature", "Whiffle", "Burble", "HasClaws"
                             ], "Constants":["Jabberwock"]},
            
             "solution"   : ["FlameyEyes(Jabberwock) & Creature(Jabberwock)",
                          "all x ((Creature(x) & FlameyEyes(x)) -> (Whiffle(x) & Burble(x)))",
                          "all x ( (Creature(x)  & (Whiffle(x) | Burble(x))) -> HasClaws(x))",
                          "HasClaws(Jabberwock)"],
            
            },

"ballooning_pigs" : {
       "title"   : "Balloonig Pigs",
       "attribution" : """This exercise is based on a problem set by Lewis Carroll
(Author of Alice in Wonderland) in his book Symbolic Logic.""",
       "logic" : "first-order logic",
       "English" : [ "All, who neither dance on tightropes nor eat penny-buns, are old.",
                  "Pigs, that are liable to giddiness, are treated with respect.",
                  "A wise balloonist takes an umbrella with him.",
                  "No one ought to lunch in public who looks ridiculous and eats penny-buns.",
                  "Young creatures, who go up in balloons, are liable to giddiness.",
                  "Fat creatures, who look ridiculous, may lunch in public, provided that they do not dance on tightropes.",
                  "No wise creatures dance on tightropes, if liable to giddiness.",
                  "A pig looks ridiculous, carrying an umbrella.",
                  "All, who do not dance on tightropes, and who are treated with respect are fat.",
                  "No one is young and old at the same time.",
                  "No wise young pigs go up in balloons."
                  ],
       
       "vocabulary" : {"Predicates": 
                      ["Dance_on_Tightropes", "Eat_Penny_Buns",
                       "Old", "Pig", "Giddy", "Respected",
                       "Wise", "Balloonist", "Takes_Umbrella",
                       "Ridiculous", "Lunch_in_Public", "Young",
                       "Fat", "Old"
                       ]},
      
       "solution"   : ["(all x (-(Dance_on_Tightropes(x) | Eat_Penny_Buns(x)) -> Old(x)) )",
                    "(all x ( (Pig(x) & Giddy(x)) -> Respected(x) ))",
                    "(all x ( (Wise(x) & Balloonist(x)) -> Takes_Umbrella(x) ) ) ",
                    "(all x ( (Ridiculous(x) & Eat_Penny_Buns(x)) -> -Lunch_in_Public(x) ) )",
                    "(all x ( (Young(x) & Balloonist(x)) -> Giddy(x) ) )",
                    "(all x ( (Fat(x) & Ridiculous(x) & -Dance_on_Tightropes(x)) -> Lunch_in_Public(x) ) )",
                    "(all x ( (Wise(x) & Giddy(x)) -> -Dance_on_Tightropes(x)))",
                    "(all x ( (Pig(x) & Takes_Umbrella(x)) -> Ridiculous(x)) )",
                    "(all x ( (-Dance_on_Tightropes(x) & Respected(x)) -> Fat(x)) )",
                    "(all x ( -(Young(x) & Old(x)) ) )",
                    "-(exists x (Wise(x) & Young(x) & Pig(x) & Balloonist(x) ))"],
      
      }
  
}
