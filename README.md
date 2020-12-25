# Christmas List Sorter

## How?

This sorts your christmas list to put the best stuff at the top. Pretty self explanatory.

The input for your christmas list to be ranked should be in a file called "wish_list.tsv", a "tab-separated values" file. The file should be formated like this:

> Gift I want (you know, the one? with the thing?)`TAB`buy.thething.com<br/>
> Other givt`TAB`amazon.com/other_givt_or_whatever?thegivtIwant=youknowtheone<br/>
> Cheese`TAB`Idon'tcarewhatcheese.com

You can choose what to put on either side of the tab (instead of `DESCRIPTION` and `URL`). The program can parse anything as long as each line has exactly one `TAB`.

The output will justify the tab-separated columns to the largest item in the left column, and it's convenient to have links in the right column to reference if you can't choose a preference.

## Why?

By handing the brunt of the labor to python's sorting algorithm, the program can minimize the comparisons you have to make in order to place every item at the right spot in the list.

Also cause it's cool. I've meant for a long time to make a list sorting program with a manual entry `compare()` function.<br/>
I'll probably make this a more generalized use case moving forward. For sure it will remain a manual sort.