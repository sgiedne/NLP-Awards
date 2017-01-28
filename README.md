# NLP-Awards

Eureka's comments:
1/26/2017
- I'm working on find_presenter.py on my branch
- I realized that building the program so that it detects the presenter after giving it an award name is more difficult than detecting the award name from tweets about presenters. This is because awards have several names and it is unclear how those names will show up in the dataset. 
- Currently, my program can return tweets that include the presenter names and exclude tweets that talk about presenters who introduce nominees (but not the awards themselves). For example, John Legend introduced La La Land, which was a nominee for an award, but not the actual award itself. 
- Next, I'm going to figure out how to divide the tweet into useful chunks so that the program can detect potential presenter names or Twitter handles. 
