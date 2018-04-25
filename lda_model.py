from gensim import corpora,models,matutils
from docutils.parsers.rst.directives import encoding

weibo_lda_model = models.ldamodel.LdaModel.load(fname="weibo_lda50.model",mmap='r'); 
print("weibo_lad_model has done!!!");
for i in range(10):
    print(weibo_lda_model.print_topic(i));
print("end!!");