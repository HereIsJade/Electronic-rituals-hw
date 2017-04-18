import sys
import markov

text=''
lines=list()
with open("quotes_rick.txt") as f:
    content = f.readlines()
# remove whitespace characters like `\n` at the end of each line
sentences = [x.strip() for x in content if x!='\n' ]
for sentence in sentences:
    sentence=sentence.translate(None,'"')
    lines.append(sentence)
    # print sentence
    # text+=sentence
print '\n'.join(markov.char_level_generate(lines, 5, count=4))
#
# model = markov.build_model(text.split(), 3)
# print model
# generated = markov.generate(model, 3)
# # print generated
# print ' '.join(generated)
