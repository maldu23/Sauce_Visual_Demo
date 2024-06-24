# Sauce_Visual_Demo

# Step 1: install dependencies

```
brew install python3
pip install saucelabs_visual
```


# Step 2: Create your custom scripts

You will create 3 scripts. I personally like to name them based on the customer website.

The first script will be run on google chrome. You will create a functional script on the customer website. The visualTemplate.py script is a template that you can use. It has comments that recommends how to create the functional script and where to take screenshots for your visual test.


The second script should be an exact copy of your Chrome test, except you run it on Firefox. 

Lastly, the third script will be the same as your Firefox script, however you will add in embedded javascript that will introduce visual changes into the customer website.

Again, you can find instructions on how to do all of this in each of the scripts themselves through the comments.