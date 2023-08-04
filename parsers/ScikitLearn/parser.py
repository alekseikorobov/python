dict_org = {}
dict_ru = {}

def line(dict, l):
    s = l.split('\t')
    k = s[1].replace('\n','');
    dict[k] = s[0]


with open('data/examp_org.txt') as f:
    r = f.readlines()
    for l in r:
        line(dict_org, l)

with open('data/examp_ru.txt') as f:
    r = f.readlines()
    for l in r:
        line(dict_ru, l)

# print(len(dict_org))
# print(len(dict_ru))

for d1 in dict_org:
    if d1 in dict_ru:
        print(d1,':\t',dict_org[d1], '->\t' ,dict_ru[d1])



#line('svm/plot_linearsvc_support_vectors.html#sphx-glr-auto-examples-svm-plot-linearsvc-support-vectors-py\tPlot the support vectors in LinearSVC\n')
#line('preprocessing/plot_discretization_classification.html#sphx-glr-auto-examples-preprocessing-plot-discretization-classification-py\tFeature discretization\n')

