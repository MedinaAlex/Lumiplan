# Start word and open word document
word = win32.gencache.EnsureDispatch('Word.Application');
doc = word.Documents.Open(r"C:\Users\alex.medina-stg@lumiplan.local\Documents/Salut.docx")
word.Visible = False
sleep(1)
 
# Do the work
print(doc)
 
# Close document and quit Microsoft Word
doc.Close(0, 1) # 0 = do not saved changes, 1 = original format
word.Application.Quit()