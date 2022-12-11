# pyconvert
This script convert a binary file into its hex representation used to store into SQL Server VARBINARY fields

## Script arguments
```
-h, --help                show this help message and exit
-t {encode,decode}, 
--type {encode,decode}    Conversion type  (REQUIRED)
-i FILEINPUT, 
--fileinput FILEINPUT     Input file  (REQUIRED)
-o FILEOUTPUT, 
--fileoutput FILEOUTPUT   Output file  (REQUIRED)
```

### Examples
```python
# Convert PDF into hex (varbinary)
python3 pyconvert.py -t encode -i ./test.pdf -o ./econde.txt

# Convert hex (varbinary) into PDF
python3 pyconvert.py -t decode -i ./encode.txt -o ./test2.pdf
```