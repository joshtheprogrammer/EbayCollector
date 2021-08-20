#xml  

import requests
import re

def buy_stuff(UNSORTED_ITEM):
    items = "https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&LH_TitleDesc=0&_sop=15".format(str(UNSORTED_ITEM).replace(" ", "+"))
    unsold = requests.get(items)

    unsoldname1 = re.compile('<li class="s-item[\s\w\-]*" data-view=mi:1686\|iid:1>(.*)<li class="s-item[\s\w\-]*" data-view=mi:1686\|iid:2>')
    unsoldname2 = re.compile('<li class="s-item[\s\w\-]*" data-view=mi:1686\|iid:2>(.*)<li class="s-item[\s\w\-]*" data-view=mi:1686\|iid:3>')    
    unsoldname3 = re.compile('<li class="s-item[\s\w\-]*" data-view=mi:1686\|iid:3>(.*)<li class="s-item[\s\w\-]*" data-view=mi:1686\|iid:4>')
    unsoldtitle = re.compile('(<h3 class=s-item__title>|<h3 class="s-item__title s-item__title--has-tags">)(<span class=LIGHT_HIGHLIGHT>)?(New Listing)?(</span>)?(<span class=BOLD>)?(.*)(</span>)?</h3>')
    unsoldprice = re.compile('<span class=s-item__price>(<span class=ITALIC>)?(\$\d*.\d*)(</span>)?(<span class=DEFAULT> to </span>)?(\$\d*.\d*)?</span>')

    unsold1 = str(unsoldtitle.search(unsoldname1.search(unsold.text).group(1)).group(6)).split("</span>")[0], str(unsoldprice.search(unsoldname1.search(unsold.text).group(1)).group(2)), str(unsoldprice.search(unsoldname1.search(unsold.text).group(1)).group(5))
    unsold2 = str(unsoldtitle.search(unsoldname2.search(unsold.text).group(1)).group(6)).split("</span>")[0], str(unsoldprice.search(unsoldname2.search(unsold.text).group(1)).group(2)), str(unsoldprice.search(unsoldname2.search(unsold.text).group(1)).group(5))
    unsold3 = str(unsoldtitle.search(unsoldname3.search(unsold.text).group(1)).group(6)).split("</span>")[0], str(unsoldprice.search(unsoldname3.search(unsold.text).group(1)).group(2)), str(unsoldprice.search(unsoldname3.search(unsold.text).group(1)).group(5))
    print(unsold1, unsold2, unsold3)

buy_stuff(input("item? "))
