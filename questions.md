
## Questions
### Time complexity. What tradeoffs did I make:
1. I choose to built the front-end solution with TailwindCSS styling because using a front-end component framework with built in solution like React+AntD would be costly in configuration terms.
2. I choose to save each csv in a dictionary with the key being the ID of the entity and the value being the entity itself for instant access by the ID. During the exercise, discovered that I could have saved in other formats for faster aggregations, but kept the initial format to save time.
3. I had problems structuring the template folder inside the app folder for better isolation of context, so I put it into my_project as a general template folder

### How would I change my solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
Since the code tries to follow SOLID patterns(although it could be refactored to achieve better SOLID patterns), the Open Closed principle says it woulld not affect to much, since its open for new features but closed for modifications. 

Probably it would need add lines to:
1. the model of the entity to add these new attributes
2. the creator of the entity, the Parser, to add these new attributes
3. the bill analyser class that would need to get these data from the model and set into the output data

### How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
I would change only the Parsers file, wich is responsible to translate the CSV into expected structure.

### How long did I spend working on the assignment?
about 8 hours in 4 splitted times. 3 hours on back-end, 4 hours on frontend(had to learn TailwindCSS for this process although not required in project description) and 1 hour on documentation