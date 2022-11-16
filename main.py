#from PyPDF2 import PdfFileReader
import tools
import glob
import tqdm
files = glob.glob("../paper_fig/[1-4].png")
Entxt = "En_5.txt"
Jatxt = "Ja_5.txt"
text_l = []
files.sort()
cnt = 0
for i in files:
    print(i)
    text_l.extend(list(tools.img_to_str(i).split()))
#print(text_l)

f = open(Entxt, "w")
print("Making English document...")
string = tools.to_str(text_l)
f.write(tools.divide_sentence(string))

f.close()

print("translating English into Japanese...")

out_f = open(Jatxt, "w")
# cnt = 0
f = open(Entxt, "r")
f_list = f.readlines()
for i in tqdm.tqdm(range(len(f_list))):
    out_f.write(tools.translate(f_list[i]))

    #=====debug=====
    # cnt+=1
    # if(cnt >= 10):
    #     break
f.close()
out_f.close()

