 
GRADESCOPE = "Challenging Logic Exercises"

HEADER = """
<H2> Challenging Logic Exercises for Prover9</H2>

This is a set of more challenging problems that is intended
to sharpen your analytic skills and deepen your understanding
of   first-order logic representations and proofs. 
"""

## If PROBLEM_SET not defined, will use all in PROBLEMS
PROBLEM_SET = [  'parts_and_overlaps',
                 'honey_crumpets', 'impostor']

PROBLEMS = {
	"impostor" : {
		"title": "Impostors on a ship",
		"attribution" : "A logic problem by <b>Adam Richard-Bollans</b>",
		"logic" : "first-order logic",
		"English" : [
	       "Blue,Red,Yellow, Purple and a Janitor are crewmembers on a ship and are the only crewmembers.",
	       "There are two crewmembers who are impostors.",
	       "There are no more than two impostors.",
	       "If somebody accuses someone then the accused is an impostor or the accuser is the impostor.",
	       "If somebody is known to be an impostor, then they are an impostor.",
	       "Impostors know they are impostors.",
	       "If someone is murdered then they are not an impostor.",
	       "Purple knows one of the impostors.",
	       "Purple doesn't know that the Janitor or Blue are an impostor.",
	       "Purple was found murdered.",
	       "Neither Red or Blue are the Janitor.",
	       "Blue accused Yellow.",
	       "Nobody knows that Yellow is an impostor.",
	       "Yellow, Purple and the Janitor are not impostors and Blue and Red are impostors."
	       ],

	    "vocabulary" : {"Constants": ["Blue", "Red", "Yellow", "Purple", "Janitor" ],

                       "Predicates": 
                      ["Crewmember", "Impostor", 
                       "Murdered"
                       ],

                       "Relations": 
                      [ "Accused", "KnowsImpostor"
                      ],
                   }, 
	    
	    "solution" : [ "Crewmember(Blue) & Crewmember(Red) & Crewmember(Yellow) & Crewmember(Purple) & Crewmember(Janitor) & all x (Crewmember(x) -> (x=Blue | x=Red | x=Janitor | x=Yellow | x = Purple))",
	    		   "exists x exists y(Impostor(x) & Crewmember(x) & Impostor(y) & Crewmember(y) & -(x=y))",
	    		   "-(exists x exists y exists z ( -(x=y) & -(x=z) & -(y=z) & Impostor(x) & Impostor(y) & Impostor(z) ) )",
	    		    "all x all y(Accused(x,y) -> (Impostor(x) | Impostor(y)))",
	    		    "all x all y (KnowsImpostor(x,y) -> Impostor(y))",
	    		    "all x (Impostor(x) -> KnowsImpostor(x,x))",
	    		    "all x (Murdered(x) -> -Impostor(x))",
	    		    "exists x (KnowsImpostor(Purple,x))",
	    		    "-KnowsImpostor(Purple,Janitor) & -KnowsImpostor(Purple,Blue)",
	    		    "Murdered(Purple)",
	    		    "-(Janitor = Blue) & -(Janitor = Red)",
	    		    "Accused(Blue,Yellow)",
	    		    "-(exists x KnowsImpostor(x,Yellow))",
	    		    "-Impostor(Yellow) & -Impostor(Janitor) & -Impostor(Purple) & Impostor(Blue) & Impostor(Red)"
	                ],
	    
#	    "outline": "",

	    # "notes": [ ,
      # ]
	},

	"parts_and_overlaps" : {
		"title": "Parts and Overlaps",
		"attribution" : "A logic problem by <b>Adam Richard-Bollans</b>",
		"logic" : "first-order logic",
		"English" : [
	       "An axiom for Contact: Contact is reflexive.",
	       "Definition of Parthood: A region, A, is part of a region, B,  if and only if whenever a region, C, is in contact with A then it is in contact with B.",
	       "Definition of Proper Parthood: A region A is a proper part of a region B if and only if A is part of B but B is not part of A.",
	       "Definition of Overlap: A region A overlaps a region B if and only if there is a region which is part of both region A and B.",
	       "If any region A is a proper part of any region B then A overlaps B and A is in contact with B."
	       ],

	    "vocabulary" : { "Predicates":["Contact", "PartOf", "ProperPartOf", "Overlaps"]
	                    
	                   }, 
	    
	    "solution" : [ "all x (Contact(x,x))",
	    		   "all x all y ( PartOf(x,y) <-> (all z (Contact(z,x) -> Contact(z,y)) ))",
	    		   "all x all y ( ProperPartOf(x,y) <-> (PartOf(x,y) & -PartOf(y,x)))",
	    		    "all x all y ( Overlaps(x,y) <-> exists z (PartOf(z,x) & PartOf(z,y)))",
	    		    "all x all y ( ProperPartOf(x,y) -> (Overlaps(x,y) & Contact(x,y)))"
	                ],
	    
#	    "outline": "",

	    "notes": [ "A1: A relationship is <b>reflexive</b> when it relates elements to themselves. For example = is reflexive as x = x for all x.",
      "The domain is regular regions in space. For those interested in further exploring logical representations of space see Cohn, A. G., Bennett, B., Gooday, J., & Gotts, N. M. (1997). Qualitative spatial representation and reasoning with the region connection calculus. GeoInformatica, 1(3), 275–316." ]
	},

	"honey_crumpets" : {
		"title": "Honey Crumpets",
		"attribution" : "A logic problem by <b>Brandon Bennett</b>",
		"logic" : "first-order logic",
		"English" : [
	       "All crumpets have butter or honey on them.",
	       "No crumpet has both honey and butter.",
	       "There are exactly two honey crumpets.",
	       #"There are not three different crumpets with honey on them.",
	       "There are exactly two buttered crumpets.",
	       #"There are not three different crumpets with butter on them.",
	       "Any two different crumpets are either next to each other or diagonally opposite.",
	       "No two crumpets are next to each other and diagonally opposite.",
	       "No crumpet is next to itself.",
	       "No crumpet is diagonally opposite itself",
	       "If any crumpet A is next to any crumpet B then B is also next to A.",
	       "If any crumpet A is diagonally opposite any crumpet B then B is also diagonally opposite A.",
	       "Every crumpet is diagonally opposite another crumpet.",
	       "Every crumpet is next to two different crumpets.",
	       "There are two honey crumpets which are next to each other.",
	       "If a crumpet A is diagonally opposite another crumpet B, and B is diagonally opposite another crumpet C, then A is C.",
	       "I ate two diagonally opposite crumpets.",
	       "I ate a honey crumpet."],

	    "vocabulary" : { "Predicates": ["Honey", "Butter", "NextTo", "Diagonal",
	    "Ate"]
	                    
	                   },
	    
	    "solution" : ["all x (Honey(x) | Butter(x))",
	    "- (exists x (Honey(x) & Butter(x)))",
	    "exists x exists y ( -(x=y) & Honey(x) & Honey(y)) & " +
	    "-(exists x exists y exists z ( -(x=y) & -(x=z) & -(y=z) & Honey(x) & Honey(y) & Honey(z) ) )",
	    "exists x exists y ( -(x=y) & Butter(x) & Butter(y)) & " +
	    "-(exists x exists y exists z ( -(x=y) & -(x=z) & -(y=z) & Butter(x) & Butter(y) & Butter(z) ) )",
	    "all x all y ( -(x=y) -> (NextTo(x,y) | Diagonal(x,y)) )",
	    "- (exists x exists y (NextTo(x,y) & Diagonal(x,y)) )",
	    "all x -(NextTo(x,x))",
	    "all x -(Diagonal(x,x))",
	    "all x all y (NextTo(x,y) -> NextTo(y,x))",
	    "all x all y (Diagonal(x,y) -> Diagonal(y,x))",
	    "all x exists y (Diagonal(x,y) & -(x=y) )",
	    "all x exists y exists z ( -(y=z) & NextTo(x,y) & NextTo(x,z) )",
	    "exists x exists y ( Honey(x) & Honey(y) & NextTo(x,y) )",
	    "all x all y all z (Diagonal(x,y) & Diagonal(y,z) -> x=z )",

            "exists x exists y ( Ate(x) & Ate(y) & Diagonal(x,y) )",

	    "exists x (Honey(x) & Ate(x))",

	                ],

	    "outline" : """I have four crumpets on a plate. Two are honey crumpets and the other two just butter. 
     I can eat two crumpets but must leave two for my freind. Of course, I want to have at least one of the Honey crumpets. 
     But unfortunately, the warm honey has run into the crumpets, and I cannot tell, or remember, which are the honey ones.
     However, I do remember that the two honey crumpets were next to each other. Is there a way to take two and be
     sure that I get a honey crumpet?<p>
     <b>Domain:</b> You should take the <i>domain of quantification</i> to be the set of crumpets on the plate. 
    """,

	    "notes": [ """
	               The NextTo and Diagonal relations are both <b>anti-relfexive</b> and <b>symmetric</b>.
	               """ ]

	},
	
}
