# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"


class PostIt(object):
    background_color = ""
    text = ""
    text_color = ""

postit1 = PostIt()
postit2 = PostIt()
postit3 = PostIt()

postit1.background_color = "orange"
postit1.text_color = "blue"
postit1.text = "Idea 1"

postit2.background_color = "pink"
postit2.text_color = "black"
postit2.text = "Awesome"

postit3.background_color = "yellow"
postit3.text_color = "green"
postit3.text = "Superb!"

print(postit1.background_color, postit1.text_color, postit1.text)
print(postit2.background_color, postit2.text_color, postit2.text)
print(postit3.background_color, postit3.text_color, postit3.text)