# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"G571.00","system":"readv2"},{"code":"G571.11","system":"readv2"},{"code":"G574.00","system":"readv2"},{"code":"327..00","system":"readv2"},{"code":"328..00","system":"readv2"},{"code":"G574100","system":"readv2"},{"code":"328Z.00","system":"readv2"},{"code":"G574z00","system":"readv2"},{"code":"G570z00","system":"readv2"},{"code":"G570.00","system":"readv2"},{"code":"3282","system":"readv2"},{"code":"G576500","system":"readv2"},{"code":"G57y900","system":"readv2"},{"code":"I47.2","system":"readv2"},{"code":"I47.1","system":"readv2"},{"code":"I49.0","system":"readv2"},{"code":"I49.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('arrhythmia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["supraventricular-arrhythmia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["supraventricular-arrhythmia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["supraventricular-arrhythmia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
