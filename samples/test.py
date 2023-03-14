import stanza

# process_options = "tokenize,mwt,pos,lemma,ner"
# stanza.download(lang="es", processors=process_options)
# nlp = stanza.Pipeline(lang="es", processors=process_options, download_method=None)
# # doc = nlp("SERÍAN, abrirlo, las diez de la mañana de un día de octubre. En el patio de la Escuela de Arquitectura, grupos de estudiantes esperaban a que se abriera la clase.")
# doc = nlp("SERÍAN abrirlo encontrarse")
# for i, sentence in enumerate(doc.sentences):
#     print(f'====== Sentence {i+1} tokens =======')
#     print(*[len(token.words) for token in sentence.tokens], sep='\n')

with open("samples/sample.txt", "r") as text:
    print(text.read().encode("unicode_escape"))