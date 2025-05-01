#output makefileone
makefileone.txt:makefiletwo.txt
	python3 makefileone.py makefileone.txt

#output makefiletwo
makefiletwo.txt:
	python3 makefiletwo.py makefiletwo.txt

clean:
	rm -f *.txt
