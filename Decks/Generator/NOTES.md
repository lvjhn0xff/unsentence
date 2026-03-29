# OBJECTIVES    
    [SHORTNAME]
        | Chapters -> { Chapter Name }
        | Objectives :: #{Objective Number}
        ==> {Objective} 
    
    [SHORTNAME]
        | Chapters -> { Chapter Name }
        | Objectives -> {Objective}
        ==> #{Objective Number}  


    [Objective Count]
        | Chapters -> { Chapter Name }
        | Objective Count 

# SECTIONS    
    :: SECTION LIST ::
        [SHORTNAME]
            | Chapters -> { Chapter Name }
            | Sections :: #{Objective Number}
            ==> {Objective} 
        
        [SHORTNAME]
            | Chapters -> { Chapter Name }
            | Sections  -> {Section}
            ==> {Section Number}

        [Objective Count]
            | Chapters -> { Chapter Name }
            | Sections Count 
    

    :: TERMINOLOGIES ::
        [SHORTNAME]
            | Define -> #{Term}
            ==> {Definition}

        [SHORTNAME]
            | Identify -> #{Definition}
            ==> {Term}
    
    :: NOTES :: 
        [SHORTNAME]
            | Understand -> #{Note}
            ==> {Definition}
        
        [SHORTNAME]
            | Notes of -> #{Section Name}
            ==> {Definition}

    :: UNORDERED SETS :: 
        [SHORTNAME]
            | Select -> #{Name} [Index]
            ==> {Definition}
        
        [SHORTNAME]
            | Notes of -> #{Name} [Index]
            ==> {Definition}

        [SHORTNAME]
            | Notes of -> #{Name} [Index]
            ==> {Definition}

        [SHORTNAME]
            | Item Count of -> #{Name}
            ==> {Definition}

    :: ORDERED SETS :: 
        [SHORTNAME]
            | #{Name}
            | Select -> [Index]
            ==> #{Definition}
        
        [SHORTNAME]
            | #{Name} 
            | Item After [Ordered Item]
            ==> #{Next Ordered Item}

        [SHORTNAME]
            | #{Name}
            | Item Before [Ordered Item]
            ==> #{Previous Ordered Item}
        
        [SHORTNAME]
            | #{Name}
            | Position [Ordered Item]
            ==> #{Position No}

        [SHORTNAME]
            | Item Count of -> #{Name}
            ==> {Definition}

    :: OBJECTS :: 
        [SHORTNAME]
            | #{Object Identifier}
            | #{Property}
            ==> #{Property Value} 

    :: DIRECT CARDS :: 
        [SHORTNAME]
            | #{Question}
            ==> #{Property Value} 

  