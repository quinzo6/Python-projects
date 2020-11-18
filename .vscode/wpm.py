# Very shi*y wpm calculator

import time

start = input("Are you ready to start?: ") 

if start == "yes":
    print("Words per minute (WPM) is a measure of typing speed, commonly used in recruitment. For the purposes of WPM measurement a word is standardized to five characters or keystrokes.")
    print("Therefore, 'brown' counts as one word, but 'accounted' counts as two. The benefits of a standardized measurement of input speed are that it enables comparison across language and hardware boundaries.")
    print("The speed of an Afrikaans-speaking operator in Cape Town can be compared with a French-speaking operator in Paris.")
    
    start_time = time.time()
    text = input(": ")
    end_time = time.time()

    total_time = end_time - start_time
    rounded_time = int(total_time)
    calculated_time =  (137 * 60) / rounded_time
    final_wpm = str(calculated_time)

    if text == "Editing is a growing field of work in the service industry. Paid editing services may be provided by specialized editing firms or by self-employed (freelance) editors. Editing firms may employ a team of in-house editors, rely on a network of individual contractors or both. Such firms are able to handle editing in a wide range of topics and genres, depending on the skills of individual editors. The services provided by these editors may be varied and can include proofreading, copy editing, online editing, developmental editing, editing for search engine optimization (SEO), etc. Self-employed editors work directly for clients or offer their services through editing firms, or both. They may specialize in a type of editing and in a particular subject area. Those who work directly for authors and develop professional relationships with them are called authors' editors.":
        print("Your wpm is " + final_wpm + "!")
    else:
        print("Your wpm is " + final_wpm + "!")
else:
    print("Script ended")
    exit()