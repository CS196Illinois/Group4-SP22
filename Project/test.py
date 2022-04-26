from msilib import Table
from unicodedata import name
from keywords import extractors

class whytry:
    def __init__(self, script):
        self.script = script
    def keyword_extract(self):
       extractor = extractors.KeyBertExtractor(self.script)
       return extractor.get_n_best(5)



def guess_word(script):
    first_words = whytry(script)
    guess_word = first_words.keyword_extract()
    final_word = {}
    for x in guess_word:
        for y in x[0].split(" "):
            if y in final_word:
                final_word[y] += guess_word[1] 
            else:
                final_word[y] = guess_word[1]
    sorted_keys = sorted(final_word)
    return sorted_keys[0:3]
script = "Christopher Nolan reprised his duties as director, and brought his brother, Jonathan, to co-write the script for the second installment. The Dark Knight featured Christian Bale reprising his role as Batman/Bruce Wayne, Heath Ledger as The Joker, and Aaron Eckhart as Harvey Dent / Two-Face. Katie Holmes turned down her role as Rachel, and Maggie Gyllenhaal was cast instead. Principal photography began in April 2007 in Chicago and concluded in November. Other locations included Pinewood Studios, Ministry of Sound in London and Hong Kong. On January 22, 2008, after he had completed filming The Dark Knight, Ledger died from an accidental overdose of prescription medication. Warner Bros. had created a viral marketing campaign for The Dark Knight, developing promotional websites and trailers highlighting screen shots of Ledger as the Joker, but after Ledger's death, the studio refocused its promotional campaign.[107][108] The film depicts Batman fighting The Joker, aided by the prosecution of charismatic District Attorney Harvey Dent. The Joker tests Batman's resolve when he causes Rachel's death and Dent's transformation into the disfigured criminal Two-Face. Although Batman is able to stop the Joker from forcing two ferries - one loaded with civilians and the other with prisoners - to destroy each other, he is forced to take the blame for the murders committed by Dent to ensure that Gotham's citizens do not lose hope for the future. The film received broad critical acclaim,[109][110][111] and set numerous records during its theatrical run.[112] With just over $1 billion in revenue worldwide, it became the 4th-highest-grossing film of all time, unadjusted for inflation.[113] The film received eight Academy Award nominations; it won the award for Best Sound Editing and Ledger was posthumously awarded Best Supporting Actor. Critics and film writers often cite The Dark Knight as one of the best films of the 2000s."
tryhard = guess_word(script)
print(tryhard)
