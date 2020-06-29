import argparse
import codecs
from event import generateEvent, generateCalendar

#TODO: Pendent passar com a paràmetre d'entrada
days = ["0701", "0702", "0703", 
    "0706", "0707", "0708", "0709", "0710", "0713", 
    "0714", "0715", "0716", "0717", "0720", "0721", 
    "0722", "0723", "0724", "0727", "0728", "0729", 
    "0730", "0731"]
hours = [["1000", "1015"], ["1015", "1030"], ["1030", "1045"], ["1030", "1045"], ["1045", "1100"], ["1045", "1100"], 
    ["1100", "1115"], ["1115", "1130"], ["1130", "1145"], ["1130", "1145"], ["1145", "1200"], ["1145", "1200"], 
    ["1200", "1215"], ["1200", "1215"], ["1215", "1230"], ["1215", "1230"], ["1230", "1245"], ["1230", "1245"], ["1245", "1300"], ["1245", "1300"], 
    ["1300", "1315"], ["1300", "1315"], ["1315", "1330"], ["1315", "1330"], ["1330", "1345"], ["1330", "1345"], ["1345", "1400"], ["1345", "1400"]]
#!TODO

#ARGUMENTS
parser = argparse.ArgumentParser(description='Given a CSV file (delimited by tabulates) with XML content column, this task gets the value of it by locale.')
parser.add_argument('--outputfile', dest='output_file', 
    help='Output ICS file name.', type=str, required=True, default='')

args = parser.parse_args()
outputFile = args.output_file

#Generate calendar and events
sb = generateCalendar(days, hours)

f = codecs.open(outputFile, "w", "utf-8")
f.write(sb)
f.close()

print("Done!")