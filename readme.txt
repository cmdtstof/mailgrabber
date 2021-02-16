mailgrabber
*************************
1) holt sich mails aus draft
2) schreibt alle mails, in ein txt/odt/html (draftnotes)
3) saves mail in archiv folder
4) del mail in mailbox (option)

TODO##########################################33
>>> code



#### improvments
- DONE: schreibt mails je nach TO: in specific file (india@allg > india_allg.odt)
- DONE: erstellen einer liste aller TO: adressen mit mapping zu specific file
 
#### usage:
~/bin/mailgrabber [options > code]


#### dev:
objects
- mailserver (connect, nextMail (> mail)
- mail (getToAdresse, getSubject, getText, getDatum)
- writer.txt / writer.odt (txt, odt > )
- 

#### testing

python3 test/app_mailgrabber.py -v
>>>>> python3 -m unittest discover -v

???? full functional test???


#### ablauf:
- getoptions
- ms.connect
- for mail in ms.nextMail()

