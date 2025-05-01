#output makefileone
makefileone.txt:makefiletwo.txt
	python3 makefileone.py makefileone.txt

#output makefiletwo
makefiletwo.txt:
	python3 makefiletwo.py makefiletwo.txt

#removes makefileone and makefiletwo .txt files from directory when make clean is run
clean:
	rm -f *.txt
