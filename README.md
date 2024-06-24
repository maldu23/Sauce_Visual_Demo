# Sauce_Visual_Demo

# Step 1: install dependencies

```
brew install python3

pip install saucelabs_visual
```


# Step 2: Create your custom scripts

You will create 3 scripts. I personally like to name them based on the customer website.

1. visualTemplate.py runs on google chrome. You will create a functional script on the customer website. The visualTemplate.py script is a template that you can use. It has comments that recommends how to create the functional script and where to take screenshots for your visual test.


2. visualTemplateF.py should be an exact copy of your Chrome test, except run it on Firefox. 

3. visualTemplateF_.py will be the same as visualTemplateF.py, however you will add in embedded javascript that will introduce visual changes into the customer website.

Again, you can find instructions on how to do all of this in each of the scripts themselves through the comments. Feel free to rename the files based on the customer name as well.

# Step 3: Ensure you are displaying proper results

1. In order to properly display value of Sauce visual, your visualTemplate.py script should go to the customer website, go through a simple functional test, take a screenshot on a few pages and pass. 

2. After you run a successful visualTemplateF.py, accept the baseline.

3. Lastly run the visualTemplateF_.py. Your functional test SHOULD pass (if not, modify your test until you have a passing functional test. This may require you to modify the rest of the scripts as well). Your visual test should show up as "For Review". 

4. When you look into the visual test in the dashboard, you should see a comparison between the screenshots you took in visualTemplateF.py and visualTemplateF_.py. This will highlight any changes that you introduced with the embedded javascript earlier.